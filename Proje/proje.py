import sys 
from PyQt6.QtWidgets import * 
from typing_extensions import Self
from ui_form import Ui_MainWindow 


class Anaform(Ui_MainWindow,QMainWindow):
     def __init__(self, *args, **kwargs):
        super(Anaform, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.ekle)
        self.pushButton_2.clicked.connect(self.sil)
        
        
     def ekle(self):
         x=self.lineEdit.text()
         y=self.lineEdit_2.text()
         z=self.lineEdit_3.text()
         m=self.lineEdit_4.text()
         self.listWidget.addItem(x)
         self.listWidget.addItem(y)
         self.listWidget.addItem(z)
         self.listWidget.addItem(m)
         self.comboBox.addItem(x)
         self.comboBox.addItem(y)
         self.comboBox.addItem(z)
         self.comboBox.addItem(m)
         
     def sil(self):
        self.listWidget.clear()
        self.comboBox.clear()           
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()




proje = QApplication(sys.argv)
form = Anaform()
form.show()
sys.exit(proje.exec())
 