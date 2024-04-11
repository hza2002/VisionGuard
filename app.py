import sys

import qdarkstyle
from PySide6 import QtGui
from PySide6.QtWidgets import *
from ui.vision_guard import Ui_VisionGuard as VisionGuardMainWindow
from ui.login_account import Ui_LoginAccount
from ui.login_face import Ui_LoginFace


class VisionGuardApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = VisionGuardMainWindow()
        self.ui.setupUi(self)
        self.show()

class LoginAcount(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginAccount()
        self.ui.setupUi(self)
        self.show()

class LoginFace(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginFace()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VisionGuardApp()
    sys.exit(app.exec())
#

