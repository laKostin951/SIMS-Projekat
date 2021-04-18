import os

from app.assets.config.settings import DEFAULT_METADATA_NAMING_EXTENSION


class Path:
    def __init__(self, path):
        self.path = path if os.path.isabs(path) else os.path.abspath(path)
        self.file_name = self.path.split('/')[-1]
        self.extension = self.file_name.split('.')[-1]
        self.clear_file_name = self.file_name.split('.')[0]
        self.metadata_path = self.path.replace(('.' + self.extension), DEFAULT_METADATA_NAMING_EXTENSION, 1)

    def is_same(self, other_path):
        other_path = other_path if os.path.isabs(other_path) else os.path.abspath(other_path)
        return self.path == other_path
