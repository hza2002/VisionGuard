import os
import sys

import cv2
import qdarkstyle
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from modules.login import Login
from modules.object_track import ObjectTrack
from ui.login_account import Ui_LoginAccount as LoginWindow
from ui.login_face import Ui_LoginFace as LoginFaceWindow
from ui.vision_guard import Ui_VisionGuard as VisionGuardMainWindow


class VisionGuardApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = VisionGuardMainWindow()
        self.ui.setupUi(self)
        self.object_track = ObjectTrack(603, 360, enable_track=False, enable_heatmap=False)

        self.camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        # 设置摄像头捕获的帧大小
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 603)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 30)

        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)

        #复选框按钮
        self.ui.track_detection.stateChanged.connect(self.toggle_track)
        self.ui.heatmap.stateChanged.connect(self.toggle_heatmap)


        self.show()

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.resize(frame, (603, 360))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = self.object_track(frame)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.ui.video_screen.setPixmap(QPixmap.fromImage(q_img))

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.ui.time_process_label.setText(current_time)

    def toggle_track(self, state):
        if state == 2:
            self.object_track.enable_track = True
        else:
            self.object_track.enable_track = False

    def toggle_heatmap(self, state):
        if state == 2:
            self.object_track.enable_heatmap = True
        else:
            self.object_track.enable_heatmap = False

    def closeEvent(self, event):
        self.camera.release()
        event.accept()


class LoginAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.face_login_button.clicked.connect(self.face_login)
        self.ui.account_login_button.clicked.connect(self.account_login)

    def face_login(self):
        self.hide()
        self.login_face_widget = LoginFace()
        self.login_face_widget.show()

    def account_login(self):
        username = self.ui.user_name.text()
        password = self.ui.password.text()

        if Login().account_login(username, password):
            # If login successful, switch to the VisionGuardApp window
            self.hide()
            self.vision_guard_widget = VisionGuardApp()
            self.vision_guard_widget.show()
            QMessageBox.information(
                self, "Login Success", "Welcome to the vision guard"
            )
        else:
            # Display an error message or handle unsuccessful login
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")


class LoginFace(QWidget):
    # face = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = LoginFaceWindow()
        self.ui.setupUi(self)

        self.camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 30)

        # 人脸验证按钮
        self.ui.face_verification_button.clicked.connect(self.face_verification)
        # 返回按钮
        self.ui.return_button.clicked.connect(self.returnlogin)

        self.show()

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.ui.face_img.setPixmap(QPixmap.fromImage(q_img))

    def face_verification(self):
        filename = "current_frame.png"
        filepath = os.path.join(os.path.dirname(__file__), "resource", filename)

        # 保存当前帧到资源文件夹
        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite(filepath, frame)

            # 调用人脸比对函数
            result = Login().face_login(filepath)
            if result:
                print("Face login successful!")
                os.remove(filepath)
                self.hide()
                self.vision_guard_widget = VisionGuardApp()
                self.vision_guard_widget.show()
                QMessageBox.information(
                    self, "Login Success", "Welcome to the vision guard"
                )
            else:
                print("Face login failed!")
                os.remove(filepath)
                QMessageBox.warning(self, "Login Failed", "Face login failed!")

    def returnlogin(self):

        self.hide()
        self.login_account_widget = LoginAccount()
        self.login_account_widget.show()

    def closeEvent(self, event):
        self.camera.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    window = LoginAccount()
    sys.exit(app.exec())
