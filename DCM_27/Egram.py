from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from PySide6.QtCore import QTimer
import sys
from random import randint


class Egram(QMainWindow):

    def __init__(self):
        super(Egram, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.time = list(range(100))
        self.volt_1 = [randint(0,100) for _ in range(100)]
        self.volt_2 = [randint(0,100) for _ in range(100)]

        #Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle("Egram", color="b", size="20pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "15px"}
        self.graphWidget.setLabel("left", "Voltage (V)", **styles)
        self.graphWidget.setLabel("bottom", "Time", **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)



        pen1 = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 0, 255))
        self.data_line_1 =  self.graphWidget.plot(self.time, self.volt_1, pen=pen1)
        self.data_line_2 =  self.graphWidget.plot(self.time, self.volt_2, pen=pen2)

        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.update_plot_data_1)
        self.timer.timeout.connect(self.update_plot_data_2)
        self.timer.start()

        self.show()
   


    def update_plot_data_1(self):

        self.time = self.time[1:]  # Remove the first y element.
        self.time.append(self.time[-1] + 1)  # Add a new value 1 higher than the last.

        self.volt_1 = self.volt_1[1:]  # Remove the first
        self.volt_1.append( randint(0,100))  # Add a new random value.

        self.data_line_1.setData(self.time, self.volt_1)  # Update the data.

    def update_plot_data_2(self):

        self.time = self.time[1:]  # Remove the first y element.
        self.time.append(self.time[-1] + 1)  # Add a new value 1 higher than the last.

        self.volt_2 = self.volt_2[1:]  # Remove the first
        self.volt_2.append( randint(0,100))  # Add a new random value.

        self.data_line_2.setData(self.time, self.volt_2)  # Update the data.


#app = QApplication(sys.argv)
#main = Egram()
#main.show()
#app.exec_()
