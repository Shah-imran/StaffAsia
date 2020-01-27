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
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # connect the two functions
        self.pushButton.clicked.connect(self.return_cancel)
        self.pushButton_2.clicked.connect(self.return_accept)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.dialoglabel.setText(_translate("Dialog", "<b>Are you sure? <br>You may lose the data if you choose to low value!</b>"))
        self.pushButton_2.setText(_translate("Dialog", "Yes"))
        self.pushButton.setText(_translate("Dialog", "No"))

    # 2 sample functions
    def return_accept(self):
        print("yes")
        return 1
    def return_cancel(self):
        print("no")
        return 0

    def closeEvent(self):
        print("Close Event")

def main():
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.exec_()
    dialog.show()