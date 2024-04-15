import json
import os
import sys

import cv2
import qdarkstyle
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = VisionGuardMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("VisionGuard")
        self.intruder_monitor = IntruderMonitor(
            670, 450, enable_detect=True, enable_track=False, enable_heatmap=False
        )

        # self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.camera = cv2.VideoCapture(0)

        # 初始化长度
        self.number = 0
        self.email = 0

        # 设置摄像头捕获的帧大小
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 670)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 30)

        # 复选框按钮
        self.ui.track_detection.stateChanged.connect(self.toggle_track)
        self.ui.heatmap.stateChanged.connect(self.toggle_heatmap)
        # listwidget按钮
        self.ui.alarm_list.itemClicked.connect(self.on_item_clicked)
        # 人脸注册按钮
        self.ui.settings.clicked.connect(self.face_register)
        # 下拉框
        # self.ui.summary_type.currentIndexChanged.connect(self.handleComboBox)
        self.login_face_widget = FaceRegister()

        self.show()

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.resize(frame, (670, 450))
            frame, _, ids = self.intruder_monitor(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.ui.video_screen.setPixmap(QPixmap.fromImage(q_img))

        if self.number != len(self.intruder_monitor.logger):
            for i in ids:
                verified = (
                    "Know" if self.intruder_monitor.logger[i]["verified"] else "Unknow"
                )
                current_time = QDateTime.currentDateTime().toString(
                    "yyyy-MM-dd hh:mm:ss"
                )
                item = QListWidgetItem(
                    " ".join([verified, "person", str(i), current_time])
                )
                self.ui.alarm_list.addItem(item)
                if self.intruder_monitor.logger[i]["verified"] == False:
                    item.setBackground(QColor("red"))
                    if self.ui.security_alarm.isChecked():
                        item_count = self.ui.alarm_list.count()
                        id = int(
                            self.ui.alarm_list.item(item_count - 1).text().split()[2]
                        )
                        Email().send_email(
                            content="Warning from VisionGuard " + current_time,
                            image=self.intruder_monitor.logger[id]["frame"],
                        )

        self.number = len(self.intruder_monitor.logger)

    def on_item_clicked(self, item):
        id = int(item.text().split()[2])

        whole_img = cv2.resize(self.intruder_monitor.logger[id]["frame"], (299, 151))
        # whole_img = cv2.cvtColor(whole_img, cv2.COLOR_BGR2RGB)
        h, w, ch = whole_img.shape
        bytes_per_line = ch * w
        q_img = QImage(whole_img, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.ui.whole_img.setPixmap(pixmap)

        x1, y1, x2, y2 = self.intruder_monitor.logger[id]["box"]
        face_image = self.intruder_monitor.logger[id]["frame"][
            int(y1) : int(y2), int(x1) : int(x2)
        ]
        face_image = cv2.resize(face_image, (199, 151))
        # face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        h, w, ch = face_image.shape
        bytes_per_line = ch * w
        q_img = QImage(face_image, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.ui.face_img.setPixmap(pixmap)

        filename = "face_feature.jpg"
        filepath = os.path.join(os.path.dirname(__file__), "resource", filename)
        cv2.imwrite(filepath, face_image)
        result = face_feature.run(filepath)
        print(result)

        try:
            os.remove(filepath)
            print(f"文件 {filepath} 已成功删除")
        except OSError as e:
            print(f"删除文件 {filepath} 时出错: {e}")

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
        if state == 2:
            self.intruder_monitor.tracker.enable_track = True
        else:
            self.intruder_monitor.tracker.enable_track = False

    def toggle_heatmap(self, state):
        if state == 2:
            self.intruder_monitor.tracker.enable_heatmap = True
        else:
            self.intruder_monitor.tracker.enable_heatmap = False

    def face_register(self):

        self.login_face_widget.show()

    # def handleComboBox(self, index):
    #     selected_option = self.comboBox.itemText(index)
    #     if selected_option == "每小时":
    #
    #     elif selected_option == "每分钟":
    #
    #     elif selected_option == "每天":

    def closeEvent(self, event):
        self.camera.release()
        event.accept()


class LoginAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("账户登录")
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
        self.setWindowTitle("人脸登录")

        self.camera = cv2.VideoCapture(0)

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


class FaceRegister(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = FaceRegisterWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("人脸注册")

        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 821)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 611)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 30)

        # ret, frame = self.camera.read()
        # h, w, ch = frame.shape
        # self.register=Register(w,h)
        self.timertimer = QTimer(self)
        self.timertimer.timeout.connect(self.face_detection)
        self.timertimer.start(1000 / 30)

        self.ui.register_completeness.setRange(0, 100)
        self.ui.register_completeness.setValue(0)

        # 人脸录入按钮
        self.ui.type_in.clicked.connect(self.type_in)
        # 人脸删除按钮
        self.ui.face_delete.clicked.connect(self.delete_face)
        # 打开文件
        self.ui.face_bank.itemDoubleClicked.connect(self.open_file)
        # 修改按钮
        self.ui.modify.clicked.connect(self.email_modify)
        # 返回按钮
        self.ui.return_button.clicked.connect(self.returnmainwindow)
        # 录入按钮
        self.ui.type_in.clicked.connect(self.face_in)
        self.click_count = 0

        # 加载人脸库
        self.folder_path = "resource/verified_face"
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

    def face_detection(self):
        # 单张人脸检测
        ret, frame = self.camera.read()
        # register_image = self.register("test_file", frame)
        # if register_image is None:
        #     print("Multiple faces or no faces detected!")
        # else:
        #     self.ui.single_face.setChecked()
        # if self.ui.single_face.isChecked():
        #     self.ui.type_in.setEnabled(True)
        # else:
        #     self.ui.type_in.setEnabled(False)

    def load_face_bank(self):
        self.ui.face_bank.clear()
        files = os.listdir(self.folder_path)
        for file in files:
            item = QListWidgetItem(file)
            self.ui.face_bank.addItem(item)

    def returnmainwindow(self):
        self.close()

    def type_in(self):
        filename = "current_frame.png"
        filepath = os.path.join(os.path.dirname(__file__), "resource", filename)
        # 保存当前帧到资源文件夹
        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite(filepath, frame)

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
        os.system(f"start {file_path}")

    def face_in(self):
        # 获取输入的名称
        name = self.ui.face_name.text().strip()
        if not name:
            QMessageBox.information(self, "提示", "请输入名称")
            return
        self.ui.face_name.setReadOnly(True)

        # 更新进度条
        self.click_count += 1
        progress = self.click_count * 20
        self.ui.register_completeness.setValue(progress)

        # 截取帧并保存到文件夹中
        ret, frame = self.camera.read()
        filename = f"{name}_{self.click_count}.jpg"
        filepath = os.path.join(self.folder_path, filename)
        cv2.imwrite(filepath, frame)
        self.load_face_bank()

        # 如果已经点击了五次，显示提示框
        if self.click_count == 5:
            QMessageBox.information(self, "提示", "录入完成")
            self.ui.register_completeness.setValue(0)
            self.ui.face_name.clear()
            self.ui.face_name.setReadOnly(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    window = VisionGuardApp()
    # window = LoginAccount()
    sys.exit(app.exec())
