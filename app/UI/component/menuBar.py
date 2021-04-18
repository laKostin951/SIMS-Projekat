import sys

from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide2.QtWidgets import QAction, QMessageBox, QInputDialog

from app.UI.window.select.selectFile import selectFile
from app.assets.config.settings import icon, DEFAULT_DATA_FOLDER


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.file_menu = QtWidgets.QMenu("File", self)
        self.edit_menu = QtWidgets.QMenu("Edit", self)
        self.view_menu = QtWidgets.QMenu("View", self)
        self.help_menu = QtWidgets.QMenu("Help", self)
        self.database_menu = QtWidgets.QMenu("Database", self)

        self.file_menu.setToolTipsVisible(True)
        self.edit_menu.setToolTipsVisible(True)
        self.view_menu.setToolTipsVisible(True)
        self.help_menu.setToolTipsVisible(True)
        self.database_menu.setToolTipsVisible(True)

        self.addMenu(self.file_menu)
        self.addMenu(self.edit_menu)
        self.addMenu(self.view_menu)
        self.addMenu(self.help_menu)
        self.addMenu(self.database_menu)

        # FILE MENU
        # new
        self.newAct = QAction(QIcon(icon.PLUS_MATH_I()), '&New', self)
        self.newAct.setToolTip('Under Construction')
        self.newAct.triggered.connect(self.open_new_table_dialog)
        self.file_menu.addAction(self.newAct)

        # open
        self.openAct = QAction(QIcon(icon.FOLDER_I()), '&Open', self)
        self.openAct.setToolTip('Open file')
        self.openAct.triggered.connect(self.select_file)
        self.file_menu.addAction(self.openAct)

        # save
        self.saveAct = QAction(QIcon(icon.SAVE_I()), '&Save', self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.setToolTip('Saving application')
        # self.saveAct.triggered.connect(self.parent().workspace.save)
        self.file_menu.addAction(self.saveAct)

        # save as new
        self.saveAsAct = QAction(QIcon(icon.SAVE_AS_I()), '&Save As', self)
        self.saveAsAct.setToolTip('Saving application')
        self.saveAsAct.setShortcut('Shift+Ctrl+S')
        # self.saveAct.triggered.connect(self.parent().workspace.save_as)
        self.file_menu.addAction(self.saveAsAct)

        # save all
        self.saveAllAct = QAction(QIcon(icon.SAVE_ALL_I()), '&Save All', self)
        self.saveAllAct.setToolTip('Saving application')
        # self.saveAllAct.triggered.connect(self.parent().workspace.save_all)
        self.file_menu.addAction(self.saveAllAct)

        # app shutdown
        self.exitAct = QAction(QIcon(icon.SHUTDOWN_I()), '&Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setToolTip('Exit application')
        self.exitAct.triggered.connect(self.close_application)
        self.file_menu.addAction(self.exitAct)

        # EDIT MENU
        # copy
        self.copyAct = QAction(QIcon(icon.COPY_I()), '&Copy', self)
        self.copyAct.triggered.connect(self.show_popup)
        self.copyAct.setToolTip('Under Construction')
        self.edit_menu.addAction(self.copyAct)

        # paste
        self.pasteAct = QAction(QIcon(icon.PASTE_I()), '&Paste', self)
        self.pasteAct.triggered.connect(self.show_popup)
        self.pasteAct.setToolTip('Under Construction')
        self.edit_menu.addAction(self.pasteAct)

        # cut
        self.cutAct = QAction(QIcon(icon.CUT_I()), '&Cut', self)
        self.cutAct.triggered.connect(self.show_popup)
        self.cutAct.setToolTip('Under Construction')
        self.edit_menu.addAction(self.cutAct)

        # find
        self.findAct = QAction(QIcon(icon.SEARCH_MORE_I()), '&Find', self)
        self.findAct.triggered.connect(self.show_dialog)
        self.findAct.setToolTip('Quick search')
        self.edit_menu.addAction(self.findAct)

        # back
        self.backAct = QAction(QIcon(icon.UNDO_I()), '&Back', self)
        # self.backAct.triggered.connect(self.parent().workspace.reset_tables)
        self.backAct.setToolTip('Go one step back')
        self.edit_menu.addAction(self.backAct)

        # forward
        self.forwardAct = QAction(QIcon(icon.REDO_I()), '&Forward', self)
        self.forwardAct.triggered.connect(self.show_popup)
        self.forwardAct.setToolTip('Go one step forward')
        self.edit_menu.addAction(self.forwardAct)

        # VIEW
        self.viewAct = QAction(QIcon('assets/img/print.png'), '&Print Preview', self)
        self.viewAct.setStatusTip('Under Construction')
        self.viewAct.triggered.connect(self.print_preview_dialog)
        self.view_menu.addAction(self.viewAct)

        # DATABASE
        # crate new connection
        self.new_conn_act = QAction(QIcon(icon.PLUS_MATH_I()), '&New connection', self)
        self.new_conn_act.setToolTip('Under Construction')
        self.new_conn_act.triggered.connect(self.print_preview_dialog)
        self.database_menu.addAction(self.new_conn_act)

        # all saved connections
        # connections = Connections().connections
        # self.database_menu.addSeparator()
        # for saved_connection in connections:
        #    saved_connections_act = QAction(QIcon(icon.RESET_I()), "aved_connection.connection-name", self)
        #    saved_connections_act.setToolTip('Under Construction')
        #    saved_connections_act.triggered.connect(self.print_preview_dialog)
        #    self.database_menu.addAction(self.new_conn_act)

        # self.database_menu.addSeparator()

        # delete all saved connection
        self.clear_conn_act = QAction(QIcon(icon.CLEAR_SYMBOL_I()), '&Clear', self)
        self.clear_conn_act.setToolTip("Clear ALL cached connections")
        self.clear_conn_act.triggered.connect(self.print_preview_dialog)
        self.database_menu.addAction(self.clear_conn_act)


        # HELP MENU
        # about
        self.aboutAct = QAction(QIcon('assets/img/about.jpg'), '&About', self)
        self.aboutAct.setToolTip('Under Construction')
        self.aboutAct.triggered.connect(self.show_popup)
        self.help_menu.addAction(self.aboutAct)

    def close_application(self):
        # TODO : Save All Question
        choice = QtWidgets.QMessageBox.question(self, 'Closing menu', 'Do you want to exit the application ?',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            print("Closing the application.")
            sys.exit()
        else:
            pass

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Fatal Error")
        msg.setText("Post Error! error code = 503")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Under Contructions!")
        msg.setDetailedText("This command isnt currently working pleas stand by untill we finish the contructions")

        execute = msg.exec_()

    def select_file(self):
        path = selectFile(self, "Open file", DEFAULT_DATA_FOLDER, "*.csv", print)

    def show_dialog(self):
        text = QInputDialog.getText(self, 'Input Dialog', "Quick Search:")
        self.parent().workspace.find(text)

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()

    def print_preview(self, printer):
        self.textEdit.print_(printer)

    def open_new_table_dialog(self):
        extra_window = ExtraWindow(self)
