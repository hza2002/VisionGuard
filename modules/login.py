import os

import face_recognition
import xfyun_liveness_detection as liveness_detection


class Login:
    def __init__(self) -> None:
        self.__data_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../resource/account.data"
        )
        self.__face_directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../resource/verified_face/"
        )
        if not os.path.exists(self.__data_path):
            with open(self.__data_path, "w") as file:
                file.write("admin,admin\n")

    def face_compare(self, img_path) -> bool:
        files = os.listdir(self.__face_directory)
        face_images = [
            os.path.join(self.__face_directory, file)
            for file in files
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")
        ]
        verified_faces = []
        for image in face_images:
            verified_face = face_recognition.load_image_file(image)
            verified_face_encoding = face_recognition.face_encodings(verified_face)[0]
            verified_faces.append(verified_face_encoding)

        unknown_image = face_recognition.load_image_file(img_path)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces(verified_faces, unknown_encoding, 0.6)
        if all(not item for item in results):  # 比对结果全为False
            return False
        return True

    def face_login(self, img_path) -> bool:
        # 静默活体检测
        if not liveness_detection.run(img_path):
            print("Liveness detection failed!")
            return False
        # 和已验证人脸数据进行比对
        if not self.face_compare(img_path):
            print("Face compare failed!")
            return False
        return True

    def account_login(self, username, password) -> bool:
        with open(self.__data_path, "r") as file:
            accounts = file.readlines()
            for account in accounts:
                stored_username, stored_password = account.strip().split(",")
                if stored_username == username and stored_password == password:
                    return True
        return False


if __name__ == "__main__":
    print(Login().account_login("admin", "admin"))
    print(Login().account_login("hza", "tbw"))
    know_img_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/know_face.jpeg"
    )
    unknow_img_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/unknow_face.jpg"
    )
    print(Login().face_login(know_img_path))
    print(Login().face_login(unknow_img_path))
