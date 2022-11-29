import sys
import platform
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

from mainwindow13 import Ui_DCM

import serial
import serial.tools.list_ports
import struct

class DCM(QMainWindow):
    def __init__(self, user):
        self.user = user
        QMainWindow.__init__(self)
        self.ui = Ui_DCM()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        # self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # PAGE 4
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # PAGE 5
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))

        # PAGE 6
        self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))

        # PAGE 7
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))

        # PAGE 8
        self.ui.btn_page_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        self.load_userData() #Load user's data
        self.ui.get_saveButton().clicked.connect(self.saveButton_check) # Check if the "Save" button has been clicked
        self.ui.get_createGraph_AOO().clicked.connect(self.createGraph_check())  # Check if the "Create Graph" button has been clicked

    def load_userData(self):
        with open("Users_data/" + self.user + ".txt", "r") as user_data:
            user_data.readline() # Read over the mode name (AOO)
            value = int(user_data.readline()) # READ Lower Rate Limit
            self.ui.set_AOO_LRL(value) # SET Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_AOO_URL(value)  # SET Upper Rate Limit
            value = int(user_data.readline())  # READ Atrial Amplitude
            self.ui.set_AOO_AA(value)  # SET Atrial Amplitude
            value = int(user_data.readline())  # READ Atrial Pulse Width
            self.ui.set_AOO_APW(value) # SET Atrial Pulse Width
            user_data.readline() # Read over the mode name (VOO)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_VOO_LRL(value)  # SET Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_VOO_URL(value)  # SET Upper Rate Limit
            value = int(user_data.readline())  # READ Ventricular Amplitude
            self.ui.set_VOO_VA(value)  # SET Ventricular Amplitude
            value = int(user_data.readline())  # READ Ventricular Pulse Width
            self.ui.set_VOO_VPW(value)  # SET Ventricular Pulse Width
            user_data.readline() # Read over the mode name (AAI)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_AAI_LRL(value) # SET Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_AAI_URL(value)  # SET Upper Rate Limit
            value = int(user_data.readline())  # READ Atrial Amplitude
            self.ui.set_AAI_AA(value) # SET Atrial Amplitude
            value = int(user_data.readline())  # READ Atrial Pulse Width
            self.ui.set_AAI_APW(value)  # SET Atrial Pulse Width
            value = int(user_data.readline())  # READ Atrial Sensitivity
            self.ui.set_AAI_AS(value) # SET Atrial Sensitivity
            value = int(user_data.readline())  # READ Rate Smoothing
            self.ui.set_AAI_RS(value)  # SET Rate Smoothing
            value = int(user_data.readline())  # READ PVARP
            self.ui.set_AAI_PVARP(value)  # SET PVARP
            value = int(user_data.readline())  # READ ARP
            self.ui.set_AAI_ARP(value)  # SET ARP
            value = int(user_data.readline())  # READ Hysteresis
            self.ui.set_AAI_H(value)  # SET Hysteresis
            user_data.readline() # Read over the mode name (VVI)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_VVI_LRL(value)  # SET Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_VVI_URL(value)  # SET Upper Rate Limit
            value = int(user_data.readline())  # READ Ventricular Sensitivity
            self.ui.set_VVI_VS(value)  # SET Ventricular Sensitivity
            value = int(user_data.readline())  # READ Rate Smoothing
            self.ui.set_VVI_RS(value)  # SET Rate Smoothing
            value = int(user_data.readline())  # READ Ventricular Amplitude
            self.ui.set_VVI_VA(value)  # SET Ventricular Amplitude
            value = int(user_data.readline())  # READ Ventricular Pulse Width
            self.ui.set_VVI_VPW(value)  # SET Ventricular Pulse Width
            value = int(user_data.readline())  # READ VRP
            self.ui.set_VVI_VRP(value)  # SET VRP
            value = int(user_data.readline())  # READ Hysteresis
            self.ui.set_VVI_H(value)  # SET Hysteresis
            user_data.readline() # Read over the mode name (AOOR)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_AOOR_LRL(value) # Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_AOOR_URL(value)  # Upper Rate Limit
            value = int(user_data.readline())  # READ Maximum Sensor Rate
            self.ui.set_AOOR_MSR(value)  # Maximum Sensor Rate
            value = int(user_data.readline())  # READ Activity Threshold
            self.ui.set_AOOR_AT(value)  # Activity Threshold
            value = int(user_data.readline())  # READ Atrial Amplitude
            self.ui.set_AOOR_AA(value)  # Atrial Amplitude
            value = int(user_data.readline())  # READ Atrial Pulse Width
            self.ui.set_AOOR_APW(value)  # Atrial Pulse Width
            value = int(user_data.readline())  # READ Reaction Time
            self.ui.set_AOOR_ReactT(value)  # Reaction Time
            value = int(user_data.readline())  # READ Response Factor
            self.ui.set_AOOR_RF(value)  # Response Factor
            value = int(user_data.readline())  # READ Recovery Time
            self.ui.set_AOOR_RecT(value)  # Recovery Time
            user_data.readline() # Read over the mode name (VOOR)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_VOOR_LRL(value)  # Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_VOOR_URL(value)  # Upper Rate Limit
            value = int(user_data.readline())  # READ Activity Threshold
            self.ui.set_VOOR_AT(value)  # Activity Threshold
            value = int(user_data.readline())  # READ Maximum Sensor Rate
            self.ui.set_VOOR_MSR(value) # Maximum Sensor Rate
            value = int(user_data.readline())  # READ Ventricular Amplitude
            self.ui.set_VOOR_VA(value)  # Ventricular Amplitude
            value = int(user_data.readline())  # READ Ventricular Pulse Width
            self.ui.set_VOOR_VPW(value)  # Ventricular Pulse Width
            value = int(user_data.readline())  # READ Reaction Time
            self.ui.set_VOOR_ReactT(value)  # Reaction Time
            value = int(user_data.readline())  # READ Response Factor
            self.ui.set_VOOR_RF(value)  # Response Factor
            value = int(user_data.readline())  # READ Recovery Time
            self.ui.set_VOOR_RecT(value)  # Recovery Time
            user_data.readline() # Read over the mode name (AAIR)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_AAIR_LRL(value)  # Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_AAIR_URL(value)  # Upper Rate Limit
            value = int(user_data.readline())  # READ Maximum Sensor Rate
            self.ui.set_AAIR_MSR(value)  # Maximum Sensor Rate
            value = int(user_data.readline())  # READ Atrial Sensitivity
            self.ui.set_AAIR_AS(value) # Atrial Sensitivity
            value = int(user_data.readline())  # READ Atrial Amplitude
            self.ui.set_AAIR_AA(value)  # Atrial Amplitude
            value = int(user_data.readline())  # READ Atrial Pulse Width
            self.ui.set_AAIR_APW(value)  # Atrial Pulse Width
            value = int(user_data.readline())  # READ ARP
            self.ui.set_AAIR_ARP(value)  # ARP
            value = int(user_data.readline())  # READ PVARP
            self.ui.set_AAIR_PVARP(value)  # PVARP
            value = int(user_data.readline())  # READ Activity Threshold
            self.ui.set_AAIR_AT(value)  # Activity Threshold
            value = int(user_data.readline())  # READ Reaction Time
            self.ui.set_AAIR_ReactT(value)  # Reaction Time
            value = int(user_data.readline())  # READ Rate Smoothing
            self.ui.set_AAIR_RS(value)  # Rate Smoothing
            value = int(user_data.readline())  # READ Hysteresis
            self.ui.set_AAIR_H(value)  # Hysteresis
            value = int(user_data.readline())  # READ Recovery Time
            self.ui.set_AAIR_RecT(value) # Recovery Time
            value = int(user_data.readline())  # READ Response Factor
            self.ui.set_AAIR_RF(value) # Response Factor
            user_data.readline() # Read over the mode name (VVIR)
            value = int(user_data.readline())  # READ Lower Rate Limit
            self.ui.set_VVIR_LRL(value)  # Lower Rate Limit
            value = int(user_data.readline())  # READ Upper Rate Limit
            self.ui.set_VVIR_URL(value)  # Upper Rate Limit
            value = int(user_data.readline())  # READ Maximum Sensor Rate
            self.ui.set_VVIR_MSR(value) # Maximum Sensor Rate
            value = int(user_data.readline())  # READ Ventricular Sensitivity
            self.ui.set_VVIR_VS(value)  # Ventricular Sensitivity
            value = int(user_data.readline())  # READ Ventricular Amplitude
            self.ui.set_VVIR_VA(value)  # Ventricular Amplitude
            value = int(user_data.readline())  # READ Atrial Pulse Width
            self.ui.set_VVIR_VPW(value)  # Ventricular Pulse Width
            value = int(user_data.readline())  # READ VRP
            self.ui.set_VVIR_VRP(value)  # VRP
            value = int(user_data.readline())  # READ Hysteresis
            self.ui.set_VVIR_H(value)  # Hysteresis
            value = int(user_data.readline())  # READ Activity Threshold
            self.ui.set_VVIR_AT(value)  # Activity Threshold
            value = int(user_data.readline())  # READ Reaction Time
            self.ui.set_VVIR_ReactT(value)  # Reaction Time
            value = int(user_data.readline())  # READ Rate Smoothing
            self.ui.set_VVIR_RS(value)  # Rate Smoothing
            value = int(user_data.readline())  # READ Response Factor
            self.ui.set_VVIR_RF(value)  # Response Factor
            value = int(user_data.readline())  # READ Recovery Time
            self.ui.set_VVIR_RecT(value)  # Recovery Time

    def saveButton_check(self):
        # If "Save" button is pressed, save all the user's parameters information
        if (self.ui.get_saveButton().isChecked() == False):
            with open("Users_data/" + self.user + ".txt", "w") as user_data:
                user_data.write("AOO\n")  # MODE
                user_data.write(str(self.ui.get_AOO_LRL().value())+"\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_AOO_URL().value())+"\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_AOO_AA().value())+"\n")  # Atrial Amplitude
                user_data.write(str(self.ui.get_AOO_APW().value())+"\n")  # Atrial Pulse Width
                user_data.write("VOO\n")  # MODE
                user_data.write(str(self.ui.get_VOO_LRL().value())+"\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_VOO_URL().value())+"\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_VOO_VA().value())+"\n")  # Ventricular Amplitude
                user_data.write(str(self.ui.get_VOO_VPW().value())+"\n")  # Ventricular Pulse Width
                user_data.write("AAI\n")  # MODE
                user_data.write(str(self.ui.get_AAI_LRL().value())+"\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_AAI_URL().value())+"\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_AAI_AA().value())+"\n")  # Atrial Amplitude
                user_data.write(str(self.ui.get_AAI_APW().value())+"\n")  # Atrial Pulse Width
                user_data.write(str(self.ui.get_AAI_AS().value())+"\n")  # Atrial Sensitivity
                user_data.write(str(self.ui.get_AAI_RS().value())+"\n")  # Rate Smoothing
                user_data.write(str(self.ui.get_AAI_PVARP().value())+"\n")  # PVARP
                user_data.write(str(self.ui.get_AAI_ARP().value())+"\n")  # ARP
                user_data.write(str(self.ui.get_AAI_H().value())+"\n")  # Hysteresis
                user_data.write("VVI\n")  # MODE
                user_data.write(str(self.ui.get_VVI_LRL().value())+"\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_VVI_URL().value())+"\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_VVI_VS().value())+"\n")  # Ventricular Sensitivity
                user_data.write(str(self.ui.get_VVI_RS().value())+"\n")  # Rate Smoothing
                user_data.write(str(self.ui.get_VVI_VA().value())+"\n")  # Ventricular Amplitude
                user_data.write(str(self.ui.get_VVI_VPW().value())+"\n")  # Ventricular Pulse Width
                user_data.write(str(self.ui.get_VVI_VRP().value())+"\n")  # VRP
                user_data.write(str(self.ui.get_VVI_H().value())+"\n")  # Hysteresis
                user_data.write("AOOR\n")  # MODE
                user_data.write(str(self.ui.get_AOOR_LRL().value()) + "\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_AOOR_URL().value()) + "\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_AOOR_MSR().value()) + "\n")  # Maximum Sensor Rate
                user_data.write(str(self.ui.get_AOOR_AT().value()) + "\n")  # Activity Threshold
                user_data.write(str(self.ui.get_AOOR_AA().value()) + "\n")  # Atrial Amplitude
                user_data.write(str(self.ui.get_AOOR_APW().value()) + "\n")  # Atrial Pulse Width
                user_data.write(str(self.ui.get_AOOR_ReactT().value()) + "\n")  # Reaction Time
                user_data.write(str(self.ui.get_AOOR_RF().value()) + "\n")  # Response Factor
                user_data.write(str(self.ui.get_AOOR_RecT().value()) + "\n")  # Recovery Time
                user_data.write("VOOR\n")  # MODE
                user_data.write(str(self.ui.get_VOOR_LRL().value()) + "\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_VOOR_URL().value()) + "\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_VOOR_AT().value()) + "\n")  # Activity Threshold
                user_data.write(str(self.ui.get_VOOR_MSR().value()) + "\n")  # Maximum Sensor Rate
                user_data.write(str(self.ui.get_VOOR_VA().value()) + "\n")  # Ventricular Amplitude
                user_data.write(str(self.ui.get_VOOR_VPW().value()) + "\n")  # Ventricular Pulse Width
                user_data.write(str(self.ui.get_VOOR_ReactT().value()) + "\n")  # Reaction Time
                user_data.write(str(self.ui.get_VOOR_RF().value()) + "\n")  # Response Factor
                user_data.write(str(self.ui.get_VOOR_RecT().value()) + "\n")  # Recovery Time
                user_data.write("AAIR\n")  # MODE
                user_data.write(str(self.ui.get_AAIR_LRL().value()) + "\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_AAIR_URL().value()) + "\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_AAIR_MSR().value()) + "\n")  # Maximum Sensor Rate
                user_data.write(str(self.ui.get_AAIR_AS().value()) + "\n")  # Atrial Sensitivity
                user_data.write(str(self.ui.get_AAIR_AA().value()) + "\n")  # Atrial Amplitude
                user_data.write(str(self.ui.get_AAIR_APW().value()) + "\n")  # Atrial Pulse Width
                user_data.write(str(self.ui.get_AAIR_ARP().value()) + "\n")  # ARP
                user_data.write(str(self.ui.get_AAIR_PVARP().value()) + "\n")  # PVARP
                user_data.write(str(self.ui.get_AAIR_AT().value()) + "\n")  # Activity Threshold
                user_data.write(str(self.ui.get_AAIR_ReactT().value()) + "\n")  # Reaction Time
                user_data.write(str(self.ui.get_AAIR_RS().value()) + "\n")  # Rate Smoothing
                user_data.write(str(self.ui.get_AAIR_H().value()) + "\n")  # Hysteresis
                user_data.write(str(self.ui.get_AAIR_RecT().value()) + "\n")  # Recovery Time
                user_data.write(str(self.ui.get_AAIR_RF().value()) + "\n")  # Response Factor
                user_data.write("VVIR\n")  # MODE
                user_data.write(str(self.ui.get_VVIR_LRL().value()) + "\n")  # Lower Rate Limit
                user_data.write(str(self.ui.get_VVIR_URL().value()) + "\n")  # Upper Rate Limit
                user_data.write(str(self.ui.get_VVIR_MSR().value()) + "\n")  # Maximum Sensor Rate
                user_data.write(str(self.ui.get_VVIR_VS().value()) + "\n")  # Ventricular Sensitivity
                user_data.write(str(self.ui.get_VVIR_VA().value()) + "\n")  # Ventricular Amplitude
                user_data.write(str(self.ui.get_VVIR_VPW().value()) + "\n")  # Ventricular Pulse Width
                user_data.write(str(self.ui.get_VVIR_VRP().value()) + "\n")  # VRP
                user_data.write(str(self.ui.get_VVIR_H().value()) + "\n")  # Hysteresis
                user_data.write(str(self.ui.get_VVIR_AT().value()) + "\n")  # Activity Threshold
                user_data.write(str(self.ui.get_VVIR_ReactT().value()) + "\n")  # Reaction Time
                user_data.write(str(self.ui.get_VVIR_RS().value()) + "\n")  # Rate Smoothing
                user_data.write(str(self.ui.get_VVIR_RF().value()) + "\n")  # Response Factor
                user_data.write(str(self.ui.get_VVIR_RecT().value()) + "\n")  # Recovery Time


    '''
    ATR_DUTY_CYCLE = struct.pack("B", )
    ATR_PW = struct.pack("B", self.ui.get_AOO_APW())
    Mode = struct.pack("B", 1)
    VENT_DUTY_CYCLE = struct.pack("B", )
    VENT_PW = struct.pack("B", )
    ARP = struct.pack("B", )
    VRP = struct.pack("B", )
    LRL = struct.pack("B", )
    Activity_Threshold = struct.pack("B", )
    Response_Factor = struct.pack("B", )
    Recovery_Time = struct.pack("B", )
    Max_Sensor_Rate = struct.pack("B", )
    Reaction_Time = struct.pack("B", )
    '''
    def createGraph_check(self):
        # Determine the mode the user is using

        # AOO
        if (self.ui.get_createGraph_AOO().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", self.ui.get_AOO_AA().value())
            ATR_PW = struct.pack("B", self.ui.get_AOO_APW().value())
            Mode = struct.pack("B", 1)
            VENT_AMP = struct.pack("B", 0)
            VENT_PW = struct.pack("B", 0)
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", 0)
            LRL = struct.pack("B", self.ui.get_AOO_LRL().value())
            Activity_Threshold = struct.pack("B", 0)
            Response_Factor = struct.pack("B", 0)
            Recovery_Time = struct.pack("B", 0)
            Max_Sensor_Rate = struct.pack("B", 0)
            Reaction_Time = struct.pack("B", 0)

            ATR_Egram = struct.pack("B", 0)
            VENT_Egram = struct.pack("B", 0)

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time + ATR_Egram + VENT_Egram

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]
                ATR_Egram = data[13]
                VENT_Egram = data[14]

                #Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # VOO
        if (self.ui.get_createGraph_VOO().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", 0)
            ATR_PW = struct.pack("B", 0)
            Mode = struct.pack("B", 2)
            VENT_AMP = struct.pack("B", self.ui.get_VOO_VA().value())
            VENT_PW = struct.pack("B", self.ui.get_VOO_VPW().value())
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", 0)
            LRL = struct.pack("B", self.ui.get_VOO_LRL().value())
            Activity_Threshold = struct.pack("B", 0)
            Response_Factor = struct.pack("B", 0)
            Recovery_Time = struct.pack("B", 0)
            Max_Sensor_Rate = struct.pack("B", 0)
            Reaction_Time = struct.pack("B", 0)

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # AAI
        if (self.ui.get_createGraph_AAI().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", self.ui.get_AAI_AA().value())
            ATR_PW = struct.pack("B", self.ui.get_AAI_APW().value())
            Mode = struct.pack("B", 3)
            VENT_AMP = struct.pack("B", 0)
            VENT_PW = struct.pack("B", 0)
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", 0)
            LRL = struct.pack("B", self.ui.get_AAI_LRL().value())
            Activity_Threshold = struct.pack("B", 0)
            Response_Factor = struct.pack("B", 0)
            Recovery_Time = struct.pack("B", 0)
            Max_Sensor_Rate = struct.pack("B", 0)
            Reaction_Time = struct.pack("B", 0)

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # VVI
        if (self.ui.get_createGraph_VVI().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", 0)
            ATR_PW = struct.pack("B", 0)
            Mode = struct.pack("B", 4)
            VENT_AMP = struct.pack("B", self.ui.get_VVI_VA().value())
            VENT_PW = struct.pack("B", self.ui.get_VVI_VPW().value())
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", self.ui.get_VVI_VRP().value())
            LRL = struct.pack("B", self.ui.get_VVI_LRL().value())
            Activity_Threshold = struct.pack("B", 0)
            Response_Factor = struct.pack("B", 0)
            Recovery_Time = struct.pack("B", 0)
            Max_Sensor_Rate = struct.pack("B", 0)
            Reaction_Time = struct.pack("B", 0)

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # AOOR
        if (self.ui.get_createGraph_AOOR().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", self.ui.get_AOOR_AA().value())
            ATR_PW = struct.pack("B", self.ui.get_AOOR_APW().value())
            Mode = struct.pack("B", 5)
            VENT_AMP = struct.pack("B", 0)
            VENT_PW = struct.pack("B", 0)
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", 0)
            LRL = struct.pack("B", self.ui.get_AOOR_LRL().value())
            Activity_Threshold = struct.pack("B", self.ui.get_AOOR_AT().value())
            Response_Factor = struct.pack("B", self.ui.get_AOOR_RF().value())
            Recovery_Time = struct.pack("B", self.ui.get_AOOR_RecT().value())
            Max_Sensor_Rate = struct.pack("B", self.ui.get_AOOR_MSR().value())
            Reaction_Time = struct.pack("B", self.ui.get_AOOR_ReactT().value())

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # VOOR
        if (self.ui.get_createGraph_VOOR().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", 0)
            ATR_PW = struct.pack("B", 0)
            Mode = struct.pack("B", 6)
            VENT_AMP = struct.pack("B", self.ui.get_VOOR_VA().value())
            VENT_PW = struct.pack("B", self.ui.get_VOOR_VPW().value())
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", 0)
            LRL = struct.pack("B", self.ui.get_VOOR_LRL().value())
            Activity_Threshold = struct.pack("B", self.ui.get_VOOR_AT().value())
            Response_Factor = struct.pack("B", self.ui.get_VOOR_RF().value())
            Recovery_Time = struct.pack("B", self.ui.get_VOOR_RecT().value())
            Max_Sensor_Rate = struct.pack("B", self.ui.get_VOOR_MSR().value())
            Reaction_Time = struct.pack("B", self.ui.get_VOOR_ReactT().value())

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # AAIR
        if (self.ui.get_createGraph_AAIR().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", self.ui.get_AAIR_AA().value())
            ATR_PW = struct.pack("B", self.ui.get_AAIR_APW().value())
            Mode = struct.pack("B", 7)
            VENT_AMP = struct.pack("B", 0)
            VENT_PW = struct.pack("B", 0)
            ARP = struct.pack("B",  self.ui.get_AAIR_ARP().value())
            VRP = struct.pack("B", 0)
            LRL = struct.pack("B", self.ui.get_AOOR_LRL().value())
            Activity_Threshold = struct.pack("B", self.ui.get_AAIR_AT().value())
            Response_Factor = struct.pack("B", self.ui.get_AAIR_RF().value())
            Recovery_Time = struct.pack("B", self.ui.get_AAIR_RecT().value())
            Max_Sensor_Rate = struct.pack("B", self.ui.get_AAIR_MSR().value())
            Reaction_Time = struct.pack("B", self.ui.get_AAIR_ReactT().value())

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")

        # VVIR
        if (self.ui.get_createGraph_VVIR().isChecked() == False):
            frdm_port = "COM5"

            Start = b'\x16'
            SYNC = b'\x22'
            Fn_set = b'\x55'
            ATR_AMP = struct.pack("B", 0)
            ATR_PW = struct.pack("B", 0)
            Mode = struct.pack("B", 8)
            VENT_AMP = struct.pack("B", self.ui.get_VVIR_VA().value())
            VENT_PW = struct.pack("B", self.ui.get_VVIR_VPW().value())
            ARP = struct.pack("B", 0)
            VRP = struct.pack("B", self.ui.get_VVIR_VRP().value())
            LRL = struct.pack("B", self.ui.get_VVIR_LRL().value())
            Activity_Threshold = struct.pack("B", self.ui.get_VVIR_AT().value())
            Response_Factor = struct.pack("B", self.ui.get_VVIR_RF().value())
            Recovery_Time = struct.pack("B", self.ui.get_VVIR_RecT().value())
            Max_Sensor_Rate = struct.pack("B", self.ui.get_VVIR_MSR().value())
            Reaction_Time = struct.pack("B", self.ui.get_VVIR_ReactT().value())

            Signal_set = Start + Fn_set + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time
            Signal_echo = Start + SYNC + ATR_AMP + ATR_PW + Mode + VENT_AMP + VENT_PW + ARP + VRP + LRL + Activity_Threshold + Response_Factor + Recovery_Time + Max_Sensor_Rate + Reaction_Time

            # Set parameters (sending data)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)

            # Read data (receiving)
            with serial.Serial(frdm_port, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                data = pacemaker.read(13)
                ATR_AMP_rev = data[0]
                ATR_PW_rev = data[1]
                Mode_rev = data[2]
                VENT_AMP_rev = data[3]
                VENT_PW_rev = data[4]
                ARP_rev = data[5]
                VRP_rev = data[6]
                LRL_rev = data[7]
                Activity_Threshold_rev = data[8]
                Response_Factor_rev = data[9]
                Recovery_Time_rev = data[10]
                Max_Sensor_Rate_rev = data[11]
                Reaction_Time_rev = data[12]

                # Verify the stored data in the Pacemaker device
                if (ATR_AMP != ATR_AMP_rev):
                    print("Error! 'Atrial Amplitude' data stored incorrectly.")
                if (ATR_PW != ATR_PW_rev):
                    print("Error! 'Atrial Pulse Width' data stored incorrectly.")
                if (Mode != Mode_rev):
                    print("Error! 'Mode' data stored incorrectly.")
                if (VENT_AMP != VENT_AMP_rev):
                    print("Error! 'Ventricular Amplitude' data stored incorrectly.")
                if (VENT_PW != VENT_PW_rev):
                    print("Error! 'Ventricular Pulse Width' data stored incorrectly.")
                if (ARP != ARP_rev):
                    print("Error! 'ARP' data stored incorrectly.")
                if (VRP != VRP_rev):
                    print("Error! 'VRP' data stored incorrectly.")
                if (LRL != LRL_rev):
                    print("Error! 'Lower Rate Limit' data stored incorrectly.")
                if (Activity_Threshold != Activity_Threshold_rev):
                    print("Error! 'Activity Threshold' data stored incorrectly.")
                if (Response_Factor != Response_Factor_rev):
                    print("Error! 'Response Factor' data stored incorrectly.")
                if (Recovery_Time != Recovery_Time_rev):
                    print("Error! 'Recovery Time' data stored incorrectly.")
                if (Max_Sensor_Rate != Max_Sensor_Rate_rev):
                    print("Error! 'Maximum Sensor Rate' data stored incorrectly.")
                if (Reaction_Time != Reaction_Time_rev):
                    print("Error! 'Reaction Time' data stored incorrectly.")