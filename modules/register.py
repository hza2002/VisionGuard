import os

import cv2
import face_recognition

from modules.object_track import ObjectTrack


class Register:
    def __init__(self, width, height):
        self.tracker = ObjectTrack(
            width, height, enable_detect=False, enable_track=False, enable_heatmap=False
        )
        self.verified_face_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../resource/verified_face/"
        )

    def detect_face(self, frame, results):
        if not len(results[0].boxes) == 1:  # 当只有一个人脸时才继续检测
            return None
        x1, y1, x2, y2 = results[0].boxes.xyxy.cpu()[0]
        face_image = frame[int(y1) : int(y2), int(x1) : int(x2)]
        rgb_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        try:
            face_recognition.face_encodings(rgb_image)[0]
        except IndexError:
            return None  # 没有检测出人脸
        return face_image

    def __call__(self, file_name, frame):
        # 若没有检测到人脸返回None
        frame, results = self.tracker(frame)
        face_image = self.detect_face(frame, results)
        if face_image is not None:
            cv2.imwrite(self.verified_face_path + file_name + ".jpg", face_image)
            return face_image
        return None


if __name__ == "__main__":
    # source = os.path.join(
    #     os.path.dirname(os.path.abspath(__file__)),
    #     "../resource/test/multiple_faces.png"
    # )
    source = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/unknow_face.jpg"
    )
    # source = os.path.join(
    #     os.path.dirname(os.path.abspath(__file__)), "../resource/test/cat_face.png"
    # )
    image = cv2.imread(source)
    h, w = image.shape[:2]
    register = Register(w, h)
    register_image = register("test_file", image)
    if register_image is None:
        print("Multiple faces or no faces detected!")
        exec("exit()")
    cv2.imshow("Register image", register_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
