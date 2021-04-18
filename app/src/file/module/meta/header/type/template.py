BLANK_HEADER = {
    "name":              "Column name",
    "is_primary":        False,
    "is_foreign_key":    False,
    "data_type":         {},
    "predefined_values": None,
    "not_null":          False
}

BLANK_INT = {
    "type":      "int",  # const
    "min_value": 0,
    "max_value": 0
}

BLANK_STR = {
    "type":      "str",  # const
    "min_value": 0,
    "max_value": 0
}

BLANK_DATA = {
    "type":              "date",  # const
    "min_value":         10,  # const
    "max_value":         10,  # const
    "date_format":       {
        "day":    [8, 9],   # pozicije
        "month":  [5, 9],
        "year":   [0, 1, 2, 3],
        "format": "YYYY-MM-DD"
    },
    "date_delimiter":    "/",
    "max_possible_date": "",
    "min_possible_date": ""
}
