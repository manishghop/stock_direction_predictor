# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Stock2020\userhome2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Prediction import Prediction


class userhome2(object):

    def predictdef(self):
        try:
            
            tstart = float(self.todaystart.text())
            print(tstart)
            st = float(self.start.text())
            print(st)
            ma = float(self.max.text())
            print(ma)
            cl = float(self.close.text())
            print(cl)
            s_m = st - ma
            s_c = st - cl
            diff = (tstart - st)

            if True:
                import csv
                row1=[diff,s_m,s_c]
                row=['diff','s_m','s_c']


                with open('test.csv', 'w') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                    writer.writerow(row1)
                    
                csvFile.close()
                res = Prediction.predict_nv()
                self.showAlertBox("Alert", "Result is " + str(res))
                self.label_9.setText(res.upper())
        


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()



    def setupUi(self, today):
        today.setObjectName("today")
        today.resize(415, 620)
        today.setMaximumSize(QtCore.QSize(16777215, 16777215))
        today.setStyleSheet("background-color: rgb(12, 190, 135);")
        self.label = QtWidgets.QLabel(today)
        self.label.setGeometry(QtCore.QRect(-240, 40, 901, 71))
        self.label.setStyleSheet("color: rgb(109, 109, 109);\n"
"font: 20pt \"Gungsuh\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(today)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 291, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(today)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 110, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(today)
        self.label_4.setGeometry(QtCore.QRect(60, 260, 131, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(today)
        self.label_5.setGeometry(QtCore.QRect(60, 300, 131, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_5.setObjectName("label_5")
        self.start = QtWidgets.QDoubleSpinBox(today)
        self.start.setGeometry(QtCore.QRect(200, 220, 120, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setMaximumSize(QtCore.QSize(120, 22))
        self.start.setMaximum(990000.0)
        self.start.setObjectName("start")
        self.max = QtWidgets.QDoubleSpinBox(today)
        self.max.setGeometry(QtCore.QRect(200, 260, 120, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max.sizePolicy().hasHeightForWidth())
        self.max.setSizePolicy(sizePolicy)
        self.max.setMaximumSize(QtCore.QSize(120, 22))
        self.max.setMaximum(990000.0)
        self.max.setObjectName("max")
        self.close = QtWidgets.QDoubleSpinBox(today)
        self.close.setGeometry(QtCore.QRect(200, 300, 120, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setMaximumSize(QtCore.QSize(120, 22))
        self.close.setMaximum(990000.0)
        self.close.setObjectName("close")
        self.todaystart = QtWidgets.QDoubleSpinBox(today)
        self.todaystart.setGeometry(QtCore.QRect(200, 430, 120, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todaystart.sizePolicy().hasHeightForWidth())
        self.todaystart.setSizePolicy(sizePolicy)
        self.todaystart.setMaximumSize(QtCore.QSize(120, 22))
        self.todaystart.setMaximum(990000.0)
        self.todaystart.setObjectName("todaystart")
        self.label_6 = QtWidgets.QLabel(today)
        self.label_6.setGeometry(QtCore.QRect(10, 370, 291, 51))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(today)
        self.label_7.setGeometry(QtCore.QRect(60, 430, 110, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(today)
        self.label_8.setGeometry(QtCore.QRect(20, 520, 91, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(today)
        self.label_9.setGeometry(QtCore.QRect(110, 520, 251, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Levenim MT\";")
        self.label_9.setObjectName("label_9")
        self.predict = QtWidgets.QPushButton(today)
        self.predict.setGeometry(QtCore.QRect(270, 480, 120, 30))
        self.predict.setObjectName("predict")

        self.predict.clicked.connect(self.predictdef)

        self.retranslateUi(today)
        QtCore.QMetaObject.connectSlotsByName(today)

    def retranslateUi(self, today):
        _translate = QtCore.QCoreApplication.translate
        today.setWindowTitle(_translate("today", "Dialog"))
        self.label.setText(_translate("today", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Predicting Daily</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Return of Stock Market Direction</span></p></body></html>"))
        self.label_2.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Enter Last Day Details</span></p></body></html>"))
        self.label_3.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:14pt;\">Start Price:</span></p></body></html>"))
        self.label_4.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:14pt;\">Max Price:</span></p></body></html>"))
        self.label_5.setText(_translate("today", "Close Price:"))
        self.label_6.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Enter Today Details</span></p></body></html>"))
        self.label_7.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:14pt;\">Start Price:</span></p></body></html>"))
        self.label_8.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#d63110;\">Result:</span></p></body></html>"))
        self.label_9.setText(_translate("today", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ebf434;\">Non</span></p></body></html>"))
        self.predict.setText(_translate("today", "Predict"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    today = QtWidgets.QDialog()
    ui = userhome2()
    ui.setupUi(today)
    today.show()
    sys.exit(app.exec_())
