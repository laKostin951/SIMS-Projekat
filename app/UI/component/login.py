import sys
import json
import os
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)

class Login(QDialog):
    korisnik = {
        "username": "",
        "password": "",
        "level": 0,
    }

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        # Create widgets
        self.user = QLineEdit("username")
        self.password = QLineEdit("password")
        self.button = QPushButton("Login")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.user)
        layout.addWidget(self.password)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal
        self.button.clicked.connect(self.Prijava())
        
    def Prijava(self):
        self.korisnik['username'] = self.user.text()
        self.korisnik['password'] = self.password.text()
        dirname = os.path.dirname(os.path.abspath(__file__))
        filedir = os.path.dirname(dirname)
        filename = os.path.join(filedir, "data\\korisnici.json")
        with open(filename ,encoding="UTF-8") as f:
            reader = json.load(f)
            for i in reader:
                if korisnik["username"] == i["username"] and korisnik["password"] == i["password"]:
                    return i
        return [""]

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Login()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())