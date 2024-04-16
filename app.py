import json
import os
import subprocess
import sys

import cv2
import qdarkstyle
from PySide6.QtCore import QTimer
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QListWidgetItem, QMessageBox, QWidget

import modules.summary_chart as summary
import modules.tencent_face_feature as face_feature
from modules.intruder_monitor import IntruderMonitor
from modules.login import Login
from modules.register import Register
from ui.face_register import Ui_FaceRegister as FaceRegisterWindow
from ui.login_account import Ui_LoginAccount as LoginWindow
from ui.login_face import Ui_LoginFace as LoginFaceWindow
from ui.vision_guard import Ui_VisionGuard as VisionGuardMainWindow
from utils.alarm_email import Email


class VisionGuardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = VisionGuardMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("VisionGuard")

        self.intruder_monitor = IntruderMonitor(
            self.ui.video_screen.width(),
            self.ui.video_screen.height(),
            enable_detect=True,
            enable_track=False,
            enable_heatmap=False,
        )
        # 设置摄像头捕获的帧大小
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.ui.video_screen.width())
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.ui.video_screen.height())

        self.recorded_logger = 0  # 已经记录日志数量
        self.email_count = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 15)

        # 复选框按钮
        self.ui.track_detection.stateChanged.connect(self.toggle_track)
        self.ui.heatmap.stateChanged.connect(self.toggle_heatmap)
        # listwidget按钮
        self.ui.alarm_list.itemClicked.connect(self.on_item_clicked)
        # 下拉框
        self.interval = "min"  # default "每分钟":
        self.ui.summary_type.currentIndexChanged.connect(self.handleComboBox)

    def update_frame(self):
        success, qframe = self.camera.read()
        if not success:
            return

        qframe, _, ids = self.intruder_monitor(qframe)
        qframe = cv2.cvtColor(qframe, cv2.COLOR_BGR2RGB)  # BGR -> RGB
        h, w, ch = qframe.shape
        bytes_per_line = ch * w
        q_img = QImage(qframe.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.ui.video_screen.setPixmap(QPixmap.fromImage(q_img))

        if self.recorded_logger != len(self.intruder_monitor.logger):  # 更新了logger
            for id in ids:
                verified = (
                    "Know" if self.intruder_monitor.logger[id]["verified"] else "Unknow"
                )
                current_time = self.intruder_monitor.logger[id]["time"]
                item = QListWidgetItem(
                    " ".join([verified, "person", str(id), current_time])
                )
                self.ui.alarm_list.addItem(item)
                if self.intruder_monitor.logger[id]["verified"] == False:
                    item.setBackground(QColor("red"))
                    if self.ui.security_alarm.isChecked():
                        Email().send_email(
                            content="Warning from VisionGuard " + current_time,
                            image=self.intruder_monitor.logger[id]["frame"],
                        )
        self.recorded_logger = len(self.intruder_monitor.logger)
        self.update_summary()

    def on_item_clicked(self, item):
        id = int(item.text().split()[2])
        # plot whole frame
        whole_frame = cv2.resize(self.intruder_monitor.logger[id]["frame"], (360, 202))
        h, w, ch = whole_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(whole_frame, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.ui.whole_img.setPixmap(pixmap)
        # plot face frame
        x1, y1, x2, y2 = self.intruder_monitor.logger[id]["box"]
        face_frame = self.intruder_monitor.logger[id]["frame"][
            int(y1) : int(y2), int(x1) : int(x2)
        ]
        face_frame = cv2.resize(face_frame, (202, 202))
        h, w, ch = face_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(face_frame, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.ui.face_img.setPixmap(pixmap)
        # get face feature
        filename = "face_feature.jpg"
        filepath = os.path.join(os.path.dirname(__file__), "resource", filename)
        cv2.imwrite(filepath, face_frame)
        result = face_feature.run(filepath)
        print(result)
        os.remove(filepath)
        # show face feature
        self.ui.gender.setText(str(result["Gender"]))
        self.ui.expression.setText(str(result["Smile"]))
        self.ui.clothes.setText(
            str(result["Glass"] + "/" + result["Hat"] + "/" + result["Mask"])
        )
        self.ui.appearance.setText(str(result["Beauty"]))
        self.ui.hair.setText(
            str(
                result["Hair Length"]
                + "/"
                + result["Hair Bang"]
                + "/"
                + result["Hair Color"]
            )
        )
        self.ui.age.setText(str(result["Age"]))

    def toggle_track(self, state):
        self.intruder_monitor.tracker.enable_track = True if state == 2 else False

    def toggle_heatmap(self, state):
        self.intruder_monitor.tracker.enable_heatmap = True if state == 2 else False

    def update_summary(self):
        img_path = summary.plot_chart(self.intruder_monitor.logger, self.interval)
        q_img = QImage(img_path)
        scaled_q_img = q_img.scaled(self.ui.summary_plot.size())
        self.ui.summary_plot.setPixmap(QPixmap.fromImage(scaled_q_img))

    def handleComboBox(self, index):
        selected_option = self.ui.summary_type.itemText(index)
        interval = "min"  # default "每分钟":
        if selected_option == "每小时":
            interval = "hour"
        elif selected_option == "每天":
            interval = "day"
        self.interval = interval
        self.update_summary()

    def closeEvent(self, event):
        self.camera.release()
        event.accept()

    def hideEvent(self, event):
        self.camera.release()
        event.accept()

    def showEvent(self, event):
        # 设置摄像头捕获的帧大小
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.ui.video_screen.width())
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.ui.video_screen.height())
        event.accept()


class LoginAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("账户登录")
        self.login = Login()
        pixmap = QPixmap("resource/logo/icon.png")
        pixmap = pixmap.scaled(self.ui.icon.width(), self.ui.icon.height())
        self.ui.icon.setPixmap(pixmap)


class LoginFace(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = LoginFaceWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("人脸登录")

        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 25)

        self.login = Login()

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (641, 470))
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.ui.face_img.setPixmap(QPixmap.fromImage(q_img))

    def closeEvent(self, event):
        self.camera.release()
        event.accept()


class FaceRegister(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = FaceRegisterWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("人脸注册")

        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 821)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 611)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 15)

        self.register = Register(720, 450)

        self.ui.register_completeness.setRange(0, 100)
        self.ui.register_completeness.setValue(0)

        # 人脸删除按钮
        self.ui.face_delete.clicked.connect(self.delete_face)
        # 打开文件
        self.ui.face_bank.itemDoubleClicked.connect(self.open_file)
        # 修改按钮
        self.ui.modify.clicked.connect(self.email_modify)
        # 录入按钮
        self.ui.type_in.clicked.connect(self.face_in)
        self.click_count = 0

        # 加载人脸库
        self.folder_path = os.path.join(
            os.path.dirname(__file__), "resource", "verified_face"
        )
        self.load_face_bank()

        # 加载邮箱
        file_path = "resource/config.json"
        config = self.load_json(file_path)
        email_config = config.get("email", {})
        if email_config:
            self.ui.to_email.setText(email_config.get("to_email"))
            self.ui.from_email.setText(email_config.get("from_email"))
            self.ui.email_password.setText(email_config.get("password"))
            self.ui.smtp_name.setText(email_config.get("smtp_name"))

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.resize(frame, (821, 611))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.ui.video_screen.setPixmap(QPixmap.fromImage(q_img))

    def load_face_bank(self):
        self.ui.face_bank.clear()
        files = os.listdir(self.folder_path)
        for file in files:
            item = QListWidgetItem(file)
            self.ui.face_bank.addItem(item)

    def load_json(self, file_path):
        with open(file_path, "r") as file:
            config = json.load(file)
        return config

    def save_config(self, file_path, config):
        with open(file_path, "w") as file:
            json.dump(config, file, indent=4)

    def email_modify(self):
        file_path = "resource/config.json"
        config = self.load_json(file_path)
        config["email"]["to_email"] = self.ui.to_email.text()
        config["email"]["from_email"] = self.ui.from_email.text()
        config["email"]["password"] = self.ui.email_password.text()
        config["email"]["smtp_name"] = self.ui.smtp_name.text()
        self.save_config(file_path, config)

    def delete_face(self):
        selected_items = self.ui.face_bank.selectedItems()
        if selected_items:
            selected_file = selected_items[0].text()
            # 删除文件夹中的文件
            file_path = os.path.join(self.folder_path, selected_file)

            os.remove(file_path)
            # 删除 QListWidget 中的 item
            self.ui.face_bank.takeItem(self.ui.face_bank.row(selected_items[0]))

    def open_file(self, item):
        # 获取双击的文件名
        file_name = item.text()
        file_path = os.path.join(self.folder_path, file_name)
        if sys.platform.startswith("win"):  # Windows
            os.startfile(file_path)
            # subprocess.run(["start", file_path])
        elif sys.platform.startswith("darwin"):  # macOS
            subprocess.run(["open", file_path])
        elif sys.platform.startswith("linux"):  # Linux
            subprocess.run(["xdg-open", file_path])
        else:
            print("Unsupported operating system.")

    def face_in(self):
        # 获取输入的名称
        name = self.ui.face_name.text().strip()
        if not name:
            QMessageBox.information(self, "提示", "请输入名称")
            return
        self.ui.face_name.setReadOnly(True)

        # 截取帧并保存到文件夹中
        ret, frame = self.camera.read()
        if not ret:
            return
        filename = f"{name}_{self.click_count}"
        register_image = self.register(filename, frame)
        if register_image is None:
            QMessageBox.information(self, "提示", "检测到多张人脸或未检测到人脸")
            return
        else:
            self.click_count += 1
            progress = self.click_count * 20
            self.ui.register_completeness.setValue(progress)

        self.load_face_bank()

        # 如果已经点击了五次，显示提示框
        if self.click_count == 5:
            self.click_count = 0
            QMessageBox.information(self, "提示", "录入完成")
            self.ui.register_completeness.setValue(0)
            self.ui.face_name.clear()
            self.ui.face_name.setReadOnly(False)

    def closeEvent(self, event):
        self.camera.release()
        event.accept()

    def hideEvent(self, event):
        self.camera.release()
        event.accept()

    def showEvent(self, event):
        # 设置摄像头捕获的帧大小
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.ui.video_screen.width())
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.ui.video_screen.height())
        event.accept()


class MainWindow:
    def __init__(self):
        self.login_account = LoginAccount()
        self.login_face = LoginFace()
        self.login_account.show()

        self.login_account.ui.face_login_button.clicked.connect(
            self.switch_to_login_face
        )
        self.login_face.ui.return_button.clicked.connect(self.switch_to_login_account)
        self.login_account.ui.account_login_button.clicked.connect(self.account_login)
        self.login_face.ui.face_verification_button.clicked.connect(self.face_login)

    def switch_to_login_account(self):
        self.login_account.show()
        self.login_face.hide()

    def switch_to_login_face(self):
        self.login_face.show()
        self.login_account.hide()

    def account_login(self):
        username = self.login_account.ui.user_name.text()
        password = self.login_account.ui.password.text()

        if self.login_account.login.account_login(username, password):
            # If login successful, switch to the VisionGuardApp window
            self.vision_guard = VisionGuardApp()
            self.vision_guard.ui.settings.clicked.connect(self.switch_to_register)
            self.vision_guard.show()
            self.login_face.hide()
            self.login_account.hide()
            self.login_face.close()
            self.login_account.close()
        else:
            # Display an error message or handle unsuccessful login
            QMessageBox.warning(
                self.login_account, "Login Failed", "Invalid username or password"
            )

    def face_login(self):
        filename = "current_frame.png"
        filepath = os.path.join(os.path.dirname(__file__), "resource", filename)

        ret, frame = self.login_face.camera.read()
        if ret:
            cv2.imwrite(filepath, frame)
            result = self.login_face.login.face_login(filepath)
            if result:
                print("Face login successful!")
                os.remove(filepath)
                self.vision_guard = VisionGuardApp()
                self.vision_guard.ui.settings.clicked.connect(self.switch_to_register)
                self.vision_guard.show()
                self.login_face.hide()
                self.login_account.hide()
                self.login_face.close()
                self.login_account.close()
            else:
                print("Face login failed!")
                os.remove(filepath)
                QMessageBox.warning(
                    self.login_face, "Login Failed", "Face login failed!"
                )

    def switch_to_register(self):
        self.register = FaceRegister()
        self.register.ui.return_button.clicked.connect(self.switch_to_vision_guard)
        self.register.show()
        self.vision_guard.hide()

    def switch_to_vision_guard(self):
        self.vision_guard.show()
        self.register.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    mainwindow = MainWindow()
    sys.exit(app.exec())
