# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Stock2020\userhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import os
import sys
from PyQt5.QtGui import QIcon
from userhome2 import userhome2
from GetData import GetData


di={}
f=open('names.txt','r')
for i in f:
	a,b=i.split("------->")
	di[a]=b


class UserHome(QWidget):
    def help(self):
        files = (os.listdir('ETFs'))
        # print(files)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.clear()
        for f in files:
            f = f.split('.')
            self.listWidget.addItem(f[0]+" "+di[f[0]]+" ")

    def prediction(self):
        companyname = self.company.text()


        GetData.main(companyname)
        self.showAlertBox("Done ", "Dataset Prepared Successfully")
        import subprocess
        import sys

        # Some code here

        pid = subprocess.Popen([sys.executable, "table.py"])

        self.uu = QtWidgets.QMainWindow()
        self.uui = userhome2()
        self.uui.setupUi(self.uu)
        self.uu.show()
        print('userhome')

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(938, 620)
        Dialog.setStyleSheet("background-color: rgb(12, 190, 135);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 951, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.tableView = QtWidgets.QTableView(self.tabWidgetPage1)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 941, 511))
        self.tableView.setStyleSheet("background-image: url(stock.jpg);")
        self.tableView.setObjectName("tableView")
        self.label_3 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 311, 51))
        self.label_3.setStyleSheet("color: rgb(109, 109, 109);\n"
                                   "font: 20pt \"Gungsuh\";")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.listWidget = QtWidgets.QListWidget(self.tabWidgetPage2)
        self.listWidget.setGeometry(QtCore.QRect(540, 50, 381, 411))
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"Rod\";")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 381, 51))
        self.label_2.setStyleSheet("color: rgb(109, 109, 109);\n"
                                   "font: 20pt \"Gungsuh\";")
        self.label_2.setObjectName("label_2")
        self.company = QtWidgets.QLineEdit(self.tabWidgetPage2)
        self.company.setGeometry(QtCore.QRect(10, 80, 350, 40))
        self.company.setStyleSheet("font: 12pt \"Levenim MT\";\n"
                                   "color: rgb(255, 255, 255);")
        self.company.setObjectName("company")
        self.pushButton = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton.setGeometry(QtCore.QRect(180, 130, 180, 30))
        self.pushButton.setStyleSheet("background-color: rgb(173, 173, 173);\n"
                                      "font: 12pt \"Courier\";\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 470, 120, 20))
        self.pushButton_2.setStyleSheet("background-color: rgb(173, 173, 173);\n"
                                        "font: 12pt \"Courier\";\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        ##########################  
        self.pushButton_2.clicked.connect(self.help)
        ##################################################  
        self.pushButton.clicked.connect(self.prediction)
        ########################

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 901, 51))
        self.label.setStyleSheet("color: rgb(109, 109, 109);\n"
                                 "font: 20pt \"Gungsuh\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Home"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; color:#f9f9f9;\">Welcome User..</span></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("Dialog", "Home"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "Click on Help"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; color:#f9f9f9;\">Enter Company Code</span></p><p><span style=\" font-size:14pt; color:#f9f9f9;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Prediction "))
        self.pushButton_2.setText(_translate("Dialog", "Help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("Dialog", "Stock Prediction"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\">Predicting Daily Return of Stock Market Direction</p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
