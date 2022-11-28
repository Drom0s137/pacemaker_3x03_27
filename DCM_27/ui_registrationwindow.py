# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Registration(object):

    def __init__(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(640, 480)
        Registration.setAutoFillBackground(False)
        Registration.setStyleSheet(u"background-color:'lightgreen'")
        self.centralwidget = QWidget(Registration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.registration_label = QLabel(Registration)
        self.registration_label.setObjectName(u"registration_label")
        self.registration_label.setGeometry(QRect(230, 60, 171, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.registration_label.setFont(font)
        self.usernameInput = QLineEdit(Registration)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(260, 250, 171, 21))
        self.usernameInput.setAutoFillBackground(False)
        self.usernameInput.setStyleSheet(u"background-color:'white'")
        self.passwordInput = QLineEdit(Registration)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(260, 290, 171, 21))
        self.passwordInput.setStyleSheet(u"background-color:'white'")
        self.username_label = QLabel(Registration)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(190, 250, 61, 16))
        self.password_label = QLabel(Registration)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(190, 290, 61, 16))
        self.registrationMessage_label = QLabel(Registration)
        self.registrationMessage_label.setObjectName(u"registrationMessage_label")
        self.registrationMessage_label.setGeometry(QRect(150, 110, 351, 21))
        self.registrationMessage_label.setStyleSheet(u"color:'blue'")
        self.create_button = QPushButton(Registration)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(370, 330, 75, 24))
        self.create_button.setStyleSheet(u"color:'darkgreen'; background-color:'white'")
        self.label = QLabel(Registration)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 130, 291, 16))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:'red'")
        self.username_label_2 = QLabel(Registration)
        self.username_label_2.setObjectName(u"username_label_2")
        self.username_label_2.setGeometry(QRect(190, 170, 61, 20))
        self.lastnameInput = QLineEdit(Registration)
        self.lastnameInput.setObjectName(u"lastnameInput")
        self.lastnameInput.setGeometry(QRect(260, 210, 171, 21))
        self.lastnameInput.setStyleSheet(u"background-color:'white'")
        self.lastnameInput.setMaxLength(32773)
        self.lastnameInput.setCursorPosition(0)
        self.firstnameInput = QLineEdit(Registration)
        self.firstnameInput.setObjectName(u"firstnameInput")
        self.firstnameInput.setGeometry(QRect(260, 170, 171, 21))
        self.firstnameInput.setAutoFillBackground(False)
        self.firstnameInput.setStyleSheet(u"background-color:'white'")
        self.password_label_2 = QLabel(Registration)
        self.password_label_2.setObjectName(u"password_label_2")
        self.password_label_2.setGeometry(QRect(190, 210, 61, 16))
        self.backToLogin_button = QPushButton(Registration)
        self.backToLogin_button.setObjectName(u"backToLogin_button")
        self.backToLogin_button.setGeometry(QRect(230, 330, 81, 24))
        self.backToLogin_button.setStyleSheet(u"background-color:'white'")

        #Error Messages
        self.missingFirstName_msg = QLabel(self.centralwidget)
        self.missingFirstName_msg.setObjectName(u"missingFirstName_msg")
        self.missingFirstName_msg.setGeometry(QRect(260, 190, 200, 15))
        self.missingFirstName_msg.setStyleSheet(u"color:'red'")
        self.missingFirstName_msg.hide()

        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    def get_create_button(self):
        return self.create_button

    def get_backToLogin_button(self):
        return self.backToLogin_button

    def get_firstnameInput(self):
        return self.firstnameInput

    def get_lastnameInput(self):
        return self.lastnameInput

    def get_usernameInput(self):
        return self.usernameInput

    def get_passwordInput(self):
        return self.passwordInput
    # setupUi

    def get_missingFirstName_msg(self):
        return self.missingFirstName_msg

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Registration", None))
        self.registration_label.setText(QCoreApplication.translate("Registration", u"Registration", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("Registration", u"e.g. CoolGuy39", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Registration", u"e.g. Password", None))
        self.username_label.setText(QCoreApplication.translate("Registration", u"Username:", None))
        self.password_label.setText(QCoreApplication.translate("Registration", u"Password:", None))
        self.registrationMessage_label.setText(QCoreApplication.translate("Registration", u"Please fill out the following sections to create your new account ", None))
        self.create_button.setText(QCoreApplication.translate("Registration", u"Create", None))
        self.label.setText(QCoreApplication.translate("Registration", u"(Disclaimer: Maximum of 10 registered users allowed only!)", None))
        self.username_label_2.setText(QCoreApplication.translate("Registration", u"First Name:", None))
        self.lastnameInput.setText("")
        self.lastnameInput.setPlaceholderText(QCoreApplication.translate("Registration", u"e.g. Noori", None))
        self.firstnameInput.setText("")
        self.firstnameInput.setPlaceholderText(QCoreApplication.translate("Registration", u"e.g. Abdul Nasir", None))
        self.password_label_2.setText(QCoreApplication.translate("Registration", u"Last Name:", None))
        self.backToLogin_button.setText(QCoreApplication.translate("Registration", u"Back to Login", None))
        self.missingFirstName_msg.setText(QCoreApplication.translate("MainWindow", u"Please enter your first name!", None))
    # retranslateUi