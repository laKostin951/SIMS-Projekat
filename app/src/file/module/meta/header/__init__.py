from app.src.file.module.meta.header.headers import _HeaderInt, _HeaderNumber, _HeaderChar, _HeaderVarchar, \
    _HeaderDate, _Header


def Header(header: dict) -> _Header:
    """

    :param header:
    :rtype: object
    :return:
    """

    if header["data_type"]["type"] == "INT":
        return _HeaderInt(header)

    if header["data_type"]["type"] == "NUMBER":
        return _HeaderNumber(header)

    if header["data_type"]["type"] == "CHAR":
        return _HeaderChar(header)

    if header["data_type"]["type"] == "VARCHAR":
        return _HeaderVarchar(header)

    if header["data_type"]["type"] == "DATE":
        return _HeaderDate(header)
