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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_FaceRegister(object):
    def setupUi(self, FaceRegister):
        if not FaceRegister.objectName():
            FaceRegister.setObjectName(u"FaceRegister")
        FaceRegister.resize(1224, 679)
        FaceRegister.setMinimumSize(QSize(1224, 679))
        self.verticalLayoutWidget = QWidget(FaceRegister)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 60, 111, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName(u"label1")

        self.verticalLayout.addWidget(self.label1)

        self.label2 = QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName(u"label2")

        self.verticalLayout.addWidget(self.label2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayoutWidget = QWidget(FaceRegister)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 391, 59))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.modify = QPushButton(self.horizontalLayoutWidget)
        self.modify.setObjectName(u"modify")
        self.modify.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.modify.setFont(font1)

        self.horizontalLayout.addWidget(self.modify)

        self.horizontalLayoutWidget_2 = QWidget(FaceRegister)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 230, 391, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.face_delete = QPushButton(self.horizontalLayoutWidget_2)
        self.face_delete.setObjectName(u"face_delete")
        self.face_delete.setMinimumSize(QSize(100, 30))
        self.face_delete.setFont(font1)

        self.horizontalLayout_2.addWidget(self.face_delete)

        self.face_bank = QListWidget(FaceRegister)
        self.face_bank.setObjectName(u"face_bank")
        self.face_bank.setGeometry(QRect(0, 270, 391, 421))
        self.horizontalLayoutWidget_3 = QWidget(FaceRegister)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(400, 0, 821, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.single_face = QCheckBox(self.horizontalLayoutWidget_3)
        self.single_face.setObjectName(u"single_face")
        self.single_face.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.single_face)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.face_name = QLineEdit(self.horizontalLayoutWidget_3)
        self.face_name.setObjectName(u"face_name")
        self.face_name.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.face_name)

        self.type_in = QPushButton(self.horizontalLayoutWidget_3)
        self.type_in.setObjectName(u"type_in")
        self.type_in.setMinimumSize(QSize(100, 30))
        self.type_in.setFont(font1)

        self.horizontalLayout_3.addWidget(self.type_in)

        self.return_button = QPushButton(self.horizontalLayoutWidget_3)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setMinimumSize(QSize(100, 30))
        self.return_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.return_button)

        self.video_screen = QLabel(FaceRegister)
        self.video_screen.setObjectName(u"video_screen")
        self.video_screen.setGeometry(QRect(400, 40, 821, 611))
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QFrame.Plain)
        self.layoutWidget = QWidget(FaceRegister)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(400, 650, 821, 29))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.register_completeness = QProgressBar(self.layoutWidget)
        self.register_completeness.setObjectName(u"register_completeness")
        self.register_completeness.setMaximum(30)
        self.register_completeness.setValue(0)

        self.horizontalLayout_4.addWidget(self.register_completeness)

        self.from_email = QLineEdit(FaceRegister)
        self.from_email.setObjectName(u"from_email")
        self.from_email.setGeometry(QRect(110, 70, 279, 24))
        self.to_email = QLineEdit(FaceRegister)
        self.to_email.setObjectName(u"to_email")
        self.to_email.setGeometry(QRect(110, 110, 279, 24))
        self.to_email.setEchoMode(QLineEdit.Normal)
        self.smtp_name = QLineEdit(FaceRegister)
        self.smtp_name.setObjectName(u"smtp_name")
        self.smtp_name.setGeometry(QRect(110, 200, 279, 24))
        self.email_password = QLineEdit(FaceRegister)
        self.email_password.setObjectName(u"email_password")
        self.email_password.setGeometry(QRect(110, 160, 279, 24))

        self.retranslateUi(FaceRegister)

        QMetaObject.connectSlotsByName(FaceRegister)
    # setupUi

    def retranslateUi(self, FaceRegister):
        FaceRegister.setWindowTitle(QCoreApplication.translate("FaceRegister", u"\u8d26\u6237\u767b\u5f55\u754c\u9762", None))
        self.label1.setText(QCoreApplication.translate("FaceRegister", u"\u53d1\u9001\u90ae\u7bb1\uff1a", None))
        self.label2.setText(QCoreApplication.translate("FaceRegister", u"\u63a5\u6536\u90ae\u7bb1\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("FaceRegister", u"\u90ae\u7bb1\u5bc6\u7801\uff1a", None))
        self.label.setText(QCoreApplication.translate("FaceRegister", u"SMTP\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("FaceRegister", u"\u90ae\u7bb1\u8bbe\u7f6e", None))
        self.modify.setText(QCoreApplication.translate("FaceRegister", u"\u4fee\u6539", None))
        self.label_4.setText(QCoreApplication.translate("FaceRegister", u"\u4eba\u8138\u5e93", None))
        self.face_delete.setText(QCoreApplication.translate("FaceRegister", u"\u5220\u9664", None))
        self.label_5.setText(QCoreApplication.translate("FaceRegister", u"\u4eba\u8138\u6ce8\u518c", None))
        self.single_face.setText(QCoreApplication.translate("FaceRegister", u"\u5355\u5f20\u4eba\u8138", None))
        self.type_in.setText(QCoreApplication.translate("FaceRegister", u"\u5f55\u5165", None))
        self.return_button.setText(QCoreApplication.translate("FaceRegister", u"\u8fd4\u56de", None))
        self.video_screen.setText("")
        self.label_6.setText(QCoreApplication.translate("FaceRegister", u"\u5b8c\u6210\u7387", None))
        self.from_email.setPlaceholderText("")
        self.to_email.setPlaceholderText("")
    # retranslateUi

