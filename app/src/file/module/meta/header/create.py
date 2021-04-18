from typing import Union

from app.src.file.module.meta.header.type.template import BLANK_HEADER


def create_header(name: str,
                  label: str,
                  is_primary: bool,
                  is_foreign_key: bool,
                  predefined_values: Union[None, dict],
                  not_null: bool,
                  data_type: dict) -> dict:
    """
    Funkcija za kreiranje 'data_type' objekta za date parametre

    :param name: Naziv kolone
    :param label: Labela koja ce se koristiti kao 'key' u applikaciji za rad sa vrednostima iz te kolone
    :param is_primary: Da li je kolona primarni kljuc( primary key) True( jeste ) / False( nije )
    :param is_foreign_key: Da li je kolona strani kljuc( foreign key) True( jeste ) / False( nije )
    :param predefined_values: Predevinisane vrednosti, odnosno listi vrednoti koje su dozvoljene da se upisu u kolonu
    :param not_null:
    :param data_type: vrednost jedne od ponudjenih opcija za kreiranje novog tipa iz klase 'CreateDataType'
    """

    blank_header = BLANK_HEADER
    blank_header["name"] = name
    blank_header["is_primary"] = is_primary
    blank_header["is_foreign_key"] = is_foreign_key
    blank_header["data_type"] = data_type
    blank_header["predefined_values"] = predefined_values
    blank_header["not_null"] = not_null

    return blank_header
