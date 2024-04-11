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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_VisionGuard(object):
    def setupUi(self, VisionGuard):
        if not VisionGuard.objectName():
            VisionGuard.setObjectName(u"VisionGuard")
        VisionGuard.resize(1252, 735)
        self.gridLayout = QGridLayout(VisionGuard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_7 = QFrame(VisionGuard)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 0, 1, 1, 1)

        self.line_9 = QFrame(VisionGuard)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 0, 2, 8, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.function_list = QLabel(VisionGuard)
        self.function_list.setObjectName(u"function_list")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.function_list.setFont(font)

        self.horizontalLayout_10.addWidget(self.function_list)

        self.security_alarm = QCheckBox(VisionGuard)
        self.security_alarm.setObjectName(u"security_alarm")
        self.security_alarm.setEnabled(True)
        self.security_alarm.setChecked(False)

        self.horizontalLayout_10.addWidget(self.security_alarm)

        self.human_recognition = QCheckBox(VisionGuard)
        self.human_recognition.setObjectName(u"human_recognition")
        self.human_recognition.setEnabled(True)
        self.human_recognition.setChecked(False)

        self.horizontalLayout_10.addWidget(self.human_recognition)

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
        self.settings.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.settings)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.video_screen = QLabel(VisionGuard)
        self.video_screen.setObjectName(u"video_screen")
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QFrame.Plain)

        self.verticalLayout_9.addWidget(self.video_screen)

        self.video_process_bar = QSlider(VisionGuard)
        self.video_process_bar.setObjectName(u"video_process_bar")
        self.video_process_bar.setAutoFillBackground(False)
        self.video_process_bar.setStyleSheet(u" QSlider {\n"
"	background-color: rgba(22, 22, 22, 0.7);\n"
"	border-radius: 5px;\n"
"}\n"
" \n"
"QSlider::sub-page:horizontal {\n"
"	background-color: #FF7826;\n"
"	height:4px;\n"
"	border-radius: 2px;\n"
"}\n"
" \n"
"QSlider::add-page:horizontal {\n"
"	background-color: #7A7B79;\n"
"	height:4px;\n"
"	border-radius: 2px;\n"
"}\n"
" \n"
"QSlider::groove:horizontal {\n"
"	background:transparent;\n"
"	height:10px;\n"
"}\n"
" \n"
"QSlider::handle:horizontal {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	margin: 0px -2px 0px -2px;\n"
"	border-radius: 5px;\n"
"	background: white;\n"
"}")
        self.video_process_bar.setMinimum(-1)
        self.video_process_bar.setMaximum(-1)
        self.video_process_bar.setValue(-1)
        self.video_process_bar.setOrientation(Qt.Horizontal)
        self.video_process_bar.setTickPosition(QSlider.NoTicks)
        self.video_process_bar.setTickInterval(0)

        self.verticalLayout_9.addWidget(self.video_process_bar)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.time_process_label = QLabel(VisionGuard)
        self.time_process_label.setObjectName(u"time_process_label")
        self.time_process_label.setLayoutDirection(Qt.LeftToRight)
        self.time_process_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.time_process_label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.play = QPushButton(VisionGuard)
        self.play.setObjectName(u"play")

        self.horizontalLayout_11.addWidget(self.play)

        self.stop = QPushButton(VisionGuard)
        self.stop.setObjectName(u"stop")

        self.horizontalLayout_11.addWidget(self.stop)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalLayout_9.setStretch(1, 8)
        self.verticalLayout_9.setStretch(3, 1)

        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.line_10 = QFrame(VisionGuard)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_10)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label = QLabel(VisionGuard)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setFont(font)

        self.horizontalLayout_12.addWidget(self.label)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.dateEdit = QDateEdit(VisionGuard)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 4, 8), QTime(16, 0, 0)))

        self.horizontalLayout_13.addWidget(self.dateEdit)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.alarm_detailed_information = QListWidget(VisionGuard)
        self.alarm_detailed_information.setObjectName(u"alarm_detailed_information")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarm_detailed_information.sizePolicy().hasHeightForWidth())
        self.alarm_detailed_information.setSizePolicy(sizePolicy)
        self.alarm_detailed_information.setMinimumSize(QSize(0, 220))
        self.alarm_detailed_information.setSizeIncrement(QSize(0, 250))
        self.alarm_detailed_information.setBaseSize(QSize(0, 250))
        self.alarm_detailed_information.setFlow(QListView.LeftToRight)

        self.verticalLayout_10.addWidget(self.alarm_detailed_information)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)


        self.gridLayout.addLayout(self.verticalLayout_8, 0, 3, 7, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_2 = QLabel(VisionGuard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.dateEdit_2 = QDateEdit(VisionGuard)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setDateTime(QDateTime(QDate(2024, 4, 8), QTime(16, 0, 0)))

        self.horizontalLayout_14.addWidget(self.dateEdit_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.alarm_list = QListWidget(VisionGuard)
        self.alarm_list.setObjectName(u"alarm_list")
        self.alarm_list.setMinimumSize(QSize(415, 0))
        self.alarm_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.alarm_list.setSelectionRectVisible(False)

        self.verticalLayout_12.addWidget(self.alarm_list)

        self.summary_plot = QLabel(VisionGuard)
        self.summary_plot.setObjectName(u"summary_plot")
        self.summary_plot.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.summary_plot.sizePolicy().hasHeightForWidth())
        self.summary_plot.setSizePolicy(sizePolicy1)
        self.summary_plot.setMinimumSize(QSize(0, 200))
        self.summary_plot.setSizeIncrement(QSize(0, 0))
        self.summary_plot.setAutoFillBackground(False)
        self.summary_plot.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.summary_plot)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.line_11 = QFrame(VisionGuard)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_11)

        self.verticalLayout_11.setStretch(0, 7)

        self.gridLayout.addLayout(self.verticalLayout_11, 0, 4, 7, 1)

        self.label_11 = QLabel(VisionGuard)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1)

        self.video_resource = QListWidget(VisionGuard)
        self.video_resource.setObjectName(u"video_resource")

        self.gridLayout.addWidget(self.video_resource, 2, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_channel = QPushButton(VisionGuard)
        self.add_channel.setObjectName(u"add_channel")

        self.horizontalLayout_6.addWidget(self.add_channel)

        self.del_channel = QPushButton(VisionGuard)
        self.del_channel.setObjectName(u"del_channel")

        self.horizontalLayout_6.addWidget(self.del_channel)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 2, 2)

        self.line_8 = QFrame(VisionGuard)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 4, 1, 1, 1)

        self.label_12 = QLabel(VisionGuard)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)

        self.video_file = QListWidget(VisionGuard)
        self.video_file.setObjectName(u"video_file")

        self.gridLayout.addWidget(self.video_file, 6, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.add_video = QPushButton(VisionGuard)
        self.add_video.setObjectName(u"add_video")

        self.horizontalLayout_8.addWidget(self.add_video)

        self.del_video = QPushButton(VisionGuard)
        self.del_video.setObjectName(u"del_video")

        self.horizontalLayout_8.addWidget(self.del_video)


        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 1, 1, 1)


        self.retranslateUi(VisionGuard)

        QMetaObject.connectSlotsByName(VisionGuard)
    # setupUi

    def retranslateUi(self, VisionGuard):
        VisionGuard.setWindowTitle(QCoreApplication.translate("VisionGuard", u"Vision Guard", None))
        self.function_list.setText(QCoreApplication.translate("VisionGuard", u"\u529f\u80fd\u5217\u8868", None))
        self.security_alarm.setText(QCoreApplication.translate("VisionGuard", u"\u5b89\u5168\u8b66\u62a5", None))
        self.human_recognition.setText(QCoreApplication.translate("VisionGuard", u"\u4eba\u50cf\u68c0\u6d4b", None))
        self.track_detection.setText(QCoreApplication.translate("VisionGuard", u"\u8f68\u8ff9\u68c0\u6d4b", None))
        self.heatmap.setText(QCoreApplication.translate("VisionGuard", u"\u70ed\u56fe", None))
        self.settings.setText(QCoreApplication.translate("VisionGuard", u"\u8bbe\u7f6e", None))
        self.video_screen.setText("")
        self.time_process_label.setText(QCoreApplication.translate("VisionGuard", u"00:00:00/00:00:00", None))
        self.play.setText(QCoreApplication.translate("VisionGuard", u"\u64ad\u653e", None))
        self.stop.setText(QCoreApplication.translate("VisionGuard", u"\u6682\u505c", None))
        self.label.setText(QCoreApplication.translate("VisionGuard", u"\u8b66\u62a5\u8be6\u7ec6\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("VisionGuard", u"\u8b66\u62a5\u53d1\u751f\u65f6\u95f4", None))
        self.summary_plot.setText("")
        self.label_11.setText(QCoreApplication.translate("VisionGuard", u"\u89c6\u9891\u901a\u9053", None))
        self.add_channel.setText(QCoreApplication.translate("VisionGuard", u"\u6dfb\u52a0\u901a\u9053", None))
        self.del_channel.setText(QCoreApplication.translate("VisionGuard", u"\u5220\u9664\u901a\u9053", None))
        self.label_12.setText(QCoreApplication.translate("VisionGuard", u"\u672c\u5730\u89c6\u9891", None))
        self.add_video.setText(QCoreApplication.translate("VisionGuard", u"\u4e0a\u4f20\u89c6\u9891", None))
        self.del_video.setText(QCoreApplication.translate("VisionGuard", u"\u5220\u9664\u89c6\u9891", None))
    # retranslateUi

