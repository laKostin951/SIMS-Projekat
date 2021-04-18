from PySide2.QtWidgets import QTabWidget

from app.UI.component.tableWorkspace.table import Table
from app.UI.component.tableWorkspace.tableWorkspace import TableWorkspace

from app.src.file.module.path import Path
from app.src.file.module.meta import MetaData
from app.src.file.tableModel import TableModel


class MainWorkspace(QTabWidget):
    """
    Widget that contains all workspaces with open files or eny other workspace
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.setTabsClosable(True)

    def is_file_open(self, file_path): ...
        # TODO : Proci kroz sve tabove i proveriti
    #  da li je u tom tabu otvoren fajl sa proseldjenim putanjom

    def open_file(self, file_path):

        file_path_c = Path(file_path)
        metadata_c = MetaData(file_path_c.metadata_path, file_path)

        table_workspace = TableWorkspace(self, Table(self, file_path_c, metadata_c))

        self.addTab(table_workspace, file_path_c.clear_file_name)
