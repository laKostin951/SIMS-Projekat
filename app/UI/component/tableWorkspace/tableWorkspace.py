from PySide2.QtWidgets import QWidget, QHBoxLayout, QIcon, QToolbar, QMenu, QMenuBar, QAction

from app.UI.component.tableWorkspace.table import Table
from app.src.file.tableModel import TableModel
from app.assets.config import icon

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


    def _createActions(self):
        self.newAction = QAction(QIcon(icon.ADD_FILE_I()), "&New", self)
        self.openAction = QAction(QIcon(icon.FOLDER_I()), "&Open", self)
        self.printAction = QAction(QIcon(icon.PRINT_I()), "&Print", self)

        self.addAction(self.newAction)
        self.addAction(self.openAction)
        self.addAction(self.printAction)

        self.addSeparator()

        self.newAction.setStatusTip('New file')
        self.openAction.setStatusTip('Open file')
        self.printAction.setStatusTip('Print file')

        self.newAction.triggered.connect(self.open_new_table_dialog)
        self.openAction.triggered.connect(self.open_dialog_box)
        self.printAction.triggered.connect(self.print_preview_dialog)