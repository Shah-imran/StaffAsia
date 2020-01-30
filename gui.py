# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 839)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:  #2c7873;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.softwareName = QtWidgets.QLabel(self.centralwidget)
        self.softwareName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.softwareName.sizePolicy().hasHeightForWidth())
        self.softwareName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.softwareName.setFont(font)
        self.softwareName.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.softwareName.setStyleSheet("font: 48pt \"Times New Roman\";\n"
"color:  #52de97;\n"
"background-color: #2c7873;\n"
"")
        self.softwareName.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.softwareName.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.softwareName.setAlignment(QtCore.Qt.AlignCenter)
        self.softwareName.setObjectName("softwareName")
        self.gridLayout_2.addWidget(self.softwareName, 0, 0, 1, 1)
        self.column = QtWidgets.QTabWidget(self.centralwidget)
        self.column.setAutoFillBackground(False)
        self.column.setStyleSheet("font: 20pt \"Times New Roman\";\n"
"color:  #0C3B40;\n"
"background-color: #63b7af;\n"
"")
        self.column.setObjectName("column")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"Times New Roman\";\n"
"color:  #0C3B40;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.columnNumber = QtWidgets.QLineEdit(self.tab_1)
        self.columnNumber.setStyleSheet(" background-color: #e1f5fe;")
        self.columnNumber.setObjectName("columnNumber")
        self.gridLayout_3.addWidget(self.columnNumber, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget.setStyleSheet(" background-color: #e1f5fe;")
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_3.addWidget(self.tableWidget, 4, 0, 1, 4)
        self.pushButton_start = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_start.setStyleSheet("background-color: #52de97;")
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 2, 2, 1, 1)
        self.pushButton_generate = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_generate.setStyleSheet("background-color: #52de97;")
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.gridLayout_3.addWidget(self.pushButton_generate, 5, 0, 1, 4)
        self.rowNumber = QtWidgets.QLineEdit(self.tab_1)
        self.rowNumber.setStyleSheet(" background-color: #e1f5fe;")
        self.rowNumber.setObjectName("rowNumber")
        self.gridLayout_3.addWidget(self.rowNumber, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setStyleSheet("font: 20pt \"Times New Roman\";\n"
"color:  #0C3B40;\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_stop.setStyleSheet("background-color: #52de97;")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_3.addWidget(self.pushButton_stop, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 3, 2, 1)
        self.column.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("color: rgb(35, 95, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("color: rgb(35, 95, 127);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font-weight: Bold;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.column.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.column, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.column.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.softwareName.setText(_translate("MainWindow", "Staff Asia"))
        self.label.setText(_translate("MainWindow", "Column Number"))
        self.columnNumber.setText(_translate("MainWindow", "7"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_generate.setText(_translate("MainWindow", "Generate Output"))
        self.rowNumber.setText(_translate("MainWindow", "100"))
        self.label_3.setText(_translate("MainWindow", "Row Number"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.label_2.setText(_translate("MainWindow", "Press Start...."))
        self.column.setTabText(self.column.indexOf(self.tab_1), _translate("MainWindow", "CopyAssist"))
        self.label_4.setText(_translate("MainWindow", "Developed by: MD. Shah Imran Shovon"))
        self.label_10.setText(_translate("MainWindow", "Ctrl + q = To stop"))
        self.label_11.setText(_translate("MainWindow", "Ctrl + up = up, Ctrl + down = down, Ctrl + left = left, Ctrl + right = right"))
        self.label_9.setText(_translate("MainWindow", "Ctrl + n = Get down to new row"))
        self.label_8.setText(_translate("MainWindow", "Ctrl + r = Remove Data from a cell"))
        self.label_7.setText(_translate("MainWindow", "Ctrl + z = Previous Cell"))
        self.label_6.setText(_translate("MainWindow", "Ctrl + c = Copy"))
        self.label_5.setText(_translate("MainWindow", "shah_imran_sust@outlook.com"))
        self.label_12.setText(_translate("MainWindow", "Manual :"))
        self.column.setTabText(self.column.indexOf(self.tab_2), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
