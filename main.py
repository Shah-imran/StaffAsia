from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
import dialog
import sys
import os
import var
import calTablePos
from time import sleep
import keystroke
# from pynput.keyboard import Key, Controller
from threading import Thread
import csv
import pyautogui

global app
class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)


class myMainClass():
    def __init__(self):
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.tableRow)
        # self.timer.start(10)

        # self.timer1 = QtCore.QTimer()
        # self.timer1.timeout.connect(self.dataPaste)
        # self.timer1.start(100)
        var.tableRowPos = 1
        var.tableColPos = 0

        self.prevR = GUI.rowNumber.text()
        self.prevC = GUI.columnNumber.text()
        var.prevR = int(self.prevR)
        var.prevC = int(self.prevC)
        GUI.tableWidget.setCurrentCell(var.tableRowPos, var.tableColPos)
        var.preTabPos = [var.tableRowPos, var.tableColPos]
        # GUI.rowNumber.setText(str(self.prevR))
        # GUI.columnNumber.setText(str(self.prevC))
        # self.keyboard = Controller()


        GUI.pushButton_start.clicked.connect(self.start)
        GUI.pushButton_stop.clicked.connect(self.stop)
        GUI.pushButton_generate.clicked.connect(self.interMgenerate)
        GUI.tableWidget.cellClicked.connect(self.updateCo)
        GUI.tableWidget.itemChanged.connect(self.remove)
        GUI.rowNumber.mouseReleaseEvent = (self.onPressed)
        GUI.columnNumber.mouseReleaseEvent = (self.onPressed)
        # GUI.columnNumber.textChanged.connect(self.onPressed)
        # GUI.rowNumber.textChanged.connect(self.onPressed)
        self.answer = 0

    def onPressed(self, event):
        print("warning")
        self.answer = dialog.main()
        print(self.answer)
        if self.answer == 1:
            GUI.pushButton_start.setDisabled(False)
            pyautogui.keyDown("ctrl")
            pyautogui.press("q")
            pyautogui.keyUp("ctrl")
        else:
            GUI.rowNumber.setText(str(self.prevR))
            GUI.columnNumber.setText(str(self.prevC))
            # GUI.pushButton_start.setDisabled(True)


    def updateCo(self):
        print("cell Clicked")
        var.tableRowPos = GUI.tableWidget.currentRow()
        var.tableColPos = GUI.tableWidget.currentColumn()

    def start(self):
        var.runStatus = True
        Thread(target=keystroke.main()).start()
        Thread(target=dataPaste, daemon=True).start()
        if self.answer == 1:
            row = GUI.rowNumber.text()
            column = GUI.columnNumber.text()

            if self.prevR != row and row.isnumeric() == True and row != '':
                self.prevR = var.prevR = int(row)
                GUI.tableWidget.setRowCount(int(row))

            if self.prevC != column and column.isnumeric() == True and column != '':
                self.prevC = var.prevC = int(column)
                GUI.tableWidget.setColumnCount(int(column))
            self.answer = 0
        else:
            GUI.rowNumber.setText(str(self.prevR))
            GUI.columnNumber.setText(str(self.prevC))

        GUI.pushButton_start.setDisabled(True)

    def stop(self):
        print("Stopping")
        GUI.pushButton_start.setDisabled(False)
        pyautogui.keyDown("ctrl")
        pyautogui.press("q")
        pyautogui.keyUp("ctrl")
        var.runStatus = False
    def closeEvent(self):
        print("Close Event")
        GUI.pushButton_start.setDisabled(False)
        pyautogui.keyDown("ctrl")
        pyautogui.press("q")
        pyautogui.keyUp("ctrl")
        var.runStatus = False
        # self.keyboard.press('q')

    def remove(self):
        print("cellChanged")
        GUI.tableWidget.clearSelection()
        GUI.tableWidget.setCurrentCell(var.tableRowPos, var.tableColPos)

    def interMgenerate(self):
        Thread(target=generate, daemon=True).start()

    def tableRow(self):
        row = GUI.rowNumber.text()
        column = GUI.columnNumber.text()

        if self.prevR != row and row.isnumeric() == True and row != '':
            self.prevR = var.prevR = int(row)
            GUI.tableWidget.setRowCount(int(row))
            self.answer = 0

        if self.prevC != column and column.isnumeric() == True and column != '':
            self.prevC = var.prevC = int(column)
            GUI.tableWidget.setColumnCount(int(column))
            self.answer = 0

def dataPaste():
    while var.runStatus!=False:
        try:
            if not var.cText.empty():
                data = var.cText.get()
                GUI.tableWidget.clearSelection()
                GUI.tableWidget.setCurrentCell(data[1][0],data[1][1])
                GUI.tableWidget.setItem(data[1][0],data[1][1], QTableWidgetItem(str(data[0])))
        except Exception as e:
            print(e)

        if var.tableRowPos != var.preTabPos[0] or var.tableColPos != var.preTabPos[1]:
            GUI.tableWidget.clearSelection()
            GUI.tableWidget.setCurrentCell(var.tableRowPos, var.tableColPos)
            var.preTabPos[0] = var.tableRowPos
            var.preTabPos[1] = var.tableColPos

def generate():
    data = list()
    for row in range(0, var.prevR):
        temp = list()
        for col in range(0, var.prevR):
            try:
                item = GUI.tableWidget.item(row, col)
                print(item.text())
                temp.append(item.text())
            except:
                temp.append("")

        data.append(temp)
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(data)



if __name__ == '__main__':

    global app
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    # keyboard = Controller()
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