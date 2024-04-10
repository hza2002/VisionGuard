import sys

import qdarkstyle
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.vision_guard import Ui_MainWindow as VisionGuardMainWindow


class VisionGuardApp(QMainWindow, VisionGuardMainWindow):

    def __init__(self, parent=None):
        super(VisionGuardApp, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super(VisionGuardApp, self).closeEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VisionGuardApp()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    window.show()
    sys.exit(app.exec())
