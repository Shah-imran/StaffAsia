from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import os
#import var
import threading


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(dialog)


class myMainClass():
    def __init__(self):

        pass


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('favicon.ico')
        dialog.setWindowIcon(QtGui.QIcon(p))
    except Exception as e:
        print(e)
        pass

    dialog.setWindowFlags(dialog.windowFlags() |
                          QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowSystemMenuHint)
    dialog.setWindowFlags(dialog.windowFlags() |
                          QtCore.Qt.WindowSystemMenuHint |
                          QtCore.Qt.WindowMinMaxButtonsHint)

    GUI = MyGui(dialog)
    dialog.show()

    myMC = myMainClass()

    app.exec_()
    print("Exit")
    sys.exit()