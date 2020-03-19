# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Stock2020\home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from signup import Signup
from userhome import UserHome
from userloginaction import UserLoginCheck


class Home(object):
    def userlogin(self):
        try:
            print("ulogin")
            uid = self.uid.text()
            upwd = self.upwd.text()
            self.uid.setText("")
            self.upwd.setText("")
            ul = UserLoginCheck()
            res = ul.datacheck(uid, upwd)
            if res:
                self.showAlertBox("Alert", "Fill the Fields")
            elif UserLoginCheck.logincheck(uid, upwd):
                self.uu = QtWidgets.QMainWindow()
                self.uui = UserHome()
                self.uui.setupUi(self.uu)
                self.uu.show()
                print('userhome')
            else:
                self.showAlertBox("Login Alert", "Login Fail")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def signup(self):
        try:
            name = self.rname.text()
            email = self.remail.text()
            ph = self.rph.text()
            pwd = self.rpwd.text()

            if Signup.datacheck(name, email, ph, pwd):
                Signup.store(name, email, ph, pwd)
                self.showAlertBox("Registration", "Registration Success")
            else:
                print("")
                self.showAlertBox("Alert ", "Please Fill the Fields")
            self.remail.setText("")
            self.rpwd.setText("")
            self.rph.setText("")
            self.rname.setText("")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

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
        Dialog.setStyleSheet("background-color: rgb(252, 236, 99);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 941, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 941, 601))
        self.tableView.setStyleSheet("background-image: url(stock-market.jpg);")
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.uid = QtWidgets.QLineEdit(self.tab_2)
        self.uid.setGeometry(QtCore.QRect(310, 240, 370, 50))
        self.uid.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                               "color: rgb(58, 58, 58);\n"
                               "border-color: rgb(48, 48, 48);\n"
                               "")
        self.uid.setText("")
        self.uid.setObjectName("uid")
        self.upwd = QtWidgets.QLineEdit(self.tab_2)
        self.upwd.setGeometry(QtCore.QRect(310, 300, 370, 50))
        self.upwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                "color: rgb(58, 58, 58);\n"
                                "border-color: rgb(48, 48, 48);\n"
                                "selection-background-color: rgb(66, 66, 66);\n"
                                "border-right-color: rgb(106, 106, 106);\n"
                                "gridline-color: rgb(86, 86, 86);")
        self.upwd.setText("")
        self.upwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.upwd.setObjectName("upwd")
        self.ulogin = QtWidgets.QPushButton(self.tab_2)
        self.ulogin.setGeometry(QtCore.QRect(310, 370, 190, 40))
        self.ulogin.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                  "color: rgb(58, 58, 58);\n"
                                  "border-color: rgb(48, 48, 48);\n"
                                  "selection-background-color: rgb(66, 66, 66);\n"
                                  "border-right-color: rgb(106, 106, 106);\n"
                                  "gridline-color: rgb(86, 86, 86);")
        self.ulogin.setObjectName("ulogin")

        ##########################  
        self.ulogin.clicked.connect(self.userlogin)
        ########################

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 441, 81))
        self.label_3.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                   "color: rgb(255, 251, 248);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(60, 20, 821, 91))
        self.label.setStyleSheet("color: rgb(109, 109, 109);\n"
                                 "font: 20pt \"Gungsuh\";")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.rph = QtWidgets.QLineEdit(self.tab_3)
        self.rph.setGeometry(QtCore.QRect(320, 290, 360, 40))
        self.rph.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                               "color: rgb(58, 58, 58);\n"
                               "border-color: rgb(48, 48, 48);\n"
                               "")
        self.rph.setText("")
        self.rph.setObjectName("rph")
        self.remail = QtWidgets.QLineEdit(self.tab_3)
        self.remail.setGeometry(QtCore.QRect(320, 340, 360, 40))
        self.remail.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                  "color: rgb(58, 58, 58);\n"
                                  "border-color: rgb(48, 48, 48);\n"
                                  "")
        self.remail.setText("")
        self.remail.setObjectName("remail")
        self.rpwd = QtWidgets.QLineEdit(self.tab_3)
        self.rpwd.setGeometry(QtCore.QRect(320, 390, 360, 40))
        self.rpwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                "color: rgb(58, 58, 58);\n"
                                "border-color: rgb(48, 48, 48);\n"
                                "")
        self.rpwd.setText("")
        self.rpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rpwd.setObjectName("rpwd")
        self.rname = QtWidgets.QLineEdit(self.tab_3)
        self.rname.setGeometry(QtCore.QRect(320, 240, 360, 40))
        self.rname.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                 "color: rgb(58, 58, 58);\n"
                                 "border-color: rgb(48, 48, 48);\n"
                                 "")
        self.rname.setText("")
        self.rname.setObjectName("rname")
        self.ulogin_2 = QtWidgets.QPushButton(self.tab_3)
        self.ulogin_2.setGeometry(QtCore.QRect(320, 440, 150, 40))
        self.ulogin_2.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                    "color: rgb(58, 58, 58);\n"
                                    "border-color: rgb(48, 48, 48);\n"
                                    "")
        self.ulogin_2.setObjectName("ulogin_2")
        self.ulogin_2.clicked.connect(self.signup)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 821, 91))
        self.label_2.setStyleSheet("color: rgb(109, 109, 109);\n"
                                   "font: 20pt \"Gungsuh\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 441, 81))
        self.label_4.setStyleSheet("font: 14pt \"Levenim MT\";\n"
                                   "color: rgb(255, 251, 248);")
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.uid.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.upwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.ulogin.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0d0d0d;\">User Login</span></p></body></html>"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\">Predicting Daily Return of Stock Market Direction</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "User"))
        self.rph.setPlaceholderText(_translate("Dialog", "Enter Contact"))
        self.remail.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.rpwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.rname.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.ulogin_2.setText(_translate("Dialog", "Register"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\">Predicting Daily Return of Stock Market Direction</p></body></html>"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0d0d0d;\">User Register Here</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "SignUp"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
