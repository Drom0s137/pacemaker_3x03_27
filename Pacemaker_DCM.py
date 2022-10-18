from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QMainWindow
from PySide6.QtGui import QCloseEvent, QFont, QIcon
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup()

    def setup(self):
        btn_quit = QPushButton("Quit", self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(1200, 700)
        btn_quit.setStyleSheet('background-color:white')

        self.setGeometry(400, 200, 1100, 700)
        self.setWindowTitle("Pacemaker DCM")
        self.setWindowIcon(QIcon('icons/pacemaker_device_icon.png'))
        # self.setStyleSheet('background-color:lightblue')

        # label = QLabel("Welcome to the DCM!", self)
        # label.setText("Welcome to the DCM!")
        # label.setFont(QFont("Arial", 30))
        # label.move(570, 200)

        self.show()

    def closeEvent(self, event: QCloseEvent):

        reply = QMessageBox.question(self, "Quit DCM", "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# class Login

def run():
    app = QApplication([])

    ex = MainWindow()

    app.exec_()


if __name__ == '__main__':
    run()