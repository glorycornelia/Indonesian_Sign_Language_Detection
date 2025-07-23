# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainoujCtl.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setMaximumSize(QSize(1200, 700))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(70, 40))
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(255, 157, 218);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 157, 218);\n"
"       color: rgb(0, 0, 0); \n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 157, 218);\n"
"       color: rgb(0, 0, 0); \n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 157, 218);\n"
"       color: rgb(0, 0, 0); \n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tittle_page_1 = QLabel(self.page_1)
        self.tittle_page_1.setObjectName(u"tittle_page_1")
        self.tittle_page_1.setMinimumSize(QSize(0, 60))
        self.tittle_page_1.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(20)
        self.tittle_page_1.setFont(font)
        self.tittle_page_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tittle_page_1.setTextFormat(Qt.RichText)
        self.tittle_page_1.setScaledContents(False)
        self.tittle_page_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.tittle_page_1)

        self.frame_content_page_1 = QFrame(self.page_1)
        self.frame_content_page_1.setObjectName(u"frame_content_page_1")
        self.frame_content_page_1.setFrameShape(QFrame.StyledPanel)
        self.frame_content_page_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_content_page_1)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(100, 40, 100, 40)
        self.label_3 = QLabel(self.frame_content_page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.image_box = QLabel(self.frame_content_page_1)
        self.image_box.setObjectName(u"image_box")
        self.image_box.setMinimumSize(QSize(500, 400))
        self.image_box.setMaximumSize(QSize(500, 400))
        self.image_box.setPixmap(QPixmap(u"images/72631756_9756520.jpg"))
        self.image_box.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.image_box)


        self.verticalLayout_7.addWidget(self.frame_content_page_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tittle_page_2 = QLabel(self.page_2)
        self.tittle_page_2.setObjectName(u"tittle_page_2")
        self.tittle_page_2.setMinimumSize(QSize(0, 60))
        self.tittle_page_2.setMaximumSize(QSize(16777215, 60))
        self.tittle_page_2.setFont(font)
        self.tittle_page_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tittle_page_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.tittle_page_2)

        self.frame_content_page_2 = QFrame(self.page_2)
        self.frame_content_page_2.setObjectName(u"frame_content_page_2")
        self.frame_content_page_2.setFrameShape(QFrame.StyledPanel)
        self.frame_content_page_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_camera = QFrame(self.frame_content_page_2)
        self.frame_camera.setObjectName(u"frame_camera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_camera.sizePolicy().hasHeightForWidth())
        self.frame_camera.setSizePolicy(sizePolicy1)
        self.frame_camera.setMaximumSize(QSize(16777215, 16777215))
        self.frame_camera.setLayoutDirection(Qt.LeftToRight)
        self.frame_camera.setFrameShape(QFrame.NoFrame)
        self.frame_camera.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_camera)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.camera_box = QLabel(self.frame_camera)
        self.camera_box.setObjectName(u"camera_box")
        self.camera_box.setMaximumSize(QSize(640, 480))
        self.camera_box.setMinimumSize(QSize(640, 480))
        self.camera_box.setScaledContents(True)
        font1 = QFont()
        font1.setPointSize(12)
        self.camera_box.setFont(font1)
        self.camera_box.setStyleSheet(u"background-color: rgb(91, 91, 91);")
        self.camera_box.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.camera_box)


        self.verticalLayout_9.addWidget(self.frame_camera)

        self.frame_text_display = QFrame(self.frame_content_page_2)
        self.frame_text_display.setObjectName(u"frame_text_display")
        self.frame_text_display.setMinimumSize(QSize(0, 60))
        self.frame_text_display.setMaximumSize(QSize(16777215, 60))
        self.frame_text_display.setFrameShape(QFrame.StyledPanel)
        self.frame_text_display.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_text_display)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(100, 9, 100, -1)
        self.label_text_display = QLabel(self.frame_text_display)
        self.label_text_display.setObjectName(u"label_text_display")
        self.label_text_display.setMaximumSize(QSize(155, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(QFont.Weight.Bold)
        self.label_text_display.setFont(font2)
        self.label_text_display.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_text_display)

        self.indicator = QLabel(self.frame_text_display)
        self.indicator.setObjectName(u"indicator")
        self.indicator.setMinimumSize(QSize(15, 15))
        self.indicator.setMaximumSize(QSize(15, 15))
        self.indicator.setStyleSheet(u"background-color: rgb(255, 157, 218);")

        self.horizontalLayout_5.addWidget(self.indicator)

        self.label_content_text_display = QLabel(self.frame_text_display)
        self.label_content_text_display.setObjectName(u"label_content_text_display")
        self.label_content_text_display.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_content_text_display)


        self.verticalLayout_9.addWidget(self.frame_text_display)

        self.frame_button = QFrame(self.frame_content_page_2)
        self.frame_button.setObjectName(u"frame_button")
        self.frame_button.setMinimumSize(QSize(0, 60))
        self.frame_button.setMaximumSize(QSize(16777215, 60))
        self.frame_button.setFrameShape(QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_button)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(100, -1, 100, -1)
        self.btn_open_camera = QPushButton(self.frame_button)
        self.btn_open_camera.setObjectName(u"btn_open_camera")
        self.btn_open_camera.setMinimumSize(QSize(0, 35))
        self.btn_open_camera.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(QFont.Weight.Bold)
        self.btn_open_camera.setFont(font3)
        self.btn_open_camera.setStyleSheet(u"background-color: rgb(255, 157, 218);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.btn_open_camera)

        self.btn_close_camera = QPushButton(self.frame_button)
        self.btn_close_camera.setObjectName(u"btn_close_camera")
        self.btn_close_camera.setMinimumSize(QSize(0, 35))
        self.btn_close_camera.setMaximumSize(QSize(16777215, 35))
        self.btn_close_camera.setFont(font3)
        self.btn_close_camera.setStyleSheet(u"background-color: rgb(143, 143, 143);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.btn_close_camera)


        self.verticalLayout_9.addWidget(self.frame_button)


        self.verticalLayout_6.addWidget(self.frame_content_page_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tittle_page_3 = QLabel(self.page_3)
        self.tittle_page_3.setObjectName(u"tittle_page_3")
        self.tittle_page_3.setMinimumSize(QSize(0, 60))
        self.tittle_page_3.setMaximumSize(QSize(16777215, 60))
        self.tittle_page_3.setFont(font)
        self.tittle_page_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tittle_page_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.tittle_page_3)

        self.frame_content_page_3 = QFrame(self.page_3)
        self.frame_content_page_3.setObjectName(u"frame_content_page_3")
        self.frame_content_page_3.setFrameShape(QFrame.StyledPanel)
        self.frame_content_page_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_content_page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 40, -1, 40)
        self.frame_video_upload = QFrame(self.frame_content_page_3)
        self.frame_video_upload.setObjectName(u"frame_video_upload")
        self.frame_video_upload.setMinimumSize(QSize(0, 80))
        self.frame_video_upload.setMaximumSize(QSize(16777215, 80))
        self.frame_video_upload.setFrameShape(QFrame.StyledPanel)
        self.frame_video_upload.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_video_upload)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(100, -1, 100, -1)
        self.label_video_text = QLabel(self.frame_video_upload)
        self.label_video_text.setObjectName(u"label_video_text")
        self.label_video_text.setStyleSheet(u"background-color: rgb(91, 91, 91);\n"
"color: rgb(255, 255, 255);")
        self.label_video_text.setMargin(10)

        self.horizontalLayout_7.addWidget(self.label_video_text)

        self.btn_video_upload = QPushButton(self.frame_video_upload)
        self.btn_video_upload.setObjectName(u"btn_video_upload")
        self.btn_video_upload.setMinimumSize(QSize(200, 40))
        self.btn_video_upload.setMaximumSize(QSize(200, 40))
        self.btn_video_upload.setStyleSheet(u"background-color: rgb(143, 143, 143);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.btn_video_upload)


        self.verticalLayout_11.addWidget(self.frame_video_upload)

        self.frame_detection_btn = QFrame(self.frame_content_page_3)
        self.frame_detection_btn.setObjectName(u"frame_detection_btn")
        self.frame_detection_btn.setMinimumSize(QSize(0, 80))
        self.frame_detection_btn.setMaximumSize(QSize(16777215, 80))
        self.frame_detection_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_detection_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_detection_btn)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(100, -1, 100, -1)
        self.btn_detection = QPushButton(self.frame_detection_btn)
        self.btn_detection.setObjectName(u"btn_detection")
        self.btn_detection.setMinimumSize(QSize(0, 40))
        self.btn_detection.setMaximumSize(QSize(16777215, 40))
        self.btn_detection.setFont(font3)
        self.btn_detection.setStyleSheet(u"background-color: rgb(255, 157, 218);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.btn_detection)


        self.verticalLayout_11.addWidget(self.frame_detection_btn)

        self.frame_text_display_2 = QFrame(self.frame_content_page_3)
        self.frame_text_display_2.setObjectName(u"frame_text_display_2")
        self.frame_text_display_2.setMinimumSize(QSize(0, 80))
        self.frame_text_display_2.setMaximumSize(QSize(16777215, 80))
        self.frame_text_display_2.setFrameShape(QFrame.StyledPanel)
        self.frame_text_display_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_text_display_2)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(100, 9, 100, -1)
        self.label_text_display_2 = QLabel(self.frame_text_display_2)
        self.label_text_display_2.setObjectName(u"label_text_display_2")
        self.label_text_display_2.setMaximumSize(QSize(200, 16777215))
        self.label_text_display_2.setFont(font2)
        self.label_text_display_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_text_display_2)

        self.label_content_text_display_2 = QLabel(self.frame_text_display_2)
        self.label_content_text_display_2.setObjectName(u"label_content_text_display_2")
        self.label_content_text_display_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_content_text_display_2)


        self.verticalLayout_11.addWidget(self.frame_text_display_2)


        self.verticalLayout_8.addWidget(self.frame_content_page_3)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Real Time", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.tittle_page_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ff9dda;\">Sign Language</span><span style=\" font-weight:600;\"> Detection</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The Sign Language Detection App is an application designed to recognize and interpret BISINDO (Bahasa Isyarat Indonesia) in real time. This app leverages the MediaPipe framework to extract pose and hand landmarks, capturing essential movement data for accurate sign detection.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Using a Long Short-Term Memory (LSTM) model,"
                        " the app processes these landmark sequences to classify and predict sign language gestures effectively. The combination of spatiotemporal data analysis and deep learning ensures high accuracy and adaptability in recognizing diverse BISINDO signs.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff9dda;\">Created By: Glory Cornelia Patining Kurik</span></p></body></html>", None))
        self.image_box.setText("")
        self.tittle_page_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ff9dda;\">Real Time</span><span style=\" font-weight:600;\"> Detection</span></p></body></html>", None))
        self.camera_box.setText("")
        self.label_text_display.setText(QCoreApplication.translate("MainWindow", u"Translation Text :", None))
        self.indicator.setText("")
        self.label_content_text_display.setText("")
        self.btn_open_camera.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.btn_close_camera.setText(QCoreApplication.translate("MainWindow", u"Close Camera", None))
        self.tittle_page_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ff9dda;\">Video</span><span style=\" font-weight:600;\"> Detection</span></p></body></html>", None))
        self.label_video_text.setText(QCoreApplication.translate("MainWindow", u"Video Tittle", None))
        self.btn_video_upload.setText(QCoreApplication.translate("MainWindow", u"Upload Video", None))
        self.btn_detection.setText(QCoreApplication.translate("MainWindow", u"Translate Now", None))
        self.label_text_display_2.setText(QCoreApplication.translate("MainWindow", u"Translation Text :", None))
        self.label_content_text_display_2.setText("")
    # retranslateUi

