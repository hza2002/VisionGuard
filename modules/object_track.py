import os
from collections import defaultdict
from datetime import datetime
from time import time

import cv2
import numpy as np
import torch
from ultralytics import YOLO
from ultralytics.solutions import heatmap

from utils.config import Config


class ObjectTrack:
    def __init__(
        self,
        width,
        height,
        enable_detect=False,
        enable_track=False,
        enable_heatmap=False,
    ):
        self.width = width
        self.height = height
        self.enable_detect = enable_detect
        self.enable_track = enable_track
        self.enable_heatmap = enable_heatmap

        self.start_time = 0
        self.end_time = 0

        self.classes = [0]  # only check person
        model_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../model/",
            Config().cfg["model"]["segment"],
        )
        self.model = YOLO(os.path.join(model_path))
        self.track_history = defaultdict(lambda: [])
        self.heatmap_obj = heatmap.Heatmap()
        self.heatmap_obj.set_args(
            colormap=cv2.COLORMAP_PARULA,
            imw=self.width,
            imh=self.height,
            shape="circle",
            classes_names=self.model.names,
        )

    def display_fps(self, frame):
        self.end_time = time()
        fps = 1 / np.round(self.end_time - self.start_time, 2)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = current_time + f" FPS: {int(fps)}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        return frame

    def plot_heatmap(self, frame, results):
        return self.heatmap_obj.generate_heatmap(frame, results)

    def plot_track(self, frame, results):
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()

            for box, track_id in zip(boxes, track_ids):
                x, y, _, _ = box
                track = self.track_history[track_id]
                track.append((float(x), float(y)))  # x, y center point
                if len(track) > 30:  # retain 90 tracks for 90 frames
                    track.pop(0)

                # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(
                    frame,
                    [points],
                    isClosed=False,
                    color=(230, 230, 230),
                    thickness=10,
                )
        return frame

    def run(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            classes=self.classes,
            verbose=False,
            device="cuda" if torch.cuda.is_available() else "cpu",
        )
        return results

    def __call__(self, frame):
        self.start_time = time()
        results = self.run(frame)
        if self.enable_detect:
            frame = results[0].plot()
        if self.enable_track:
            frame = self.plot_track(frame, results)
        if self.enable_heatmap:
            frame = self.plot_heatmap(frame, results)
        frame = self.display_fps(frame)
        return frame, results


if __name__ == "__main__":
    source = 0  # camera
    cap = cv2.VideoCapture(source)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    object_track = ObjectTrack(
        w, h, enable_detect=True, enable_track=False, enable_heatmap=False
    )
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame, _ = object_track(frame)
        cv2.imshow("Object Track", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
