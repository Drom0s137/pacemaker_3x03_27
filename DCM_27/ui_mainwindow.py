# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from RegistrationWindow import RegistrationWindow
from DCM_Window import DCM

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(u"background-color:'lightgrey'")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.welcomeMessage_label = QLabel(self.centralwidget)
        self.welcomeMessage_label.setObjectName(u"welcomeMessage_label")
        self.welcomeMessage_label.setGeometry(QRect(150, 40, 321, 121))
        self.welcomeMessage_label.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        self.welcomeMessage_label.setFont(font)
        self.welcomeMessage_label.setStyleSheet(u"color:'yellow'")
        self.welcomeMessage_label.setAlignment(Qt.AlignCenter)
        self.usernameInput = QLineEdit(self.centralwidget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(240, 160, 201, 21))
        self.usernameInput.setStyleSheet(u"background-color:'white'")
        self.passwordInput = QLineEdit(self.centralwidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(240, 200, 201, 21))
        self.passwordInput.setStyleSheet(u"background-color:'white'")
        self.passwordInput.setEchoMode(QLineEdit.Password) # hide password characters (on screen)
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(180, 155, 61, 31))
        self.username_label.setStyleSheet(u"color:'black'")
        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(180, 195, 61, 31))
        self.password_label.setStyleSheet(u"color:'black'")
        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(370, 230, 75, 24))
        self.login_button.setStyleSheet(u"background-color:'white'")
        self.newUser_label = QLabel(self.centralwidget)
        self.newUser_label.setObjectName(u"newUser_label")
        self.newUser_label.setGeometry(QRect(190, 270, 61, 21))
        self.newUser_label.setStyleSheet(u"color:'black'")
        self.register_button = QPushButton(self.centralwidget)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(250, 270, 81, 21))
        self.register_button.setStyleSheet(u"background-color:'white'")
        self.register_button.setCheckable(False)
        self.incorrectPassword_label = QLabel(self.centralwidget)
        self.incorrectPassword_label.setObjectName(u"incorrectPassword_label")
        self.incorrectPassword_label.setGeometry(QRect(250, 230, 120, 10))
        self.incorrectPassword_label.setStyleSheet(u"color:'red'")
        self.incorrectPassword_label.hide()
        self.invalidUsername_label = QLabel(self.centralwidget)
        self.invalidUsername_label.setObjectName(u"invalidUsername_label")
        self.invalidUsername_label.setGeometry(QRect(250, 230, 120, 10))
        self.invalidUsername_label.setStyleSheet(u"color:'red'")
        self.invalidUsername_label.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.login_button.clicked.connect(self.loginButton_check)
        self.register_button.clicked.connect(self.registerButton_check)
    # setupUi
    def num_of_users(self):
        user_count = 0
        with open('Local_Database.txt', 'r') as f:
            users_list = f.readlines()
            for i in users_list:
                user_count += 1

        return int(user_count / 2)

    def loginButton_check(self):

        if (self.login_button.isChecked() == False):
            self.invalidUsername_label.hide()
            self.incorrectPassword_label.hide()
            num_of_users = self.num_of_users()
            #Open local database and check if the user credentials are correct
            with open('Local_Database.txt', 'r') as f:
                username_check = 0
                n = range(num_of_users)
                for i in n:
                    username = f.readline().replace("\n", "")
                    password = f.readline().replace("\n", "")
                    #Check if user exists
                    if (self.usernameInput.text() == username):
                        username_check = 1
                        #Check if the password is correct
                        if (self.passwordInput.text() == password):
                            print("Login Successful!")
                            self.dcm = DCM(self.usernameInput.text()) #Successful login, open the user's pacemaker DCM
                        else:
                            self.incorrectPassword_label.show()
                            print("Incorrect Password!")
                if (username_check==0):
                    self.invalidUsername_label.show()
                    print("Invalid Username!")

    def registerButton_check(self):
        if (self.register_button.isChecked() == False):
            # Open registration window
            self.r = RegistrationWindow()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcomeMessage_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to the DCM! ", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.newUser_label.setText(QCoreApplication.translate("MainWindow", u"New User? ", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Register Now", None))
        self.incorrectPassword_label.setText(QCoreApplication.translate("MainWindow", u"Incorrect Password!", None))
        self.invalidUsername_label.setText(QCoreApplication.translate("MainWindow", u"Invalid Username!", None))
    # retranslateUi

