import os
from collections import defaultdict

import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.solutions import heatmap

from utils.config import Config


class ObjectTrack:
    def __init__(
        self,
        width,
        height,
        enable_track=False,
        enable_heatmap=False,
    ):
        self.width = width
        self.height = height
        self.enable_track = enable_track
        self.enable_heatmap = enable_heatmap

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

    def plot_heatmap(self, frame, results):
        return self.heatmap_obj.generate_heatmap(frame, results)

    def plot_track(self, frame, results):
        if results[0].boxes.id is not None and results[0].masks is not None:
            masks = results[0].masks.xy
            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()

            for mask, box, track_id in zip(masks, boxes, track_ids):
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
        results = self.model.track(frame, persist=True, classes=self.classes)
        return results

    def __call__(self, frame):
        results = self.run(frame)
        frame = results[0].plot()
        if self.enable_track:
            frame = self.plot_track(frame, results)
        if self.enable_heatmap:
            frame = self.plot_heatmap(frame, results)
        return frame


if __name__ == "__main__":
    source = 0  # camera
    cap = cv2.VideoCapture(source)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    object_track = ObjectTrack(w, h, enable_track=True, enable_heatmap=True)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = object_track(frame)
        cv2.imshow("Object Track", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()