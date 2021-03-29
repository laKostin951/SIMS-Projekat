import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QScrollArea, QPushButton, QWidget

from app.assets.config.settings import icon, HEIGHT
from app.assets.style import STYLES


class FileSystem(QWidget):
    def __init__(self, open_file_callback, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self.open_file_callback = open_file_callback

        self.setStyleSheet(STYLES.file_path_button)
        self.setMaximumHeight(HEIGHT)

        self.v_layout = QVBoxLayout()

        self.area = QScrollArea(self)
        self.area.setWidgetResizable(True)

        self.refresh_btn = QPushButton(QIcon(icon.RESET_I()), '', self)
        self.refresh_btn.clicked.connect(self.refresh)

        self.v_layout.addWidget(self.refresh_btn)
        self.v_layout.addWidget(self.area)

        self.set_scroll_area()

        self.setLayout(self.v_layout)

    def refresh(self):
        w = self.area.widget()
        w.setParent(None)
        del w
        self.set_scroll_area()

    def set_scroll_area(self):

        scroll_content = QWidget(self.area)
        scroll_layout = QVBoxLayout(scroll_content)

        scroll_content.setLayout(scroll_layout)

        for file in sorted(os.listdir(self.folder_path)):
            file_absolute_path = self.folder_path + os.path.sep + file

            if os.path.isdir(file_absolute_path):
                scroll_layout.addWidget(Folder(scroll_content,
                                               self.open_file_callback,
                                               self.folder_path + os.path.sep + file))
                continue

            if os.path.splitext(file_absolute_path)[1] != '.csv':
                continue

            scroll_layout.addWidget(FilePathButton(scroll_content,
                                                   file,
                                                   file_absolute_path,
                                                   self.open_file_callback))

        scroll_layout.addStretch(1)

        self.area.setWidget(scroll_content)


class FilePathButton(QWidget):
    def __init__(self, parent, file_name: str, file_path: str, callback):
        super().__init__(parent)
        self.file_path = file_path
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.v_layout.setSpacing(0)
        self.v_layout.setMargin(0)

        file_icon = QIcon(icon.TABLE_I())

        self.btn = QPushButton(file_icon, file_name, self)
        self.btn.clicked.connect(self.send_file_path_signal)

        self.v_layout.addWidget(self.btn)
        self.setLayout(self.v_layout)

    def send_file_path_signal(self) -> None:
        self.callback(self.file_path)


class Folder(QWidget):
    def __init__(self, parent, open_file_call, folder_path):
        super().__init__(parent)
        self.folder_path = folder_path
        self.folder_open = False

        self.setStyleSheet(STYLES.file_path_button)

        self.main_v_layout = QVBoxLayout()
        self.main_v_layout.setSpacing(2)
        self.main_v_layout.setMargin(0)

        self.files = QWidget(self)
        self.files.hide()
        self.files.setStyleSheet(STYLES.files_list)
        self.files.setContentsMargins(15, 0, 0, 0)
        self.files_v_layout = QVBoxLayout()

        self.folder_btn = QPushButton(QIcon(icon.FOLDER_I()),
                                      self.folder_path.split(os.path.sep)[-1],
                                      self)
        self.folder_btn.clicked.connect(self.open_folder)

        self.main_v_layout.addWidget(self.folder_btn)

        for file in sorted(os.listdir(self.folder_path)):
            file_absolute_path = f'app{os.path.sep}{self.folder_path}{os.path.sep}{file}'

            if os.path.isdir(file_absolute_path):
                self.files_v_layout.addWidget(Folder(
                    self.files,
                    open_file_call,
                    self.folder_path + os.path.sep + file))
                continue

            if os.path.splitext(file_absolute_path)[1] != '.csv':
                continue
            file_btn = FilePathButton(self.files, file, file_absolute_path, open_file_call)
            self.files_v_layout.addWidget(file_btn)

        self.files.setLayout(self.files_v_layout)

        self.main_v_layout.addWidget(self.files)

        self.setLayout(self.main_v_layout)

    def open_folder(self):
        self.close() if self.folder_open else self.open()
        self.folder_open = not self.folder_open

    def open(self):
        self.files.show()
        self.folder_btn.setIcon(QIcon(icon.OPENED_FOLDER_I()))

    def close(self):
        self.files.hide()
        self.folder_btn.setIcon(QIcon(icon.FOLDER_I()))
