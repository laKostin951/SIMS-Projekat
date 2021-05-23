from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

class FilterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Filter")
        self.setGeometry(300,200,400,100)
 
        self.createCheckBox()
 
        self.show()
    
    def createCheckBox(self):
        vbox = QVBoxLayout()
 
        check = QCheckBox("Opcija", self)
        check.stateChanged.connect(self.checkBoxChange)
        check.toggle()
 
        vbox.addWidget(check)
        vbox.addWidget(self.label)
 
        self.setLayout(vbox)
 
 
    izabraniFilteri = []
    def checkBoxChange(self, state, text):
        if state == Qt.Checked:
            izabraniFilteri += text