from PySide2.QtWidgets import QTableView

from app.src.file.tableModel import TableModel
from app.src.file.module.path import Path
from app.src.file.module.meta import MetaData


class Table(QTableView):
    """
    Table widget which show all records from opened file

    :param file_path_c :type Path: Created object 'Path' with path to the desired file

    :param metadata_c :type MetaData: Created object 'MetaData' with metadata for desired file
    """
    def __init__(self, parent, file_path_c: Path, metadata_c: MetaData):
        super().__init__(parent)
        self.model_c = TableModel(file_path_c, metadata_c)

        self.setModel(self.model_c)

