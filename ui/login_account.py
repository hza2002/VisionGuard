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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginAccount(object):
    def setupUi(self, LoginAccount):
        if not LoginAccount.objectName():
            LoginAccount.setObjectName(u"LoginAccount")
        LoginAccount.resize(600, 337)
        LoginAccount.setMinimumSize(QSize(600, 337))
        LoginAccount.setMaximumSize(QSize(600, 337))
        self.verticalLayoutWidget_3 = QWidget(LoginAccount)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 581, 321))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.icon = QLabel(self.verticalLayoutWidget_3)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(90, 85))
        self.icon.setMaximumSize(QSize(90, 85))

        self.horizontalLayout_3.addWidget(self.icon)

        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label1 = QLabel(self.verticalLayoutWidget_3)
        self.label1.setObjectName(u"label1")

        self.verticalLayout.addWidget(self.label1)

        self.label2 = QLabel(self.verticalLayoutWidget_3)
        self.label2.setObjectName(u"label2")

        self.verticalLayout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.user_name = QLineEdit(self.verticalLayoutWidget_3)
        self.user_name.setObjectName(u"user_name")

        self.verticalLayout_2.addWidget(self.user_name)

        self.password = QLineEdit(self.verticalLayoutWidget_3)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.face_login_button = QPushButton(self.verticalLayoutWidget_3)
        self.face_login_button.setObjectName(u"face_login_button")
        self.face_login_button.setMinimumSize(QSize(140, 40))
        self.face_login_button.setMaximumSize(QSize(140, 40))

        self.horizontalLayout_2.addWidget(self.face_login_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.account_login_button = QPushButton(self.verticalLayoutWidget_3)
        self.account_login_button.setObjectName(u"account_login_button")
        self.account_login_button.setMinimumSize(QSize(140, 40))
        self.account_login_button.setMaximumSize(QSize(140, 40))

        self.horizontalLayout_2.addWidget(self.account_login_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(3, 2)

        self.retranslateUi(LoginAccount)

        QMetaObject.connectSlotsByName(LoginAccount)
    # setupUi

    def retranslateUi(self, LoginAccount):
        LoginAccount.setWindowTitle(QCoreApplication.translate("LoginAccount", u"\u8d26\u6237\u767b\u5f55\u754c\u9762", None))
        self.icon.setText("")
        self.label.setText(QCoreApplication.translate("LoginAccount", u"Vision Guard", None))
        self.label1.setText(QCoreApplication.translate("LoginAccount", u"\u7528\u6237\u540d\uff1a", None))
        self.label2.setText(QCoreApplication.translate("LoginAccount", u"\u5bc6\u7801\uff1a", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("LoginAccount", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginAccount", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.face_login_button.setText(QCoreApplication.translate("LoginAccount", u"\u4eba\u8138\u9a8c\u8bc1\u767b\u5f55", None))
        self.account_login_button.setText(QCoreApplication.translate("LoginAccount", u"\u8d26\u53f7\u5bc6\u7801\u767b\u5f55", None))
    # retranslateUi

