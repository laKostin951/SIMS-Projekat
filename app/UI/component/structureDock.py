from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QVBoxLayout, QWidget

from app.UI.component.fileSystem.fileSystem import FileSystem
from app.assets.config.settings import DEFAULT_DATA_FOLDER


class StructureDock(QtWidgets.QDockWidget):
    clicked = QtCore.Signal(str)
    #sql_clicked = QtCore.Signal(str, bool, bool, str)

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.main_widget = QWidget(self)
        self.main_v_layout = QVBoxLayout()

        self.file_system = FileSystem(self.file_clicked, DEFAULT_DATA_FOLDER)

        self.main_v_layout.addWidget(self.file_system)

        self.main_widget.setLayout(self.main_v_layout)
        self.setWidget(self.main_widget)

    def file_clicked(self, path):
        self.clicked.emit(path)

    def sql_table_file_clicked(self, path): ...
        #self.sql_clicked.emit(None, False, True, path)
