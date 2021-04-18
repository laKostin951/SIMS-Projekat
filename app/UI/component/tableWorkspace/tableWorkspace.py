from PySide2.QtWidgets import QWidget, QHBoxLayout

from app.UI.component.tableWorkspace.table import Table
from app.src.file.tableModel import TableModel


class TableWorkspace(QWidget):
    """
    Widget that contain table with all records from serial file,
    and all necessary tools for working with that records .

    Can be used as single table in more complex relational file system,
    for that usage, some of tools from toolbar must be re implement or added

    :param table: The table we want to work with
    """
    def __init__(self, parent: QWidget, table: Table):
        super().__init__(parent)
        self.table = table

        self.horizontal_layout = QHBoxLayout()

        self.horizontal_layout.addWidget(self.table)

        self.setLayout(self.horizontal_layout)


