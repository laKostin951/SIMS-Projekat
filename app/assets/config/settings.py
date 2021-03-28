from app.assets.config._config import _Config
from app.assets.config._icon import _Icon
from cache.server.mysql_server_connections import MysqlServerConnections
from dataHandler.mySql.connection import make_pool_party

config = _Config()
icon = _Icon(config.get_icon_config())
mysqlServerConnections = MysqlServerConnections()
cnxpool = make_pool_party(mysqlServerConnections[0])

WIDTH = 1920
HEIGHT = 1080

DEFAULT_DATA_FOLDER = config.get_default_data_path()
