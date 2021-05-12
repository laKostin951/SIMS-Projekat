import csv
import os
from abc import ABC
from collections import Counter

from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QDir
from PySide2.QtGui import QFont, QIcon
from dataHandler.dataExtras.abstract_table_model import AbstractTableModel
from dataHandler.dataExtras.metadata import MetaData
from dataHandler.dataExtras.path import Path


class File(AbstractTableModel, ABC):
    def __init__(self, path_c, auto_load=True, metadata_c=None, structure_dock=None):
        super().__init__()
        self.structure_dock = structure_dock
        if metadata_c is None:
            self.metadata_c = MetaData(path_c.get_metadata_path(), path_c)
        else:
            self.metadata_c = metadata_c

        self.path_c = path_c
        self.data = []

        if auto_load:
            self.load()

    def __getitem__(self, index):
        return self.data[0]


def load(self, file=None):
        try:
            data_file = open(self.path_c.path, 'r')

            reader = csv.DictReader(data_file,
                                    delimiter=self.metadata_c.metadata["dialect"]["delimiter"],
                                    fieldnames=self.metadata_c.get_headers_names(),
                                    quoting=self.metadata_c.metadata["dialect"]["quoting"])

            if self.metadata_c.metadata["dialect"]["skip_first_line"]:
                next(reader)

            for row in reader:
                self.data.append(row)

            data_file.close()
            del reader

        except:
            
            return

        return self.data
def save(self):
        with open(self.path_c.path, 'w') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=self.metadata_c.get_headers_names(),
                                    delimiter=self.metadata_c.metadata["dialect"]["delimiter"],
                                    quoting=self.metadata_c.metadata["dialect"]["quoting"])

            writer.writerows(self.data)

def delete(self, index):
        del self.data[index]