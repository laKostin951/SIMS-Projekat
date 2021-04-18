from PySide2 import QtWidgets, QtGui, QtCore

from app.UI.component.menuBar import MenuBar
from app.UI.component.statusBar import StatusBar
from app.UI.component.structureDock import StructureDock
from app.UI.component.toolBar import ToolBar
from app.UI.component.workspace.mainWorkSpace import MainWorkspace
from app.assets.style import STYLES


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(STYLES.filter_line_edit)

        self.resize(600, 480)
        self.setWindowTitle("Editor generickih podataka")
        self.setWindowIcon(QtGui.QIcon("../assets/img/icons8-edit-file-64.png"))

        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        self.structure_dock = StructureDock("Structure dock", self)

        self.main_workspace = MainWorkspace(self)

        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.toggle_structure_dock_action = self.structure_dock.toggleViewAction()
        self.menu_bar.view_menu.addAction(self.toggle_structure_dock_action)

        self.structure_dock.clicked.connect(self.main_workspace.open_file)
        #self.structure_dock.sql_clicked.connect(self.workspace.open_file)

        self.tool_bar = ToolBar()
        self.addToolBar(self.tool_bar)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)
        self.setCentralWidget(self.main_workspace)

        self.show()
