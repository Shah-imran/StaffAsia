from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
import sys
import os
import var
import calTablePos
from time import sleep
import keystroke
from pynput.keyboard import Key, Controller
from threading import Thread

global app
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

        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.dataPaste)
        self.timer1.start(100)


        self.prevR = 100
        self.prevC = 5
        var.prevR = int(self.prevR)
        var.prevC = int(self.prevC)
        GUI.tableWidget.setCurrentCell(var.tableRowPos, var.tableColPos)
        self.preTabPos = [var.tableRowPos, var.tableColPos]
        GUI.rowNumber.setText(str(self.prevR))
        GUI.columnNumber.setText(str(self.prevC))
        self.keyboard = Controller()


        GUI.pushButton_start.clicked.connect(self.start)
        GUI.pushButton_stop.clicked.connect(self.stop)
        GUI.pushButton_generate.clicked.connect(self.generate)

    def start(self):
        var.quitingStatus = False
        var.runStatus = True
        Thread(target=keystroke.main()).start()

    def stop(self):
        print("Stopping")
        self.keyboard.press('q')
        # var.runStatus = False
    def closeEvent(self):
        print("Close Event")
        self.keyboard.press('q')

    def generate(self):
        pass

    def dataPaste(self):
        try:
            if not var.cText.empty():
                data = var.cText.get()
                GUI.tableWidget.setItem(data[1][0],data[1][1], QTableWidgetItem(str(data[0])))
        except Exception as e:
            print(e)

    def tableRow(self):
        if var.tableRowPos != self.preTabPos[0] or var.tableColPos != self.preTabPos[1]:
            GUI.tableWidget.clearSelection()
            GUI.tableWidget.setCurrentCell(var.tableRowPos, var.tableColPos)
            self.preTabPos[0] = var.tableRowPos
            self.preTabPos[1] = var.tableColPos


        row = GUI.rowNumber.text()
        column = GUI.columnNumber.text()


        if self.prevR != row and row.isnumeric() == True and row != '':
            self.prevR = var.prevR = int(row)
            GUI.tableWidget.setRowCount(int(row))

        if self.prevC != column and column.isnumeric() == True and column != '':
            self.prevC = var.prevC = int(column)
            GUI.tableWidget.setColumnCount(int(column))


if __name__ == '__main__':

    global app
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    keyboard = Controller()
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
    print("Exit")
    sys.exit()