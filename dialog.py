from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 126)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dialoglabel = QtWidgets.QLabel(Dialog)
        self.dialoglabel.setObjectName("dialoglabel")
        self.horizontalLayout_3.addWidget(self.dialoglabel)
        self.dialoglabel.setStyleSheet("font: 20pt \"Times New Roman\";\n"
"color:  #0C3B40;\n"
"background-color: #c0ffb3;\n"
"")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.dialoglineedit = QtWidgets.QLineEdit(Dialog)
        # self.dialoglineedit.setObjectName("dialoglineedit")
        # self.horizontalLayout_2.addWidget(self.dialoglineedit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: #52de97;")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #52de97;")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # connect the two functions
        self.pushButton.clicked.connect(Dialog.reject)
        self.pushButton_2.clicked.connect(Dialog.accept)
        # self.finished.connect(self.return_accept)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        html = '''<center><b>Are you sure?
        <br>You may lose the data if you choose too low value!</b></center>
        '''
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.dialoglabel.setText(_translate("Dialog", html))
        self.pushButton_2.setText(_translate("Dialog", "Yes"))
        self.pushButton.setText(_translate("Dialog", "No"))

def main():
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    return dialog.exec_()