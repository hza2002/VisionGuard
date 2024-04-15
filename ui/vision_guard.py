# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vision_guard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_VisionGuard(object):
    def setupUi(self, VisionGuard):
        if not VisionGuard.objectName():
            VisionGuard.setObjectName(u"VisionGuard")
        VisionGuard.resize(951, 710)
        self.horizontalLayoutWidget_3 = QWidget(VisionGuard)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 933, 689))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.function_list = QLabel(self.horizontalLayoutWidget_3)
        self.function_list.setObjectName(u"function_list")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.function_list.setFont(font)

        self.horizontalLayout_10.addWidget(self.function_list)

        self.security_alarm = QCheckBox(self.horizontalLayoutWidget_3)
        self.security_alarm.setObjectName(u"security_alarm")
        self.security_alarm.setEnabled(True)
        self.security_alarm.setMouseTracking(True)
        self.security_alarm.setTabletTracking(False)
        self.security_alarm.setAcceptDrops(False)
        self.security_alarm.setAutoFillBackground(False)
        self.security_alarm.setChecked(False)
        self.security_alarm.setTristate(False)

        self.horizontalLayout_10.addWidget(self.security_alarm)

        self.track_detection = QCheckBox(self.horizontalLayoutWidget_3)
        self.track_detection.setObjectName(u"track_detection")

        self.horizontalLayout_10.addWidget(self.track_detection)

        self.heatmap = QCheckBox(self.horizontalLayoutWidget_3)
        self.heatmap.setObjectName(u"heatmap")

        self.horizontalLayout_10.addWidget(self.heatmap)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.settings = QPushButton(self.horizontalLayoutWidget_3)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_10.addWidget(self.settings)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.video_screen = QLabel(self.horizontalLayoutWidget_3)
        self.video_screen.setObjectName(u"video_screen")
        self.video_screen.setMinimumSize(QSize(670, 450))
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.video_screen)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.whole_img = QLabel(self.horizontalLayoutWidget_3)
        self.whole_img.setObjectName(u"whole_img")
        self.whole_img.setMinimumSize(QSize(100, 120))
        self.whole_img.setAutoFillBackground(False)
        self.whole_img.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.whole_img.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.whole_img)

        self.face_img = QLabel(self.horizontalLayoutWidget_3)
        self.face_img.setObjectName(u"face_img")
        self.face_img.setMinimumSize(QSize(100, 120))
        self.face_img.setAutoFillBackground(False)
        self.face_img.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.face_img.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.face_img)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.label = QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.label_6 = QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_9 = QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_2 = QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gender = QLabel(self.horizontalLayoutWidget_3)
        self.gender.setObjectName(u"gender")

        self.verticalLayout_6.addWidget(self.gender)

        self.age = QLabel(self.horizontalLayoutWidget_3)
        self.age.setObjectName(u"age")

        self.verticalLayout_6.addWidget(self.age)

        self.appearance = QLabel(self.horizontalLayoutWidget_3)
        self.appearance.setObjectName(u"appearance")

        self.verticalLayout_6.addWidget(self.appearance)

        self.hair = QLabel(self.horizontalLayoutWidget_3)
        self.hair.setObjectName(u"hair")

        self.verticalLayout_6.addWidget(self.hair)

        self.clothes = QLabel(self.horizontalLayoutWidget_3)
        self.clothes.setObjectName(u"clothes")

        self.verticalLayout_6.addWidget(self.clothes)

        self.expression = QLabel(self.horizontalLayoutWidget_3)
        self.expression.setObjectName(u"expression")

        self.verticalLayout_6.addWidget(self.expression)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_3 = QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.alarm_list = QListWidget(self.horizontalLayoutWidget_3)
        self.alarm_list.setObjectName(u"alarm_list")
        self.alarm_list.setMinimumSize(QSize(250, 200))
        self.alarm_list.setSizeIncrement(QSize(319, 300))
        self.alarm_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.alarm_list.setSelectionRectVisible(False)

        self.verticalLayout_3.addWidget(self.alarm_list)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_4)

        self.summary_type = QComboBox(self.horizontalLayoutWidget_3)
        self.summary_type.addItem("")
        self.summary_type.addItem("")
        self.summary_type.addItem("")
        self.summary_type.setObjectName(u"summary_type")

        self.horizontalLayout_16.addWidget(self.summary_type)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.summary_plot = QLabel(self.horizontalLayoutWidget_3)
        self.summary_plot.setObjectName(u"summary_plot")
        self.summary_plot.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary_plot.sizePolicy().hasHeightForWidth())
        self.summary_plot.setSizePolicy(sizePolicy)
        self.summary_plot.setMinimumSize(QSize(0, 250))
        self.summary_plot.setSizeIncrement(QSize(0, 0))
        self.summary_plot.setAutoFillBackground(False)
        self.summary_plot.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.summary_plot)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(VisionGuard)

        QMetaObject.connectSlotsByName(VisionGuard)
    # setupUi

    def retranslateUi(self, VisionGuard):
        VisionGuard.setWindowTitle(QCoreApplication.translate("VisionGuard", u"\u8d26\u6237\u767b\u5f55\u754c\u9762", None))
        self.function_list.setText(QCoreApplication.translate("VisionGuard", u"\u529f\u80fd\u5217\u8868", None))
        self.security_alarm.setText(QCoreApplication.translate("VisionGuard", u"\u5b89\u5168\u8b66\u62a5", None))
        self.track_detection.setText(QCoreApplication.translate("VisionGuard", u"\u8f68\u8ff9\u68c0\u6d4b", None))
        self.heatmap.setText(QCoreApplication.translate("VisionGuard", u"\u70ed\u56fe", None))
        self.settings.setText(QCoreApplication.translate("VisionGuard", u"\u8bbe\u7f6e", None))
        self.video_screen.setText("")
        self.label_8.setText(QCoreApplication.translate("VisionGuard", u"\u8b66\u62a5\u8be6\u7ec6\u4fe1\u606f", None))
        self.whole_img.setText("")
        self.face_img.setText("")
        self.label_7.setText(QCoreApplication.translate("VisionGuard", u"\u6027\u522b\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("VisionGuard", u"\u5e74\u9f84\uff1a", None))
        self.label.setText(QCoreApplication.translate("VisionGuard", u"\u989c\u503c\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("VisionGuard", u"\u5934\u53d1\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("VisionGuard", u"\u8863\u7740\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("VisionGuard", u"\u8868\u60c5\uff1a", None))
        self.gender.setText("")
        self.age.setText("")
        self.appearance.setText("")
        self.hair.setText("")
        self.clothes.setText("")
        self.expression.setText("")
        self.label_3.setText(QCoreApplication.translate("VisionGuard", u"\u8b66\u62a5\u53d1\u751f\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("VisionGuard", u"\u76d1\u63a7\u60c5\u51b5\u7edf\u8ba1", None))
        self.summary_type.setItemText(0, QCoreApplication.translate("VisionGuard", u"\u6bcf\u5206\u949f", None))
        self.summary_type.setItemText(1, QCoreApplication.translate("VisionGuard", u"\u6bcf\u5c0f\u65f6", None))
        self.summary_type.setItemText(2, QCoreApplication.translate("VisionGuard", u"\u6bcf\u5929", None))

        self.summary_plot.setText("")
    # retranslateUi

