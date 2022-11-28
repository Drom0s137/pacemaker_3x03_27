# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DCM_UI_2.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget
import numpy as np

class Ui_DCM(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
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
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
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
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
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
        self.verticalLayout_3.setSpacing(0)
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
"	background-color: rgb(85, 170, 255);\n"
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
"	background-color: rgb(85, 170, 255);\n"
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
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_4)

        self.btn_page_5 = QPushButton(self.frame_top_menus)
        self.btn_page_5.setObjectName(u"btn_page_5")
        self.btn_page_5.setMinimumSize(QSize(0, 40))
        self.btn_page_5.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_5)

        self.btn_page_6 = QPushButton(self.frame_top_menus)
        self.btn_page_6.setObjectName(u"btn_page_6")
        self.btn_page_6.setMinimumSize(QSize(0, 40))
        self.btn_page_6.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_6)

        self.btn_page_7 = QPushButton(self.frame_top_menus)
        self.btn_page_7.setObjectName(u"btn_page_7")
        self.btn_page_7.setMinimumSize(QSize(0, 40))
        self.btn_page_7.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_7)

        self.btn_page_8 = QPushButton(self.frame_top_menus)
        self.btn_page_8.setObjectName(u"btn_page_8")
        self.btn_page_8.setMinimumSize(QSize(0, 40))
        self.btn_page_8.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_8)


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
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 20, 371, 201))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 111, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 111, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 110, 101, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 150, 111, 16))
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(140, 30, 42, 22))
        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(140, 70, 42, 22))
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(140, 110, 42, 22))
        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(140, 150, 42, 22))
        self.label_11 = QLabel(self.page_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(400, 0, 81, 16))
        self.label_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.graphicsView = QGraphicsView(self.page_1)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 230, 651, 201))
        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 40, 161, 41))
        self.pushButton.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.page_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(690, 100, 161, 41))
        self.pushButton_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 20, 501, 141))
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 101, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 101, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(250, 30, 131, 16))
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(250, 70, 141, 16))
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_9 = QSpinBox(self.groupBox_2)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setGeometry(QRect(150, 30, 42, 22))
        self.spinBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_13 = QSpinBox(self.groupBox_2)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setGeometry(QRect(400, 30, 42, 22))
        self.spinBox_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_14 = QSpinBox(self.groupBox_2)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setGeometry(QRect(400, 70, 42, 22))
        self.spinBox_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_10 = QSpinBox(self.groupBox_2)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setGeometry(QRect(150, 70, 42, 22))
        self.spinBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 40, 141, 41))
        self.pushButton_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(630, 100, 141, 41))
        self.pushButton_4.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.graphicsView_2 = QGraphicsView(self.page_2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(0, 220, 621, 211))
        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(400, 0, 71, 16))
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.groupBox_3 = QGroupBox(self.page_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 20, 561, 171))
        self.groupBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 100, 101, 16))
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_17 = QSpinBox(self.groupBox_3)
        self.spinBox_17.setObjectName(u"spinBox_17")
        self.spinBox_17.setGeometry(QRect(390, 20, 42, 22))
        self.spinBox_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(240, 20, 131, 16))
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 20, 101, 16))
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 60, 101, 16))
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_18 = QSpinBox(self.groupBox_3)
        self.spinBox_18.setObjectName(u"spinBox_18")
        self.spinBox_18.setGeometry(QRect(140, 140, 42, 22))
        self.spinBox_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(240, 60, 141, 16))
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_19 = QSpinBox(self.groupBox_3)
        self.spinBox_19.setObjectName(u"spinBox_19")
        self.spinBox_19.setGeometry(QRect(140, 60, 42, 22))
        self.spinBox_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(240, 140, 31, 16))
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_20 = QSpinBox(self.groupBox_3)
        self.spinBox_20.setObjectName(u"spinBox_20")
        self.spinBox_20.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_21 = QSpinBox(self.groupBox_3)
        self.spinBox_21.setObjectName(u"spinBox_21")
        self.spinBox_21.setGeometry(QRect(140, 100, 42, 22))
        self.spinBox_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(230, 100, 41, 20))
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_22 = QSpinBox(self.groupBox_3)
        self.spinBox_22.setObjectName(u"spinBox_22")
        self.spinBox_22.setGeometry(QRect(390, 60, 42, 22))
        self.spinBox_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 140, 111, 16))
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_23 = QSpinBox(self.groupBox_3)
        self.spinBox_23.setObjectName(u"spinBox_23")
        self.spinBox_23.setGeometry(QRect(290, 100, 42, 22))
        self.spinBox_24 = QSpinBox(self.groupBox_3)
        self.spinBox_24.setObjectName(u"spinBox_24")
        self.spinBox_24.setGeometry(QRect(290, 140, 42, 22))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 110, 61, 16))
        self.spinBox_5 = QSpinBox(self.groupBox_3)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(430, 110, 42, 22))
        self.graphicsView_3 = QGraphicsView(self.page_3)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(0, 200, 661, 231))
        self.pushButton_5 = QPushButton(self.page_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(720, 50, 151, 41))
        self.pushButton_5.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(720, 120, 151, 41))
        self.pushButton_6.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_27 = QLabel(self.page_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(420, 0, 71, 16))
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.groupBox_4 = QGroupBox(self.page_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 20, 521, 171))
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 100, 121, 16))
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_25 = QSpinBox(self.groupBox_4)
        self.spinBox_25.setObjectName(u"spinBox_25")
        self.spinBox_25.setGeometry(QRect(390, 20, 42, 22))
        self.spinBox_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(240, 20, 131, 16))
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.groupBox_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 20, 101, 16))
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 60, 101, 16))
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_26 = QSpinBox(self.groupBox_4)
        self.spinBox_26.setObjectName(u"spinBox_26")
        self.spinBox_26.setGeometry(QRect(140, 140, 42, 22))
        self.spinBox_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(240, 60, 141, 16))
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_27 = QSpinBox(self.groupBox_4)
        self.spinBox_27.setObjectName(u"spinBox_27")
        self.spinBox_27.setGeometry(QRect(140, 60, 42, 22))
        self.spinBox_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(210, 140, 61, 20))
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_28 = QSpinBox(self.groupBox_4)
        self.spinBox_28.setObjectName(u"spinBox_28")
        self.spinBox_28.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_29 = QSpinBox(self.groupBox_4)
        self.spinBox_29.setObjectName(u"spinBox_29")
        self.spinBox_29.setGeometry(QRect(140, 100, 42, 22))
        self.spinBox_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(240, 100, 31, 16))
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_30 = QSpinBox(self.groupBox_4)
        self.spinBox_30.setObjectName(u"spinBox_30")
        self.spinBox_30.setGeometry(QRect(390, 60, 42, 22))
        self.spinBox_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(20, 140, 111, 16))
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_31 = QSpinBox(self.groupBox_4)
        self.spinBox_31.setObjectName(u"spinBox_31")
        self.spinBox_31.setGeometry(QRect(290, 100, 42, 22))
        self.spinBox_32 = QSpinBox(self.groupBox_4)
        self.spinBox_32.setObjectName(u"spinBox_32")
        self.spinBox_32.setGeometry(QRect(290, 140, 42, 22))
        self.graphicsView_4 = PlotWidget(self.page_4)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(0, 200, 671, 231))
        self.pushButton_7 = QPushButton(self.page_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(710, 120, 151, 41))
        self.pushButton_7.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8 = QPushButton(self.page_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(710, 50, 151, 41))
        self.pushButton_8.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_36 = QLabel(self.page_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(410, 0, 71, 16))
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.graphicsView_5 = QGraphicsView(self.page_5)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(0, 201, 721, 231))
        self.groupBox_5 = QGroupBox(self.page_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 20, 521, 171))
        self.groupBox_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_37 = QLabel(self.groupBox_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 100, 121, 16))
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_AA = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_AA.setObjectName(u"spinBox_AOOR_AA")
        self.spinBox_AOOR_AA.setGeometry(QRect(350, 20, 42, 22))
        self.spinBox_AOOR_AA.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_38 = QLabel(self.groupBox_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(250, 20, 91, 16))
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_39 = QLabel(self.groupBox_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 20, 101, 16))
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_40 = QLabel(self.groupBox_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(20, 60, 101, 16))
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_AT = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_AT.setObjectName(u"spinBox_AOOR_AT")
        self.spinBox_AOOR_AT.setGeometry(QRect(140, 140, 42, 22))
        self.spinBox_AOOR_AT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_41 = QLabel(self.groupBox_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(240, 60, 141, 16))
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_URL = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_URL.setObjectName(u"spinBox_AOOR_URL")
        self.spinBox_AOOR_URL.setGeometry(QRect(140, 60, 42, 22))
        self.spinBox_AOOR_URL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_42 = QLabel(self.groupBox_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(190, 140, 91, 20))
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_LRL = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_LRL.setObjectName(u"spinBox_AOOR_LRL")
        self.spinBox_AOOR_LRL.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_AOOR_LRL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_MSR = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_MSR.setObjectName(u"spinBox_AOOR_MSR")
        self.spinBox_AOOR_MSR.setGeometry(QRect(140, 100, 42, 22))
        self.spinBox_AOOR_MSR.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_43 = QLabel(self.groupBox_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(190, 100, 81, 20))
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_APW = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_APW.setObjectName(u"spinBox_AOOR_APW")
        self.spinBox_AOOR_APW.setGeometry(QRect(350, 60, 42, 22))
        self.spinBox_AOOR_APW.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_44 = QLabel(self.groupBox_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 140, 111, 16))
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AOOR_REACT_T = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_REACT_T.setObjectName(u"spinBox_AOOR_REACT_T")
        self.spinBox_AOOR_REACT_T.setGeometry(QRect(290, 100, 42, 22))
        self.spinBox_AOOR_RF = QSpinBox(self.groupBox_5)
        self.spinBox_AOOR_RF.setObjectName(u"spinBox_AOOR_RF")
        self.spinBox_AOOR_RF.setGeometry(QRect(290, 140, 42, 22))
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 100, 81, 20))
        self.spinBox_Rec_T = QSpinBox(self.groupBox_5)
        self.spinBox_Rec_T.setObjectName(u"spinBox_Rec_T")
        self.spinBox_Rec_T.setGeometry(QRect(440, 100, 42, 22))
        self.label_45 = QLabel(self.page_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(410, 0, 71, 16))
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.pushButton_9 = QPushButton(self.page_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(710, 120, 151, 41))
        self.pushButton_9.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10 = QPushButton(self.page_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(710, 50, 151, 41))
        self.pushButton_10.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.groupBox_6 = QGroupBox(self.page_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(0, 20, 521, 171))
        self.groupBox_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_46 = QLabel(self.groupBox_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 100, 121, 16))
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_VA = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_VA.setObjectName(u"spinBox_VOOR_VA")
        self.spinBox_VOOR_VA.setGeometry(QRect(390, 20, 42, 22))
        self.spinBox_VOOR_VA.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_47 = QLabel(self.groupBox_6)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(240, 20, 131, 16))
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_48 = QLabel(self.groupBox_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 20, 101, 16))
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_49 = QLabel(self.groupBox_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(20, 60, 101, 16))
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_MSR = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_MSR.setObjectName(u"spinBox_VOOR_MSR")
        self.spinBox_VOOR_MSR.setGeometry(QRect(140, 140, 42, 22))
        self.spinBox_VOOR_MSR.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_50 = QLabel(self.groupBox_6)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(240, 60, 141, 16))
        self.label_50.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_URL = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_URL.setObjectName(u"spinBox_VOOR_URL")
        self.spinBox_VOOR_URL.setGeometry(QRect(140, 60, 42, 22))
        self.spinBox_VOOR_URL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_51 = QLabel(self.groupBox_6)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(190, 140, 91, 20))
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_LRL = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_LRL.setObjectName(u"spinBox_VOOR_LRL")
        self.spinBox_VOOR_LRL.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_VOOR_LRL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_AT = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_AT.setObjectName(u"spinBox_VOOR_AT")
        self.spinBox_VOOR_AT.setGeometry(QRect(140, 100, 42, 22))
        self.spinBox_VOOR_AT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_52 = QLabel(self.groupBox_6)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(190, 100, 81, 20))
        self.label_52.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_VPW = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_VPW.setObjectName(u"spinBox_VOOR_VPW")
        self.spinBox_VOOR_VPW.setGeometry(QRect(390, 60, 42, 22))
        self.spinBox_VOOR_VPW.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_53 = QLabel(self.groupBox_6)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 140, 121, 20))
        self.label_53.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VOOR_React_T = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_React_T.setObjectName(u"spinBox_VOOR_React_T")
        self.spinBox_VOOR_React_T.setGeometry(QRect(290, 100, 42, 22))
        self.spinBox_VOOR_RF = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_RF.setObjectName(u"spinBox_VOOR_RF")
        self.spinBox_VOOR_RF.setGeometry(QRect(290, 140, 42, 22))
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(350, 100, 81, 20))
        self.spinBox_VOOR_Rec_T = QSpinBox(self.groupBox_6)
        self.spinBox_VOOR_Rec_T.setObjectName(u"spinBox_VOOR_Rec_T")
        self.spinBox_VOOR_Rec_T.setGeometry(QRect(440, 100, 42, 22))
        self.graphicsView_6 = QGraphicsView(self.page_6)
        self.graphicsView_6.setObjectName(u"graphicsView_6")
        self.graphicsView_6.setGeometry(QRect(0, 200, 721, 231))
        self.pushButton_11 = QPushButton(self.page_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(710, 50, 151, 41))
        self.pushButton_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12 = QPushButton(self.page_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(710, 120, 151, 41))
        self.pushButton_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_62 = QLabel(self.page_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(410, 0, 71, 16))
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_62.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.pushButton_13 = QPushButton(self.page_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(710, 120, 151, 41))
        self.pushButton_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.graphicsView_7 = QGraphicsView(self.page_7)
        self.graphicsView_7.setObjectName(u"graphicsView_7")
        self.graphicsView_7.setGeometry(QRect(0, 200, 721, 231))
        self.pushButton_14 = QPushButton(self.page_7)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(710, 50, 151, 41))
        self.pushButton_14.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox_7 = QGroupBox(self.page_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(0, 20, 701, 171))
        self.groupBox_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_63 = QLabel(self.groupBox_7)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(10, 100, 121, 16))
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_AA = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_AA.setObjectName(u"spinBox_AAIR_AA")
        self.spinBox_AAIR_AA.setGeometry(QRect(390, 20, 42, 22))
        self.spinBox_AAIR_AA.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_64 = QLabel(self.groupBox_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(240, 20, 131, 16))
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_65 = QLabel(self.groupBox_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(20, 20, 101, 16))
        self.label_65.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_66 = QLabel(self.groupBox_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(20, 60, 101, 16))
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_AS = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_AS.setObjectName(u"spinBox_AAIR_AS")
        self.spinBox_AAIR_AS.setGeometry(QRect(140, 140, 42, 22))
        self.spinBox_AAIR_AS.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_67 = QLabel(self.groupBox_7)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(240, 60, 141, 16))
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_URL = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_URL.setObjectName(u"spinBox_AAIR_URL")
        self.spinBox_AAIR_URL.setGeometry(QRect(140, 60, 42, 22))
        self.spinBox_AAIR_URL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_68 = QLabel(self.groupBox_7)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(230, 140, 41, 20))
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_LRL = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_LRL.setObjectName(u"spinBox_AAIR_LRL")
        self.spinBox_AAIR_LRL.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_AAIR_LRL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_MSR = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_MSR.setObjectName(u"spinBox_AAIR_MSR")
        self.spinBox_AAIR_MSR.setGeometry(QRect(140, 100, 42, 22))
        self.spinBox_AAIR_MSR.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_69 = QLabel(self.groupBox_7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(240, 100, 31, 16))
        self.label_69.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_APW = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_APW.setObjectName(u"spinBox_AAIR_APW")
        self.spinBox_AAIR_APW.setGeometry(QRect(390, 60, 42, 22))
        self.spinBox_AAIR_APW.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_70 = QLabel(self.groupBox_7)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(20, 140, 111, 16))
        self.label_70.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_ARP = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_ARP.setObjectName(u"spinBox_AAIR_ARP")
        self.spinBox_AAIR_ARP.setGeometry(QRect(290, 100, 42, 22))
        self.spinBox_AAIR_PVARP = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_PVARP.setObjectName(u"spinBox_AAIR_PVARP")
        self.spinBox_AAIR_PVARP.setGeometry(QRect(290, 140, 42, 22))
        self.spinBox_AAIR_H = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_H.setObjectName(u"spinBox_AAIR_H")
        self.spinBox_AAIR_H.setGeometry(QRect(430, 140, 42, 22))
        self.label_81 = QLabel(self.groupBox_7)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(350, 100, 111, 16))
        self.label_81.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_RS = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_RS.setObjectName(u"spinBox_AAIR_RS")
        self.spinBox_AAIR_RS.setGeometry(QRect(450, 100, 42, 22))
        self.spinBox_AAIR_RS.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_82 = QLabel(self.groupBox_7)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(360, 140, 61, 20))
        self.label_82.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(510, 100, 81, 20))
        self.label_83 = QLabel(self.groupBox_7)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(480, 140, 91, 20))
        self.label_83.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_React_T = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_React_T.setObjectName(u"spinBox_AAIR_React_T")
        self.spinBox_AAIR_React_T.setGeometry(QRect(560, 60, 42, 22))
        self.label_84 = QLabel(self.groupBox_7)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(460, 60, 81, 20))
        self.label_84.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_Res_F = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_Res_F.setObjectName(u"spinBox_AAIR_Res_F")
        self.spinBox_AAIR_Res_F.setGeometry(QRect(570, 140, 42, 22))
        self.spinBox_AAIR_AT = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_AT.setObjectName(u"spinBox_AAIR_AT")
        self.spinBox_AAIR_AT.setGeometry(QRect(570, 20, 42, 22))
        self.spinBox_AAIR_AT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_85 = QLabel(self.groupBox_7)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(450, 20, 121, 16))
        self.label_85.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_AAIR_Rec_T = QSpinBox(self.groupBox_7)
        self.spinBox_AAIR_Rec_T.setObjectName(u"spinBox_AAIR_Rec_T")
        self.spinBox_AAIR_Rec_T.setGeometry(QRect(600, 100, 42, 22))
        self.label_71 = QLabel(self.page_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(420, 0, 71, 16))
        self.label_71.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_71.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.pushButton_15 = QPushButton(self.page_8)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(710, 50, 151, 41))
        self.pushButton_15.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16 = QPushButton(self.page_8)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(710, 120, 151, 41))
        self.pushButton_16.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.graphicsView_8 = QGraphicsView(self.page_8)
        self.graphicsView_8.setObjectName(u"graphicsView_8")
        self.graphicsView_8.setGeometry(QRect(0, 200, 721, 231))
        self.groupBox_8 = QGroupBox(self.page_8)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(0, 20, 701, 171))
        self.groupBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_72 = QLabel(self.groupBox_8)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(10, 100, 121, 16))
        self.label_72.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_VA = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_VA.setObjectName(u"spinBox_VVIR_VA")
        self.spinBox_VVIR_VA.setGeometry(QRect(390, 20, 42, 22))
        self.spinBox_VVIR_VA.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_73 = QLabel(self.groupBox_8)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(240, 20, 131, 16))
        self.label_73.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_74 = QLabel(self.groupBox_8)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(20, 20, 101, 16))
        self.label_74.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_75 = QLabel(self.groupBox_8)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(20, 60, 101, 16))
        self.label_75.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_VS = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_VS.setObjectName(u"spinBox_VVIR_VS")
        self.spinBox_VVIR_VS.setGeometry(QRect(140, 140, 42, 22))
        self.spinBox_VVIR_VS.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_76 = QLabel(self.groupBox_8)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(240, 60, 141, 16))
        self.label_76.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_URL = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_URL.setObjectName(u"spinBox_VVIR_URL")
        self.spinBox_VVIR_URL.setGeometry(QRect(140, 60, 42, 22))
        self.spinBox_VVIR_URL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_77 = QLabel(self.groupBox_8)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(210, 140, 61, 20))
        self.label_77.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_LRL = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_LRL.setObjectName(u"spinBox_VVIR_LRL")
        self.spinBox_VVIR_LRL.setGeometry(QRect(140, 20, 42, 22))
        self.spinBox_VVIR_LRL.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_MSR = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_MSR.setObjectName(u"spinBox_VVIR_MSR")
        self.spinBox_VVIR_MSR.setGeometry(QRect(140, 100, 42, 22))
        self.spinBox_VVIR_MSR.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_78 = QLabel(self.groupBox_8)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(240, 100, 31, 16))
        self.label_78.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_VPW = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_VPW.setObjectName(u"spinBox_VVIR_VPW")
        self.spinBox_VVIR_VPW.setGeometry(QRect(390, 60, 42, 22))
        self.spinBox_VVIR_VPW.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_79 = QLabel(self.groupBox_8)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(10, 140, 121, 20))
        self.label_79.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_VRP = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_VRP.setObjectName(u"spinBox_VVIR_VRP")
        self.spinBox_VVIR_VRP.setGeometry(QRect(290, 100, 42, 22))
        self.spinBox_VVIR_H = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_H.setObjectName(u"spinBox_VVIR_H")
        self.spinBox_VVIR_H.setGeometry(QRect(290, 140, 42, 22))
        self.spinBox_VVIR_RS = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_RS.setObjectName(u"spinBox_VVIR_RS")
        self.spinBox_VVIR_RS.setGeometry(QRect(440, 100, 42, 22))
        self.spinBox_VVIR_RS.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_86 = QLabel(self.groupBox_8)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(340, 100, 91, 16))
        self.label_86.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_Reac_T = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_Reac_T.setObjectName(u"spinBox_VVIR_Reac_T")
        self.spinBox_VVIR_Reac_T.setGeometry(QRect(570, 60, 42, 22))
        self.spinBox_VVIR_Rec_T = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_Rec_T.setObjectName(u"spinBox_VVIR_Rec_T")
        self.spinBox_VVIR_Rec_T.setGeometry(QRect(610, 100, 42, 22))
        self.label_157 = QLabel(self.groupBox_8)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(460, 20, 121, 16))
        self.label_157.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_158 = QLabel(self.groupBox_8)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setGeometry(QRect(470, 60, 81, 20))
        self.label_158.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_159 = QLabel(self.groupBox_8)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(360, 140, 91, 20))
        self.label_159.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_AT = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_AT.setObjectName(u"spinBox_VVIR_AT")
        self.spinBox_VVIR_AT.setGeometry(QRect(580, 20, 42, 22))
        self.spinBox_VVIR_AT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_VVIR_Res_F = QSpinBox(self.groupBox_8)
        self.spinBox_VVIR_Res_F.setObjectName(u"spinBox_VVIR_Res_F")
        self.spinBox_VVIR_Res_F.setGeometry(QRect(460, 140, 42, 22))
        self.label_160 = QLabel(self.groupBox_8)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(510, 100, 81, 20))
        self.label_80 = QLabel(self.page_8)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(420, 0, 71, 16))
        self.label_80.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_80.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_8)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        self.saveButton = QPushButton(self.frame_top)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(825, 5, 80, 30))
        self.saveButton.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);""background-color: rgb(85, 170, 255);")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)

        # self.pushButton.clicked.connect(lambda: self.draw())
        # self.pushButton_2.clicked.connect(lambda: self.clear())
    # setupUi

    #GETTERS
    def get_saveButton(self):
        return self.saveButton

    def get_createGraph_AOO(self):
        return self.pushButton

    def get_createGraph_VOO(self):
        return self.pushButton_3

    def get_createGraph_AAI(self):
        return self.pushButton_5

    def get_createGraph_VVI(self):
        return self.pushButton_8

    def get_createGraph_AOOR(self):
        return self.pushButton_10

    def get_createGraph_VOOR(self):
        return self.pushButton_11

    def get_createGraph_AAIR(self):
        return self.pushButton_14

    def get_createGraph_VVIR(self):
        return self.pushButton_15

    def get_AOO_LRL(self):
        return self.spinBox #AOO: Lower Rate Limit

    def get_AOO_URL(self):
        return self.spinBox_2 #AOO: Upper Rate Limit

    def get_AOO_AA(self):
        return self.spinBox_3 #AOO: Atrial Amplitude

    def get_AOO_APW(self):
        return self.spinBox_4 #AOO: Atrial Pulse Width

    def get_VOO_LRL(self):
        return self.spinBox_9 #VOO: Lower Rate Limit

    def get_VOO_URL(self):
        return self.spinBox_10 #VOO: Upper Rate Limit

    def get_VOO_VA(self):
        return self.spinBox_13 #VOO: Ventricular Amplitude

    def get_VOO_VPW(self):
        return self.spinBox_14 #VOO: Ventricular Pulse Width

    def get_AAI_LRL(self):
        return self.spinBox_20 #AAI: Lower Rate Limit

    def get_AAI_URL(self):
        return self.spinBox_19 #AAI: Upper Rate Limit

    def get_AAI_AA(self):
        return self.spinBox_21 #AAI: Atrial Amplitude

    def get_AAI_APW(self):
        return self.spinBox_18 #AAI: Atrial Pulse Width

    def get_AAI_AS(self):
        return self.spinBox_17 #AAI: Atrial Sensitivity

    def get_AAI_RS(self):
        return self.spinBox_22 #AAI: Rate Smoothing

    def get_AAI_PVARP(self):
        return self.spinBox_23 #AAI: PVARP

    def get_AAI_ARP(self):
        return self.spinBox_24 #AAI: ARP

    def get_AAI_H(self):
        return self.spinBox_5 #AAI: Hysteresis

    def get_VVI_LRL(self):
        return self.spinBox_28 #VVI: Lower Rate Limit

    def get_VVI_URL(self):
        return self.spinBox_27 #VVI: Upper Rate Limit

    def get_VVI_VS(self):
        return self.spinBox_29 #VVI: Ventricular Sensitivity

    def get_VVI_RS(self):
        return self.spinBox_26 #VVI: Rate Smoothing

    def get_VVI_VA(self):
        return self.spinBox_25 #VVI: Ventricular Amplitude

    def get_VVI_VPW(self):
        return self.spinBox_30 #VVI: Ventricular Pulse Width

    def get_VVI_VRP(self):
        return self.spinBox_31 #VVI: VRP

    def get_VVI_H(self):
        return self.spinBox_32 #VVI: Hysteresis

    def get_AOOR_LRL(self):
        return self.spinBox_AOOR_LRL #AOOR: Lower Rate Limit

    def get_AOOR_URL(self):
        return self.spinBox_AOOR_URL #AOOR: Upper Rate Limit

    def get_AOOR_MSR(self):
        return self.spinBox_AOOR_MSR #AOOR: Maximum Sensor Rate

    def get_AOOR_AT(self):
        return self.spinBox_AOOR_AT #AOOR: Activity Threshold

    def get_AOOR_AA(self):
        return self.spinBox_AOOR_AA #AOOR: Atrial Amplitude

    def get_AOOR_APW(self):
        return self.spinBox_AOOR_APW #AOOR: Atrial Pulse Width

    def get_AOOR_ReactT(self):
        return self.spinBox_AOOR_REACT_T #AOOR: Reaction Time

    def get_AOOR_RF(self):
        return self.spinBox_AOOR_RF #AOOR: Response Factor

    def get_AOOR_RecT(self):
        return self.spinBox_Rec_T #AOOR: Recovery Time

    def get_VOOR_LRL(self):
        return self.spinBox_VOOR_LRL #VOOR: Lower Rate Limit

    def get_VOOR_URL(self):
        return self.spinBox_VOOR_URL #VOOR: Upper Rate Limit

    def get_VOOR_AT(self):
        return self.spinBox_VOOR_AT #VOOR: Activity Threshold

    def get_VOOR_MSR(self):
        return self.spinBox_VOOR_MSR #VOOR: Maximum Sensor Rate

    def get_VOOR_VA(self):
        return self.spinBox_VOOR_VA #VOOR: Ventricular Amplitude

    def get_VOOR_VPW(self):
        return self.spinBox_VOOR_VPW #VOOR: Ventricular Pulse Width

    def get_VOOR_ReactT(self):
        return self.spinBox_VOOR_React_T #VOOR: Reaction Time

    def get_VOOR_RF(self):
        return self.spinBox_VOOR_RF #VOOR: Response Factor

    def get_VOOR_RecT(self):
        return self.spinBox_VOOR_Rec_T #VOOR: Recovery Time

    def get_AAIR_LRL(self):
        return self.spinBox_AAIR_LRL #AAIR: Lower Rate Limit

    def get_AAIR_URL(self):
        return self.spinBox_AAIR_URL #AAIR: Upper Rate Limit

    def get_AAIR_MSR(self):
        return self.spinBox_AAIR_MSR #AAIR: Maximum Sensor Rate

    def get_AAIR_AS(self):
        return self.spinBox_AAIR_AS #AAIR: Atrial Sensitivity

    def get_AAIR_AA(self):
        return self.spinBox_AAIR_AA #AAIR: Atrial Amplitude

    def get_AAIR_APW(self):
        return self.spinBox_AAIR_APW #AAIR: Atrial Pulse Width

    def get_AAIR_ARP(self):
        return self.spinBox_AAIR_ARP #AAIR: ARP

    def get_AAIR_PVARP(self):
        return self.spinBox_AAIR_PVARP #AAIR: PVARP

    def get_AAIR_AT(self):
        return self.spinBox_AAIR_AT #AAIR: Activity Threshold

    def get_AAIR_ReactT(self):
        return self.spinBox_AAIR_React_T #AAIR: Reaction Time

    def get_AAIR_RS(self):
        return self.spinBox_AAIR_RS #AAIR: Rate Smoothing

    def get_AAIR_H(self):
        return self.spinBox_AAIR_H #AAIR: Hysteresis

    def get_AAIR_RecT(self):
        return self.spinBox_AAIR_Rec_T #AAIR: Recovery Time

    def get_AAIR_RF(self):
        return self.spinBox_AAIR_Res_F #AAIR: Response Factor

    def get_VVIR_LRL(self):
            return self.spinBox_VVIR_LRL  # VVIR: Lower Rate Limit

    def get_VVIR_URL(self):
            return self.spinBox_VVIR_URL  # VVIR: Upper Rate Limit

    def get_VVIR_MSR(self):
            return self.spinBox_VVIR_MSR  # VVIR: Maximum Sensor Rate

    def get_VVIR_VS(self):
            return self.spinBox_VVIR_VS  # VVIR: Ventricular Sensitivity

    def get_VVIR_VA(self):
            return self.spinBox_VVIR_VA  # VVIR: Ventricular Amplitude

    def get_VVIR_VPW(self):
            return self.spinBox_VVIR_VPW  # VVIR: Ventricular Pulse Width

    def get_VVIR_VRP(self):
            return self.spinBox_VVIR_VRP  # VVIR: VRP

    def get_VVIR_H(self):
            return self.spinBox_VVIR_H  # VVIR: Hysteresis

    def get_VVIR_AT(self):
            return self.spinBox_VVIR_AT  # VVIR: Activity Threshold

    def get_VVIR_ReactT(self):
            return self.spinBox_VVIR_Reac_T  # VVIR: Reaction Time

    def get_VVIR_RS(self):
            return self.spinBox_VVIR_RS  # VVIR: Rate Smoothing

    def get_VVIR_RF(self):
            return self.spinBox_VVIR_Res_F  # VVIR: Response Factor

    def get_VVIR_RecT(self):
            return self.spinBox_VVIR_Rec_T  # VVIR: Recovery Time



    #SETTERS
    def set_AOO_LRL(self, value):
        self.spinBox.setValue(value)  #AOO: Lower Rate Limit

    def set_AOO_URL(self, value):
        self.spinBox_2.setValue(value) #AOO: Upper Rate Limit

    def set_AOO_AA(self, value):
        self.spinBox_3.setValue(value) #AOO: Atrial Amplitude

    def set_AOO_APW(self, value):
        self.spinBox_4.setValue(value) #AOO: Atrial Pulse Width

    def set_VOO_LRL(self, value):
        self.spinBox_9.setValue(value) #VOO: Lower Rate Limit

    def set_VOO_URL(self, value):
        self.spinBox_10.setValue(value) #VOO: Upper Rate Limit

    def set_VOO_VA(self, value):
        self.spinBox_13.setValue(value) #VOO: Ventricular Amplitude

    def set_VOO_VPW(self, value):
        self.spinBox_14.setValue(value) #VOO: Ventricular Pulse Width

    def set_AAI_LRL(self, value):
        self.spinBox_20.setValue(value) #AAI: Lower Rate Limit

    def set_AAI_URL(self, value):
        self.spinBox_19.setValue(value) #AAI: Upper Rate Limit

    def set_AAI_AA(self, value):
        self.spinBox_21.setValue(value) #AAI: Atrial Amplitude

    def set_AAI_APW(self, value):
        self.spinBox_18.setValue(value) #AAI: Atrial Pulse Width

    def set_AAI_AS(self, value):
        self.spinBox_17.setValue(value) #AAI: Atrial Sensitivity

    def set_AAI_RS(self, value):
        self.spinBox_22.setValue(value) #AAI: Rate Smoothing

    def set_AAI_PVARP(self, value):
        self.spinBox_23.setValue(value) #AAI: PVARP

    def set_AAI_ARP(self, value):
        self.spinBox_24.setValue(value) #AAI: ARP

    def set_AAI_H(self, value):
        self.spinBox_5.setValue(value) #AAI: Hysteresis

    def set_VVI_LRL(self, value):
        self.spinBox_28.setValue(value) #VVI: Lower Rate Limit

    def set_VVI_URL(self, value):
        self.spinBox_27.setValue(value) #VVI: Upper Rate Limit

    def set_VVI_VS(self, value):
        self.spinBox_29.setValue(value) #VVI: Ventricular Sensitivity

    def set_VVI_RS(self, value):
        self.spinBox_26.setValue(value) #VVI: Rate Smoothing

    def set_VVI_VA(self, value):
        self.spinBox_25.setValue(value) #VVI: Ventricular Amplitude

    def set_VVI_VPW(self, value):
        self.spinBox_30.setValue(value) #VVI: Ventricular Pulse Width

    def set_VVI_VRP(self, value):
        self.spinBox_31.setValue(value) #VVI: VRP

    def set_VVI_H(self, value):
        self.spinBox_32.setValue(value) #VVI: Hysteresis

    def set_AOOR_LRL(self, value):
        self.spinBox_AOOR_LRL.setValue(value) #AOOR: Lower Rate Limit

    def set_AOOR_URL(self, value):
        self.spinBox_AOOR_URL.setValue(value) #AOOR: Upper Rate Limit

    def set_AOOR_MSR(self, value):
        self.spinBox_AOOR_MSR.setValue(value) #AOOR: Maximum Sensor Rate

    def set_AOOR_AT(self, value):
        self.spinBox_AOOR_AT.setValue(value) #AOOR: Activity Threshold

    def set_AOOR_AA(self, value):
        self.spinBox_AOOR_AA.setValue(value) #AOOR: Atrial Amplitude

    def set_AOOR_APW(self, value):
        self.spinBox_AOOR_APW.setValue(value) #AOOR: Atrial Pulse Width

    def set_AOOR_ReactT(self, value):
        self.spinBox_AOOR_REACT_T.setValue(value) #AOOR: Reaction Time

    def set_AOOR_RF(self, value):
        self.spinBox_AOOR_RF.setValue(value) #AOOR: Response Factor

    def set_AOOR_RecT(self, value):
        self.spinBox_Rec_T.setValue(value) #AOOR: Recovery Time

    def set_VOOR_LRL(self, value):
        self.spinBox_VOOR_LRL.setValue(value) #VOOR: Lower Rate Limit

    def set_VOOR_URL(self, value):
        self.spinBox_VOOR_URL.setValue(value) #VOOR: Upper Rate Limit

    def set_VOOR_AT(self, value):
        self.spinBox_VOOR_AT.setValue(value) #VOOR: Activity Threshold

    def set_VOOR_MSR(self, value):
        self.spinBox_VOOR_MSR.setValue(value) #VOOR: Maximum Sensor Rate

    def set_VOOR_VA(self, value):
        self.spinBox_VOOR_VA.setValue(value) #VOOR: Ventricular Amplitude

    def set_VOOR_VPW(self, value):
        self.spinBox_VOOR_VPW.setValue(value) #VOOR: Ventricular Pulse Width

    def set_VOOR_ReactT(self, value):
        self.spinBox_VOOR_React_T.setValue(value) #VOOR: Reaction Time

    def set_VOOR_RF(self, value):
        self.spinBox_VOOR_RF.setValue(value) #VOOR: Response Factor

    def set_VOOR_RecT(self, value):
        self.spinBox_VOOR_Rec_T.setValue(value) #VOOR: Recovery Time

    def set_AAIR_LRL(self, value):
        self.spinBox_AAIR_LRL.setValue(value) #AAIR: Lower Rate Limit

    def set_AAIR_URL(self, value):
        self.spinBox_AAIR_URL.setValue(value) #AAIR: Upper Rate Limit

    def set_AAIR_MSR(self, value):
        self.spinBox_AAIR_MSR.setValue(value) #AAIR: Maximum Sensor Rate

    def set_AAIR_AS(self, value):
        self.spinBox_AAIR_AS.setValue(value) #AAIR: Atrial Sensitivity

    def set_AAIR_AA(self, value):
        self.spinBox_AAIR_AA.setValue(value) #AAIR: Atrial Amplitude

    def set_AAIR_APW(self, value):
        self.spinBox_AAIR_APW.setValue(value) #AAIR: Atrial Pulse Width

    def set_AAIR_ARP(self, value):
        self.spinBox_AAIR_ARP.setValue(value) #AAIR: ARP

    def set_AAIR_PVARP(self, value):
        self.spinBox_AAIR_PVARP.setValue(value) #AAIR: PVARP

    def set_AAIR_AT(self, value):
        self.spinBox_AAIR_AT.setValue(value) #AAIR: Activity Threshold

    def set_AAIR_ReactT(self, value):
        self.spinBox_AAIR_React_T.setValue(value) #AAIR: Reaction Time

    def set_AAIR_RS(self, value):
        self.spinBox_AAIR_RS.setValue(value) #AAIR: Rate Smoothing

    def set_AAIR_H(self, value):
        self.spinBox_AAIR_H.setValue(value) #AAIR: Hysteresis

    def set_AAIR_RecT(self, value):
        self.spinBox_AAIR_Rec_T.setValue(value) #AAIR: Recovery Time

    def set_AAIR_RF(self, value):
        self.spinBox_AAIR_Res_F.setValue(value) #AAIR: Response Factor

    def set_VVIR_LRL(self, value):
            self.spinBox_VVIR_LRL.setValue(value)  # VVIR: Lower Rate Limit

    def set_VVIR_URL(self, value):
            self.spinBox_VVIR_URL.setValue(value)  # VVIR: Upper Rate Limit

    def set_VVIR_MSR(self, value):
            self.spinBox_VVIR_MSR.setValue(value)  # VVIR: Maximum Sensor Rate

    def set_VVIR_VS(self, value):
            self.spinBox_VVIR_VS.setValue(value)  # VVIR: Ventricular Sensitivity

    def set_VVIR_VA(self, value):
            self.spinBox_VVIR_VA.setValue(value)  # VVIR: Ventricular Amplitude

    def set_VVIR_VPW(self, value):
            self.spinBox_VVIR_VPW.setValue(value)  # VVIR: Ventricular Pulse Width

    def set_VVIR_VRP(self, value):
            self.spinBox_VVIR_VRP.setValue(value)  # VVIR: VRP

    def set_VVIR_H(self, value):
            self.spinBox_VVIR_H.setValue(value)  # VVIR: Hysteresis

    def set_VVIR_AT(self, value):
            self.spinBox_VVIR_AT.setValue(value)  # VVIR: Activity Threshold

    def set_VVIR_ReactT(self, value):
            self.spinBox_VVIR_Reac_T.setValue(value)  # VVIR: Reaction Time

    def set_VVIR_RS(self, value):
            self.spinBox_VVIR_RS.setValue(value)  # VVIR: Rate Smoothing

    def set_VVIR_RF(self, value):
            self.spinBox_VVIR_Res_F.setValue(value)  # VVIR: Response Factor

    def set_VVIR_RecT(self, value):
            self.spinBox_VVIR_Rec_T.setValue(value)  # VVIR: Recovery Time

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"AOO", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"VOO", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"AAI", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"VVI", None))
        self.btn_page_5.setText(QCoreApplication.translate("MainWindow", u"AOOR", None))
        self.btn_page_6.setText(QCoreApplication.translate("MainWindow", u"VOOR", None))
        self.btn_page_7.setText(QCoreApplication.translate("MainWindow", u"AAIR", None))
        self.btn_page_8.setText(QCoreApplication.translate("MainWindow", u"VVIR", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Atrial Amplitude", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Atrial Pulse Width", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"AOO", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ventricular Amplitude", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ventricular Pulse Width", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"VOO", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Atrial Amplitude", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Atrial Sensitivity", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Rate Smoothing", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ARP", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"PVARP", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Atrial Pulse Width", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hysteresis", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"AAI", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ventricular Sensitivity", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Ventricular Amplitude", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Ventricular Pulse Width", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Hysteresis", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"VRP", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Rate Smoothing", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"VVI", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Maximum Sensor Rate", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Atrial Amplitude", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Atrial Pulse Width", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Response Factor", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Reaction Time ", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Activity Threshold ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Recovery Time ", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"AOOR", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Activity Threshold", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ventricular Amplitude", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Ventricular Pulse Width", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Response Factor", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Reaction Time", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Maximum Sensor Rate", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Recovery Time ", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"VOOR", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Maximum Sensor Rate", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Atrial Amplitude", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Atrial Pulse Width", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"PVARP", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"ARP", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Atrial Sensitivity", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Rate Smoothing", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Hysteresis", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Recovery Time ", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Response Factor", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Reaction Time", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Activity Threshold", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"AAIR", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Maximum Sensor Rate", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Ventricular Amplitude", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Lower Rate Limit", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Upper Rate Limit", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Ventricular Pulse Width", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Hysteresis", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"VRP", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Ventricular Sensitivity", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Rate Smoothing", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Activity Threshold", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Reaction Time", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Response Factor", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Recovery Time ", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"VVIR", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

    def draw(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=(3,1000))
        for i in range(3):
            self.graphicsView.plot(x,y[i],pen=(i,3))

    def clear(self):
        self.graphicsView.clear()

