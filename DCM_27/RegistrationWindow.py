from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QMainWindow
from PySide6.QtGui import QCloseEvent, QFont, QIcon
from PySide6.QtCore import (QCoreApplication, QRect)
from ui_registrationwindow import Ui_Registration

class RegistrationWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration(self)
        # self.ui.setupUi(self)
        self.setup()

    def setup(self):
        self.setGeometry(400, 200, 625, 500)
        self.setWindowTitle("Pacemaker DCM Registration")
        self.setWindowIcon(QIcon('icons/pacemaker_device_icon.png'))

        self.show()

        self.ui.get_create_button().clicked.connect(self.createButton_check)
        self.ui.get_backToLogin_button().clicked.connect(self.backToLoginButton_check)


    def num_of_users(self):
        user_count = 0
        with open('Local_Database.txt', 'r') as f:
            users_list = f.readlines()
            for i in users_list:
                user_count += 1

        return int(user_count / 2)

    def userIsRegistered(self, user):
        num_of_users = self.num_of_users()
        with open('Local_Database.txt', 'r') as f:
            n = range(num_of_users)
            for i in n:
                username = f.readline().replace("\n", "")
                password = f.readline().replace("\n", "")
                if (user == username):
                    return True
            return False

    def charactersCheck(self, text):
        invalid = 0
        for c in text:
            #if (c=="(" or c==")" or c=="," or c=="." or c==" " or c=="&" or c=="%" or c=="^" or c=="*" or c=="=" or c=="+" or c=="/" or c=="|" or c=="[" or c=="]" or c=="{" or c=="}" or c==";" or c==":" or c=="'" or c=='"' or c=="<" or c==">" or c=="?"):
            if ((ord(c)>=48 and ord(c)<=57) or (ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122) or ord(c)==45 or ord(c)==95):
                pass
            else:
                invalid = 1
        if (invalid==0):
            return True
        else:
            return False
    def createButton_check(self):
        if (self.ui.get_create_button().isChecked() == False):
            if (self.ui.get_firstnameInput().text() == ""):
                print("Please enter your first name!")
            if (self.ui.get_lastnameInput().text() == ""):
                print("Please enter your last name!")
            if (self.ui.get_usernameInput().text() == ""):
                print("Please enter an username!")
            if (self.ui.get_passwordInput().text() == ""):
                print("Please enter a password!")
            if (self.ui.get_firstnameInput().text() != "" and self.ui.get_lastnameInput().text() != "" and self.ui.get_usernameInput().text() != "" and self.ui.get_passwordInput().text() != ""):
                if (self.charactersCheck(self.ui.get_usernameInput().text())==False):
                    print("Invalid characters used... Please use letters, numbers, dashes, and/or underscores only!")
                elif (len(self.ui.get_usernameInput().text())<4 or len(self.ui.get_usernameInput().text())>20):
                    print("Error! Invalid number of characters used for the username, please use 4-20 characters.")
                elif (len(self.ui.get_passwordInput().text())<8 or len(self.ui.get_passwordInput().text())>20):
                    print("Error! Invalid number of characters used for the password, please use 8-20 characters.")
                else:
                    # Check if user is already registered
                    if self.userIsRegistered(self.ui.get_usernameInput().text()):
                        print("User already exists! Please login or use a different username.")
                    elif (self.num_of_users() == 10):
                        print("Sorry, the maximum users threshold (10) has already been reached...")
                    else:
                        with open('Local_Database.txt', 'a') as user_login:
                            user_login.write(self.ui.get_usernameInput().text() + "\n")
                            user_login.write(self.ui.get_passwordInput().text() + "\n")
                        with open("Users_data/"+self.ui.get_usernameInput().text()+".txt", "w") as user_data:
                            user_data.write("AOO\n") #MODE
                            user_data.write("0\n") #Lower Rate Limit
                            user_data.write("0\n") #Upper Rate Limit
                            user_data.write("0\n") #Atrial Amplitude
                            user_data.write("0\n") #Atrial Pulse Width
                            user_data.write("VOO\n") #MODE
                            user_data.write("0\n") #Lower Rate Limit
                            user_data.write("0\n") #Upper Rate Limit
                            user_data.write("0\n") #Ventricular Amplitude
                            user_data.write("0\n") #Ventricular Pulse Width
                            user_data.write("AAI\n") #MODE
                            user_data.write("0\n") #Lower Rate Limit
                            user_data.write("0\n") #Upper Rate Limit
                            user_data.write("0\n") #Atrial Amplitude
                            user_data.write("0\n") #Atrial Pulse Width
                            user_data.write("0\n") #Atrial Sensitivity
                            user_data.write("0\n") #Rate Smoothing
                            user_data.write("0\n") #PVARP
                            user_data.write("0\n") #ARP
                            user_data.write("0\n") #Hysteresis
                            user_data.write("VVI\n") #MODE
                            user_data.write("0\n") #Lower Rate Limit
                            user_data.write("0\n") #Upper Rate Limit
                            user_data.write("0\n") #Ventricular Sensitivity
                            user_data.write("0\n") #Rate Smoothing
                            user_data.write("0\n") #Ventricular Amplitude
                            user_data.write("0\n") #Ventricular Pulse Width
                            user_data.write("0\n") #VRP
                            user_data.write("0\n") #Hysteresis
                            user_data.write("AOOR\n")  # MODE
                            user_data.write("0\n")  # Lower Rate Limit
                            user_data.write("0\n")  # Upper Rate Limit
                            user_data.write("0\n")  # Maximum Sensor Rate
                            user_data.write("0\n")  # Activity Threshold
                            user_data.write("0\n")  # Atrial Amplitude
                            user_data.write("0\n")  # Atrial Pulse Width
                            user_data.write("0\n")  # Reaction Time
                            user_data.write("0\n")  # Response Factor
                            user_data.write("0\n")  # Recovery Time
                            user_data.write("VOOR\n")  # MODE
                            user_data.write("0\n")  # Lower Rate Limit
                            user_data.write("0\n")  # Upper Rate Limit
                            user_data.write("0\n")  # Activity Threshold
                            user_data.write("0\n")  # Maximum Sensor Rate
                            user_data.write("0\n")  # Ventricular Amplitude
                            user_data.write("0\n")  # Ventricular Pulse Width
                            user_data.write("0\n")  # Reaction Time
                            user_data.write("0\n")  # Response Factor
                            user_data.write("0\n")  # Recovery Time
                            user_data.write("AAIR\n")  # MODE
                            user_data.write("0\n")  # Lower Rate Limit
                            user_data.write("0\n")  # Upper Rate Limit
                            user_data.write("0\n")  # Maximum Sensor Rate
                            user_data.write("0\n")  # Atrial Sensitivity
                            user_data.write("0\n")  # Atrial Amplitude
                            user_data.write("0\n")  # Atrial Pulse Width
                            user_data.write("0\n")  # ARP
                            user_data.write("0\n")  # PVARP
                            user_data.write("0\n")  # Activity Threshold
                            user_data.write("0\n")  # Reaction Time
                            user_data.write("0\n")  # Rate Smoothing
                            user_data.write("0\n")  # Hysteresis
                            user_data.write("0\n")  # Recovery Time
                            user_data.write("0\n")  # Response Factor
                            user_data.write("VVIR\n")  # MODE
                            user_data.write("0\n")  # Lower Rate Limit
                            user_data.write("0\n")  # Upper Rate Limit
                            user_data.write("0\n")  # Maximum Sensor Rate
                            user_data.write("0\n")  # Ventricular Sensitivity
                            user_data.write("0\n")  # Ventricular Amplitude
                            user_data.write("0\n")  # Ventricular Pulse Width
                            user_data.write("0\n")  # VRP
                            user_data.write("0\n")  # Hysteresis
                            user_data.write("0\n")  # Activity Threshold
                            user_data.write("0\n")  # Reaction Time
                            user_data.write("0\n")  # Rate Smoothing
                            user_data.write("0\n")  # Response Factor
                            user_data.write("0\n")  # Recovery Time
                        self.close()

    def backToLoginButton_check(self):
        if (self.ui.get_backToLogin_button().isChecked() == False):
            self.close()

    # def closeEvent(self, event: QCloseEvent):
    #
    #     reply = QMessageBox.question(self, "Quit DCM", "Are you sure you want to quit?",
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
