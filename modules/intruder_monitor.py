import os
from datetime import datetime

import cv2
import face_recognition

from modules.object_track import ObjectTrack


class IntruderMonitor:
    def __init__(
        self,
        width,
        height,
        enable_detect=True,
        enable_track=False,
        enable_heatmap=False,
    ):
        self.tracker = ObjectTrack(
            width, height, enable_detect, enable_track, enable_heatmap
        )
        self.logger = dict()

        self.verified_faces = []
        self.load_verified_faces()

    def load_verified_faces(self):
        # 加载已知人脸
        files = os.listdir(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../resource/verified_face/"
            )
        )
        face_images = [
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "..",
                "resource",
                "verified_face",
                file,
            )
            for file in files
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")
        ]
        for face_image in face_images:
            try:
                verified_face = face_recognition.load_image_file(face_image)
                verified_encoding = face_recognition.face_encodings(verified_face)[0]
                self.verified_faces.append(verified_encoding)
            except Exception as e:
                print("Error:", e)
                continue

    def detect_intruder(self, frame, results):
        if results[0].boxes.id is None:
            return
        boxes = results[0].boxes.xyxy.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        new_track_ids = []
        for box, track_id in zip(boxes, track_ids):
            if not track_id in self.logger:  # 未检验过该目标
                x1, y1, x2, y2 = box
                face_image = frame[int(y1) : int(y2), int(x1) : int(x2)]
                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
                try:
                    unknown_encoding = face_recognition.face_encodings(rgb_image)[0]
                except IndexError:
                    continue
                compare_results = face_recognition.compare_faces(
                    self.verified_faces, unknown_encoding, 0.8
                )

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if all(not item for item in compare_results):
                    self.logger[track_id] = {
                        "verified": False,
                        "track_id": track_id,
                        "frame": frame,
                        "box": box,  # in xyxy format
                        "time": current_time,
                    }
                    print("Unknow person detected", track_id, box, current_time)
                else:
                    self.logger[track_id] = {
                        "verified": True,
                        "track_id": track_id,
                        "frame": frame,
                        "box": box,  # in xyxy format
                        "time": current_time,
                    }
                    print("know person detected", track_id, box, current_time)
                new_track_ids.append(track_id)
        return new_track_ids

    def __call__(self, frame):
        plot_frame, results = self.tracker(frame)
        new_track_ids = self.detect_intruder(frame, results)
        return plot_frame, results, new_track_ids


if __name__ == "__main__":
    source = 0
    cap = cv2.VideoCapture(source)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    intruder_monitor = IntruderMonitor(
        w, h, enable_detect=True, enable_track=False, enable_heatmap=False
    )
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Camera is disconnected!")
            break
        frame, results, new_track_ids = intruder_monitor(frame)
        cv2.imshow("Intruder Monitor", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
