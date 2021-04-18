from datetime import date
from typing import Union

from app.src.file.module.meta.header.type.template import BLANK_INT, BLANK_STR


def _create_NUMBER(ln: int = 11) -> dict:
    """
    Creates a 'data_type' object for metadata for data type NUMBER

    :param ln: Represents min/max number of digits that the value could have,
     since it is NUMBER min and max are equal,
     if the parameter is not forwarded, the default value is 11

    :return: Returns the 'data_type' object needed to create metadata
    :rtype: dict:
    """
    blank_data_type = BLANK_INT
    blank_data_type["min_value"] = ln
    blank_data_type["max_value"] = ln
    return blank_data_type


def _create_VARCHAR(min_: int = 0, max_: int = 1000) -> dict:
    """
    Creates a 'data_type' object for the metadata for the VARCHAR data type

    :param min_: type int: The minimum number of characters that a value must have

    :param max_: type int: The maximum number of characters that a value value could have

    :return: Returns the 'data_type' object needed to create metadata
    """
    blank_data_type = BLANK_STR
    blank_data_type["min_value"] = min_
    blank_data_type["max_value"] = max_
    return blank_data_type


def _create_DATE(max_possible_date: Union[date, str] = "", min_possible_date: Union[date, str] = "") -> dict:
    """
    Creates a 'data_type' object for the metadata for the DATE data type

    :param max_possible_date: Maximum possible date
    :param min_possible_date: Minimum possible date

    :return: Returns the 'data_type' object needed to create metadata
    """
    blank_data_type = BLANK_STR
    blank_data_type["min_possible_date"] = min_possible_date
    blank_data_type["max_possible_date"] = max_possible_date
    return blank_data_type


def _create_CHAR(ln: int = 256) -> dict:
    """
    Creates a 'data_type' object for the metadata for the CHAR data type

    :param ln : Represents the minimum - maximum, that is the number of characters that the value must retain

    :return: Returns the 'data_type' object needed to create the metadata
    """
    blank_data_type = BLANK_STR
    blank_data_type["min_value"] = ln
    blank_data_type["max_value"] = ln
    return blank_data_type
