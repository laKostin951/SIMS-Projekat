import time
import csv

from PySide2 import QtCore
from PySide2.QtCore import Qt

from app.src.file.module.path import Path
from app.src.file.module.meta import MetaData


class TableModel(QtCore.QAbstractTableModel):
    """
    Table data model

    :param file_path_c :type Path: Created object 'Path' with path to the desired file

    :param metadata_c :type MetaData: Created object 'MetaData' with metadata for desired file

    :param load :type bool: Load records when creating this object,
     or leave records to be loaded by calling a function ' load_records '
    """

    def __init__(self, file_path_c: Path, metadata_c: MetaData, load: bool = True):
        super(TableModel, self).__init__()
        self.metadata_c = metadata_c
        self.file_path_c = file_path_c

        self.records = []
        if load:
            self.load_records()

    def data(self, index, role=None):
        if not index.isValid():
            return None
        # QModelIndex index = model->index(row, column, parent);
        if role == Qt.DisplayRole:
            return self.records[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid():
            return value

    def headerData(self, section, orientation, role=None):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.metadata_c.metadata["headers"][section]["name"]

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.records)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.records[0])

    def load_records(self):
        with open(self.file_path_c.path) as file:
            records = csv.reader(file,
                                 delimiter=self.metadata_c.metadata["dialect"]["delimiter"],
                                 quoting=self.metadata_c.metadata["dialect"]["quoting"])
            for row in records:
                self.records.append(row)
