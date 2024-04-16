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
    QDialog, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_VisionGuard(object):
    def setupUi(self, VisionGuard):
        if not VisionGuard.objectName():
            VisionGuard.setObjectName(u"VisionGuard")
        VisionGuard.resize(1100, 740)
        VisionGuard.setMinimumSize(QSize(1100, 740))
        VisionGuard.setMaximumSize(QSize(1100, 740))
        VisionGuard.setSizeIncrement(QSize(951, 710))
        self.horizontalLayout_8 = QHBoxLayout(VisionGuard)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.function_list = QLabel(VisionGuard)
        self.function_list.setObjectName(u"function_list")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.function_list.setFont(font)

        self.horizontalLayout_10.addWidget(self.function_list)

        self.security_alarm = QCheckBox(VisionGuard)
        self.security_alarm.setObjectName(u"security_alarm")
        self.security_alarm.setEnabled(True)
        self.security_alarm.setMouseTracking(True)
        self.security_alarm.setTabletTracking(False)
        self.security_alarm.setAcceptDrops(False)
        self.security_alarm.setAutoFillBackground(False)
        self.security_alarm.setChecked(False)
        self.security_alarm.setTristate(False)

        self.horizontalLayout_10.addWidget(self.security_alarm)

        self.track_detection = QCheckBox(VisionGuard)
        self.track_detection.setObjectName(u"track_detection")

        self.horizontalLayout_10.addWidget(self.track_detection)

        self.heatmap = QCheckBox(VisionGuard)
        self.heatmap.setObjectName(u"heatmap")

        self.horizontalLayout_10.addWidget(self.heatmap)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.settings = QPushButton(VisionGuard)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_10.addWidget(self.settings)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.video_screen = QLabel(VisionGuard)
        self.video_screen.setObjectName(u"video_screen")
        self.video_screen.setMinimumSize(QSize(720, 404))
        self.video_screen.setMaximumSize(QSize(720, 404))
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.video_screen)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(VisionGuard)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(VisionGuard)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 25))
        self.label_7.setMaximumSize(QSize(40, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_7.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.gender = QLabel(VisionGuard)
        self.gender.setObjectName(u"gender")
        self.gender.setMinimumSize(QSize(122, 25))
        self.gender.setMaximumSize(QSize(16777215, 25))
        self.gender.setFont(font1)
        self.gender.setStyleSheet(u"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.gender)

        self.label_5 = QLabel(VisionGuard)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 25))
        self.label_5.setMaximumSize(QSize(40, 25))
        self.label_5.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.age = QLabel(VisionGuard)
        self.age.setObjectName(u"age")
        self.age.setMinimumSize(QSize(122, 25))
        self.age.setMaximumSize(QSize(16777215, 25))
        self.age.setFont(font1)
        self.age.setStyleSheet(u"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.age)

        self.label = QLabel(VisionGuard)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 25))
        self.label.setMaximumSize(QSize(40, 25))
        self.label.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.appearance = QLabel(VisionGuard)
        self.appearance.setObjectName(u"appearance")
        self.appearance.setMinimumSize(QSize(122, 25))
        self.appearance.setMaximumSize(QSize(16777215, 25))
        self.appearance.setFont(font1)
        self.appearance.setStyleSheet(u"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.appearance)

        self.label_6 = QLabel(VisionGuard)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 25))
        self.label_6.setMaximumSize(QSize(40, 25))
        self.label_6.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.hair = QLabel(VisionGuard)
        self.hair.setObjectName(u"hair")
        self.hair.setMinimumSize(QSize(122, 25))
        self.hair.setMaximumSize(QSize(16777215, 25))
        self.hair.setFont(font1)
        self.hair.setStyleSheet(u"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.hair)

        self.label_2 = QLabel(VisionGuard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 25))
        self.label_2.setMaximumSize(QSize(40, 25))
        self.label_2.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.expression = QLabel(VisionGuard)
        self.expression.setObjectName(u"expression")
        self.expression.setMinimumSize(QSize(122, 25))
        self.expression.setMaximumSize(QSize(16777215, 25))
        self.expression.setFont(font1)
        self.expression.setStyleSheet(u"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.expression)

        self.label_9 = QLabel(VisionGuard)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(40, 25))
        self.label_9.setMaximumSize(QSize(40, 25))
        self.label_9.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.clothes = QLabel(VisionGuard)
        self.clothes.setObjectName(u"clothes")
        self.clothes.setMinimumSize(QSize(122, 25))
        self.clothes.setMaximumSize(QSize(16777215, 25))
        self.clothes.setFont(font1)
        self.clothes.setStyleSheet(u"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.clothes)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.face_img = QLabel(VisionGuard)
        self.face_img.setObjectName(u"face_img")
        self.face_img.setMinimumSize(QSize(202, 202))
        self.face_img.setMaximumSize(QSize(202, 202))
        self.face_img.setAutoFillBackground(False)
        self.face_img.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.face_img.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.face_img)

        self.whole_img = QLabel(VisionGuard)
        self.whole_img.setObjectName(u"whole_img")
        self.whole_img.setMinimumSize(QSize(360, 202))
        self.whole_img.setMaximumSize(QSize(360, 202))
        self.whole_img.setAutoFillBackground(False)
        self.whole_img.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.whole_img.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.whole_img)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(VisionGuard)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.alarm_list = QListWidget(VisionGuard)
        self.alarm_list.setObjectName(u"alarm_list")
        self.alarm_list.setMinimumSize(QSize(320, 420))
        self.alarm_list.setMaximumSize(QSize(320, 420))
        self.alarm_list.setSizeIncrement(QSize(320, 420))
        self.alarm_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.alarm_list.setSelectionRectVisible(False)

        self.verticalLayout_7.addWidget(self.alarm_list)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_4 = QLabel(VisionGuard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.summary_type = QComboBox(VisionGuard)
        self.summary_type.addItem("")
        self.summary_type.addItem("")
        self.summary_type.addItem("")
        self.summary_type.setObjectName(u"summary_type")
        self.summary_type.setMinimumSize(QSize(76, 0))

        self.horizontalLayout_16.addWidget(self.summary_type)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.summary_plot = QLabel(VisionGuard)
        self.summary_plot.setObjectName(u"summary_plot")
        self.summary_plot.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary_plot.sizePolicy().hasHeightForWidth())
        self.summary_plot.setSizePolicy(sizePolicy)
        self.summary_plot.setMinimumSize(QSize(320, 210))
        self.summary_plot.setMaximumSize(QSize(320, 210))
        self.summary_plot.setSizeIncrement(QSize(320, 210))
        self.summary_plot.setAutoFillBackground(False)
        self.summary_plot.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.summary_plot)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)


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
        self.label_7.setText(QCoreApplication.translate("VisionGuard", u"\u6027\u522b", None))
        self.gender.setText("")
        self.label_5.setText(QCoreApplication.translate("VisionGuard", u"\u5e74\u9f84", None))
        self.age.setText("")
        self.label.setText(QCoreApplication.translate("VisionGuard", u"\u989c\u503c", None))
        self.appearance.setText("")
        self.label_6.setText(QCoreApplication.translate("VisionGuard", u"\u5934\u53d1", None))
        self.hair.setText("")
        self.label_2.setText(QCoreApplication.translate("VisionGuard", u"\u8868\u60c5", None))
        self.expression.setText("")
        self.label_9.setText(QCoreApplication.translate("VisionGuard", u"\u8863\u7740", None))
        self.clothes.setText("")
        self.face_img.setText("")
        self.whole_img.setText("")
        self.label_3.setText(QCoreApplication.translate("VisionGuard", u"\u8b66\u62a5\u53d1\u751f\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("VisionGuard", u"\u76d1\u63a7\u60c5\u51b5\u7edf\u8ba1", None))
        self.summary_type.setItemText(0, QCoreApplication.translate("VisionGuard", u"\u6bcf\u5206\u949f", None))
        self.summary_type.setItemText(1, QCoreApplication.translate("VisionGuard", u"\u6bcf\u5c0f\u65f6", None))
        self.summary_type.setItemText(2, QCoreApplication.translate("VisionGuard", u"\u6bcf\u5929", None))

        self.summary_plot.setText("")
    # retranslateUi

