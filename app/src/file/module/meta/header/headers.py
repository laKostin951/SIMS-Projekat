from abc import ABC
from enum import Enum

from PySide2.QtWidgets import QWidget
from multimethod import multimethod


class InvalidInput(Enum):
    Min: 1
    Format: 2


class _Header(ABC):
    def __init__(self, header):
        self.signature = None
        self.header = header
        self.min = self.header["data_type"]["min_value"]
        self.max = self.header["data_type"]["max_value"]
        self.predefined_values = self.header["predefined_values"]
        self.not_null = self.header["not_null"]

    def input(self, parent: QWidget) -> QWidget:  ...

    def filter_input(self, parent: QWidget) -> QWidget: ...

    def validate(self, enrolled_text: str):
        if enrolled_text < self.min:
            yield False, InvalidInput.Min

        return self.signature.match(), InvalidInput.Format


class _HeaderInt(_Header, ABC):
    def __init__(self, header):
        super().__init__(header)
        self.signature = ""

    @multimethod
    def input(self) -> QWidget:  ...

    @multimethod
    def input(self, parent: QWidget) -> QWidget: ...


class _HeaderNumber(_Header, ABC):
    def __init__(self, header):
        super().__init__(header)
        self.signature = ""

    @multimethod
    def input(self) -> QWidget:  ...

    @multimethod
    def input(self, parent: QWidget) -> QWidget: ...


class _HeaderDate(_Header, ABC):
    def __init__(self, header):
        super().__init__(header)
        self.signature = ""

    @multimethod
    def input(self) -> QWidget:  ...

    @multimethod
    def input(self, parent: QWidget) -> QWidget: ...


class _HeaderChar(_Header, ABC):
    def __init__(self, header):
        super().__init__(header)
        self.signature = ""

    @multimethod
    def input(self) -> QWidget:  ...

    @multimethod
    def input(self, parent: QWidget) -> QWidget: ...


class _HeaderVarchar(_Header):
    def __init__(self, header):
        super().__init__(header)
        self.signature = ""

    @multimethod
    def input(self) -> QWidget:  ...

    @multimethod
    def input(self, parent: QWidget) -> QWidget: ...
