import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout
import matplotlib
import psutil as ps
import time
import threading

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

Form = uic.loadUiType(os.path.join(os.getcwd(), "mainwindow.ui"))[0]


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow, Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.label_CPU: QLabel = self.label_CPU
        self.matplotlib_container: QGridLayout = self.matplotlib_container
        self.graph = MplCanvas()
        self.graph.axes.plot([])
        self.matplotlib_container.addWidget(self.graph)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
