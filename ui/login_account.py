# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_account.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginAccount(object):
    def setupUi(self, LoginAccount):
        if not LoginAccount.objectName():
            LoginAccount.setObjectName(u"LoginAccount")
        LoginAccount.resize(513, 343)
        self.face_login_button = QPushButton(LoginAccount)
        self.face_login_button.setObjectName(u"face_login_button")
        self.face_login_button.setGeometry(QRect(80, 280, 101, 31))
        self.label = QLabel(LoginAccount)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 491, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(LoginAccount)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 170, 82, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName(u"label1")

        self.verticalLayout.addWidget(self.label1)

        self.label2 = QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName(u"label2")

        self.verticalLayout.addWidget(self.label2)

        self.verticalLayoutWidget_2 = QWidget(LoginAccount)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(170, 170, 241, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user_name = QLineEdit(self.verticalLayoutWidget_2)
        self.user_name.setObjectName(u"user_name")

        self.verticalLayout_2.addWidget(self.user_name)

        self.password = QLineEdit(self.verticalLayoutWidget_2)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password)

        self.account_login_button = QPushButton(LoginAccount)
        self.account_login_button.setObjectName(u"account_login_button")
        self.account_login_button.setGeometry(QRect(310, 280, 101, 31))
        self.icon = QLabel(LoginAccount)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(220, 40, 69, 19))

        self.retranslateUi(LoginAccount)

        QMetaObject.connectSlotsByName(LoginAccount)
    # setupUi

    def retranslateUi(self, LoginAccount):
        LoginAccount.setWindowTitle(QCoreApplication.translate("LoginAccount", u"\u8d26\u6237\u767b\u5f55\u754c\u9762", None))
        self.face_login_button.setText(QCoreApplication.translate("LoginAccount", u"\u4eba\u8138\u9a8c\u8bc1\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("LoginAccount", u"Vision Guard", None))
        self.label1.setText(QCoreApplication.translate("LoginAccount", u"\u7528\u6237\u540d\uff1a", None))
        self.label2.setText(QCoreApplication.translate("LoginAccount", u"\u5bc6\u7801\uff1a", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("LoginAccount", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginAccount", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.account_login_button.setText(QCoreApplication.translate("LoginAccount", u"\u8d26\u53f7\u5bc6\u7801\u767b\u5f55", None))
        self.icon.setText(QCoreApplication.translate("LoginAccount", u"    \u56fe\u6807", None))
    # retranslateUi

