from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from DBConnection import DBConnection
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.title = "Data of the Company"
        self.top = 200
        self.left = 200
        self.width = 880
        self.height = 500

        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
 
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
 
        self.creatingTables()
 
 
        self.show()
 
    def creatingTables(self):

        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select sno,date_,open, high, low,close from data")
        rows = cursor.fetchall()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))

        tot=len(rows)
        #print(rows)


 
        self.tableWidget.setItem(0,0, QTableWidgetItem("Sno"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Date"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Open"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("High"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Low"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Close"))

        
        for s in range(tot):
            s0=str(rows[s][0])
            s2=str(rows[s][2])
            s3=str(rows[s][3])
            s4=str(rows[s][4])
            s5=str(rows[s][5])
            

            self.tableWidget.setItem(s+1,0, QTableWidgetItem(s0))
            self.tableWidget.setItem(s+1,1, QTableWidgetItem(rows[s][1]))
            self.tableWidget.setItem(s+1,2, QTableWidgetItem(s2))
            self.tableWidget.setItem(s+1,3, QTableWidgetItem(s3))
            self.tableWidget.setItem(s+1,4, QTableWidgetItem(s4))
            self.tableWidget.setItem(s+1,5, QTableWidgetItem(s5))
        

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
 
        
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
    
    def main(self):
        App = QApplication(sys.argv)
        window = Window()
        sys.exit(App.exec())

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())



