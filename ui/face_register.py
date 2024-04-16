# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'face_register.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_FaceRegister(object):
    def setupUi(self, FaceRegister):
        if not FaceRegister.objectName():
            FaceRegister.setObjectName(u"FaceRegister")
        FaceRegister.resize(1072, 571)
        FaceRegister.setMinimumSize(QSize(1072, 571))
        FaceRegister.setMaximumSize(QSize(1072, 571))
        self.horizontalLayoutWidget_5 = QWidget(FaceRegister)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 10, 1051, 551))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.face_name = QLineEdit(self.horizontalLayoutWidget_5)
        self.face_name.setObjectName(u"face_name")
        self.face_name.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.face_name)

        self.type_in = QPushButton(self.horizontalLayoutWidget_5)
        self.type_in.setObjectName(u"type_in")
        self.type_in.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.type_in.setFont(font1)

        self.horizontalLayout_3.addWidget(self.type_in)

        self.return_button = QPushButton(self.horizontalLayoutWidget_5)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setMinimumSize(QSize(100, 30))
        self.return_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.return_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.video_screen = QLabel(self.horizontalLayoutWidget_5)
        self.video_screen.setObjectName(u"video_screen")
        self.video_screen.setMinimumSize(QSize(720, 450))
        self.video_screen.setMaximumSize(QSize(720, 450))
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.video_screen)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.register_completeness = QProgressBar(self.horizontalLayoutWidget_5)
        self.register_completeness.setObjectName(u"register_completeness")
        self.register_completeness.setMaximum(30)
        self.register_completeness.setValue(0)

        self.horizontalLayout_4.addWidget(self.register_completeness)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(1, 2)

        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.modify = QPushButton(self.horizontalLayoutWidget_5)
        self.modify.setObjectName(u"modify")
        self.modify.setMinimumSize(QSize(100, 30))
        self.modify.setFont(font1)

        self.horizontalLayout.addWidget(self.modify)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label1 = QLabel(self.horizontalLayoutWidget_5)
        self.label1.setObjectName(u"label1")

        self.verticalLayout.addWidget(self.label1)

        self.label2 = QLabel(self.horizontalLayoutWidget_5)
        self.label2.setObjectName(u"label2")

        self.verticalLayout.addWidget(self.label2)

        self.label_2 = QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget_5)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.from_email = QLineEdit(self.horizontalLayoutWidget_5)
        self.from_email.setObjectName(u"from_email")

        self.verticalLayout_4.addWidget(self.from_email)

        self.to_email = QLineEdit(self.horizontalLayoutWidget_5)
        self.to_email.setObjectName(u"to_email")
        self.to_email.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_4.addWidget(self.to_email)

        self.email_password = QLineEdit(self.horizontalLayoutWidget_5)
        self.email_password.setObjectName(u"email_password")

        self.verticalLayout_4.addWidget(self.email_password)

        self.smtp_name = QLineEdit(self.horizontalLayoutWidget_5)
        self.smtp_name.setObjectName(u"smtp_name")

        self.verticalLayout_4.addWidget(self.smtp_name)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.face_delete = QPushButton(self.horizontalLayoutWidget_5)
        self.face_delete.setObjectName(u"face_delete")
        self.face_delete.setMinimumSize(QSize(100, 30))
        self.face_delete.setFont(font1)

        self.horizontalLayout_2.addWidget(self.face_delete)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.face_bank = QListWidget(self.horizontalLayoutWidget_5)
        self.face_bank.setObjectName(u"face_bank")

        self.verticalLayout_3.addWidget(self.face_bank)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.retranslateUi(FaceRegister)

        QMetaObject.connectSlotsByName(FaceRegister)
    # setupUi

    def retranslateUi(self, FaceRegister):
        FaceRegister.setWindowTitle(QCoreApplication.translate("FaceRegister", u"\u8d26\u6237\u767b\u5f55\u754c\u9762", None))
        self.label_5.setText(QCoreApplication.translate("FaceRegister", u"\u4eba\u8138\u6ce8\u518c", None))
        self.label_7.setText(QCoreApplication.translate("FaceRegister", u"\u7528\u6237\u540d\uff1a", None))
        self.type_in.setText(QCoreApplication.translate("FaceRegister", u"\u5f55\u5165", None))
        self.return_button.setText(QCoreApplication.translate("FaceRegister", u"\u8fd4\u56de", None))
        self.video_screen.setText("")
        self.label_6.setText(QCoreApplication.translate("FaceRegister", u"\u5b8c\u6210\u7387", None))
        self.label_3.setText(QCoreApplication.translate("FaceRegister", u"\u90ae\u7bb1\u8bbe\u7f6e", None))
        self.modify.setText(QCoreApplication.translate("FaceRegister", u"\u4fee\u6539", None))
        self.label1.setText(QCoreApplication.translate("FaceRegister", u"\u53d1\u9001\u90ae\u7bb1\uff1a", None))
        self.label2.setText(QCoreApplication.translate("FaceRegister", u"\u63a5\u6536\u90ae\u7bb1\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("FaceRegister", u"\u90ae\u7bb1\u5bc6\u7801\uff1a", None))
        self.label.setText(QCoreApplication.translate("FaceRegister", u"SMTP\u540d\u79f0\uff1a", None))
        self.from_email.setPlaceholderText("")
        self.to_email.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("FaceRegister", u"\u4eba\u8138\u5e93", None))
        self.face_delete.setText(QCoreApplication.translate("FaceRegister", u"\u5220\u9664", None))
    # retranslateUi

