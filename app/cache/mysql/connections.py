import json
import os
import sys
from typing import Union


class Connections:
    def __init__(self):
        self.connections = []
        self._connections = None
        self._CONNECTIONS_PATH = f'data{os.path.sep}connections.json'

        self._load_connections()

    def _load_connections(self):
        try:
            connections_file = open(self._CONNECTIONS_PATH, 'r')
            self.connections = json.load(connections_file)
            connections_file.close()
            self.set_up()

        except IOError:
            pass

    def add_connection(self) -> bool:
        pass

    def delete_connection(self, conn: Union[dict, int]) -> None:
        pass

    def delete_connections(self) -> bool:
        pass

    def set_up(self):
        pass
        # for connection in self._connections:
        #    self.connections.append(c)


conn = Connections().connections


class MutableDefault:
    def __init__(self, object_):
        self.value = None
        if type(object_) is list:
            self.value = []
            for item in object_:
                if type(item) in [dict, list]:
                    self.value.append(MutableDefault(item))
                    continue
                self.value.append(item)
        else:
            for key in object_.keys():
                if type(object_[key]) in [dict, list]:
                    setattr(self, key, MutableDefault(object_[key]))
                    continue
                setattr(self, key, object_[key])

    def __getitem__(self, index):
        if type(self.value) is list:
            return self.value[index]
        raise os.error.KeyError(f": {index}")

    def __iter__(self):
        if self.value is None:
            for atr in [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))][1:]:
                yield atr
            return
        for value in self.value:
            yield value


d1 = {
    'x':{
        "x1":"x1",
        "x2":"x2",
        "x3":{
            "x31":"x31",
            "x32":"x32",
            "x33":"x33"
        },
        "x4":[
            {
                "x411":"x411",
                "x412":"x412",
                "x413":"x413"

            },
            {
                "x421":"x421",
                "x422":"x422",
                "x423":"x423"

            },
            {
                "x431":"x431",
                "x432":"x432",
                "x432":"x432"

            },
            "x45"
        ]
    },
    "y": 2,
    "z": 3
}

m = MutableDefault(d1)
print(sys.getsizeof(m))
print(sys.getsizeof(d1))
