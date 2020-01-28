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
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_3.addWidget(self.tableWidget, 4, 0, 1, 4)
        self.pushButton_start = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_start.setStyleSheet("background-color: #52de97;")
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 2, 2, 1, 1)
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
        self.gridLayout_3.addWidget(self.label_2, 6, 0, 1, 4)
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
        self.column.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
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
        self.label_2.setText(_translate("MainWindow", "First Put the column names then press Start button to start copy assisting!"))
        self.pushButton_generate.setText(_translate("MainWindow", "Generate Output"))
        self.rowNumber.setText(_translate("MainWindow", "1000"))
        self.label_3.setText(_translate("MainWindow", "Row Number"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.column.setTabText(self.column.indexOf(self.tab_1), _translate("MainWindow", "CopyAssist"))
        self.column.setTabText(self.column.indexOf(self.tab_2), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
