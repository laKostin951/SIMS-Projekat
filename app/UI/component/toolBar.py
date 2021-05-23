from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide2.QtWidgets import QAction, QFileDialog, QMenu, QToolBar, QIcon, QCheckBox

from app import icon
from app import config
class Toolbar(MainWindow):
        def _createToolBars(self):
                fileToolBar = self.addToolBar("File")
                fileToolBar.addAction(self.copyAction)
                fileToolBar.addAction(self.saveAction)
                fileToolBar.addAction(self.deleteAction)
                fileToolBar.addAction(self.filterAction)
                #editToolBar = QToolBar("Edit", self)                
                #self.addToolBar(editToolBar)                        ako zatreba
                #helpToolBar = QToolBar("Help", self)                
                #self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

        def _createMenuBar(self):
                menuBar = self.menuBar()
                fileMenu = QMenu("&File", self)
                menuBar.addMenu(fileMenu)
                fileMenu.addAction(self.addFileAction)
                fileMenu.addAction(self.saveAction)
                fileMenu.addAction(self.copyAction)
                fileMenu.addAction(self.deleteAction)
                editMenu = menuBar.addMenu("&Edit")

        def _createActions(self):
                #self.QAction(icon, text, parent)       <- sablon za pravljenje klasa
                self.saveAction(QIcon(SAVE_I()),"&Save", self)
                self.addFileAction(QIcon(ADDFILE_I()),"&AddFIle", self)
                self.copyAction(QIcon(COPY_I()),"&Copy", self)
                self.deleteAction(QIcon(DELETE_I()),"&Delete", self)
                self.filterAction(QIcon(FILTER_I()),"&Filter", self)
        #def _connectActions(self):
                #self.saveAction.triggered.connect(save)        treba povezati
                #self.filterAction.triggered.connect(FilterWindow())

        def __init__(self, parent=None):
                self._createActions()
                self._createMenuBar()
                self._createToolBars()
                #self._connectActinos()