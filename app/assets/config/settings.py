from app.assets.config._config import _Config
from app.assets.config._icon import _Icon

config = _Config()
icon = _Icon(config.get_icon_config())

WIDTH = 1080
HEIGHT = 1980

DEFAULT_DATA_FOLDER = config.get_default_data_path()
DEFAULT_METADATA_NAMING_EXTENSION = '_metadata.json'

