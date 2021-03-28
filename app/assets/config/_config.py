import json
import os

# Klasa _Config se sme instacirati samo `settigs` , Za sve potrevbe koriscenja klase `_Config` ona se moze importovati iskoljucivo iz
# `assets.config.settings` kao kreinrana variabala `config`


class _Config:
    def __init__(self):
        self.config = None
        self._config_path = f"assets{os.path.sep}config{os.path.sep}data{os.path.sep}config.json"
        # putanja do samog fajla u kojem se nalaze informacje vezane za confoiguraciju programa
        self._load_config()

    def _load_config(self) -> None:
        try:
            config_file = open(self._config_path, 'r')
            self.config = json.load(config_file)
            config_file.close()

        except IOError:
            pass

    def get_icon_config(self) -> str:
        # Dobavlja folder u kojem su smesten ikonice koje ce se koristiti u programu
        # return self.config["icon"]
        return f'{self.config["icon"]["icon_source"]}{os.path.sep}{self.config["icon"]["icon_collection"]}{os.path.sep}'

    def get_default_data_path(self) -> str:
        # Dobavlja putanju za `default` folder u kojem su smesteni podaci za rad u softveru
        # `Default` folder je smesten  u fajlu `assets/config/data/config.json` pod ['data']['default_folder']
        return os.getcwd() + os.path.sep + self.config["data"]["default_folder"]

