from enum import Enum

from app.src.file.module.meta.header.type.creates import _create_NUMBER, _create_VARCHAR, _create_DATE, _create_CHAR


class CreateDataType(Enum):
    create_NUMBER = _create_NUMBER
    create_VARCHAR = _create_VARCHAR
    create_DATE = _create_DATE
    create_CHAR = _create_CHAR
