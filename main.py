from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import clipboard
import os
import var
import time

#import var
import threading


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)


class myMainClass():
    def __init__(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tableRow)
        self.timer.start(10)

        self.prevR = 100
        self.prevC = 100

        GUI.pushButton_start.clicked.connect(self.start)
        GUI.pushButton_stop.clicked.connect(self.stop)
        GUI.pushButton_generate.clicked.connect(self.generate)

    def start(self):
        var.runStatus = True
        clipboard.copy(0, "thread-0").start()
        pass
    def stop(self):
        var.runStatus = False
        print("stopping")
    def generate(self):
        pass

    def tableRow(self):
        row = GUI.rowNumber.text()
        column = GUI.columnNumber.text()
        if self.prevR != row and row.isnumeric() == True and row != '':
            self.prevR = row
            GUI.tableWidget.setRowCount(int(row))

        if self.prevC != column and column.isnumeric() == True and column != '':
            self.prevC = column
            GUI.tableWidget.setColumnCount(int(column))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('favicon.ico')
        mainWindow.setWindowIcon(QtGui.QIcon(p))
    except Exception as e:
        print(e)

    mainWindow.setWindowFlags(mainWindow.windowFlags() |
                          QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowSystemMenuHint)
    mainWindow.setWindowFlags(mainWindow.windowFlags() |
                          QtCore.Qt.WindowSystemMenuHint |
                          QtCore.Qt.WindowMinMaxButtonsHint)

    GUI = MyGui(mainWindow)
    mainWindow.show()

    myMC = myMainClass()

    app.exec_()
    var.runStatus = False
    time.sleep(3)
    print("Exit")
    sys.exit()