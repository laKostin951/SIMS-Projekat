from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog

from app.assets.config.settings import DEFAULT_DATA_FOLDER


class Select(QFileDialog):
    def __init__(self, parent=None, title="Select file",  folder=DEFAULT_DATA_FOLDER, name_filter="*"):
        super().__init__(parent, title, folder, name_filter)
        self.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)


def selectFile(parent=None, title="Select file",  folder=DEFAULT_DATA_FOLDER, name_filter="*", callback=None):
    dialog = Select(parent, title, folder, name_filter)
    dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)

    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        file_path = dialog.selectedFiles()[0]
        if callback is not None:
            return callback(file_path)
        return file_path


def selectFiles(parent=None, title="Select file",  folder=DEFAULT_DATA_FOLDER, name_filter="*", callback=None):
    dialog = Select(parent, title, folder, name_filter)
    dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        file_path = dialog.selectedFiles()
        if callback is not None:
            return callback(file_path)
        return file_path
