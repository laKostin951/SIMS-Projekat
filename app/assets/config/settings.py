import os

from app.assets.config._config import _Config
from app.assets.config._icon import _Icon

# from main import app

config = _Config()
icon = _Icon(config.get_icon_config())

# screen_resolution = app.desktop().screenGeometry()
# WIDTH, HEIGHT = screen_resolution.width(), screen_resolution.height()

WIDTH = 1080
HEIGHT = 1980

DEFAULT_DATA_FOLDER = config.get_default_data_path()
