# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_face.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_LoginFace(object):
    def setupUi(self, LoginFace):
        if not LoginFace.objectName():
            LoginFace.setObjectName(u"LoginFace")
        LoginFace.resize(701, 621)
        self.face_verification_button = QPushButton(LoginFace)
        self.face_verification_button.setObjectName(u"face_verification_button")
        self.face_verification_button.setGeometry(QRect(110, 570, 101, 31))
        self.return_button = QPushButton(LoginFace)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(490, 570, 101, 31))
        self.face_img = QLabel(LoginFace)
        self.face_img.setObjectName(u"face_img")
        self.face_img.setGeometry(QRect(30, 80, 641, 471))
        self.face_img.setMinimumSize(QSize(95, 95))
        self.face_img.setLayoutDirection(Qt.LeftToRight)
        self.face_img.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.face_img.setAlignment(Qt.AlignCenter)
        self.face_img.setOpenExternalLinks(False)
        self.label = QLabel(LoginFace)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 701, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(LoginFace)

        QMetaObject.connectSlotsByName(LoginFace)
    # setupUi

    def retranslateUi(self, LoginFace):
        LoginFace.setWindowTitle(QCoreApplication.translate("LoginFace", u"\u4eba\u8138\u767b\u5f55\u754c\u9762", None))
        self.face_verification_button.setText(QCoreApplication.translate("LoginFace", u"\u4eba\u8138\u9a8c\u8bc1", None))
        self.return_button.setText(QCoreApplication.translate("LoginFace", u"\u8fd4\u56de", None))
        self.face_img.setText("")
        self.label.setText(QCoreApplication.translate("LoginFace", u"\u4eba\u8138\u9a8c\u8bc1\u767b\u5f55", None))
    # retranslateUi

