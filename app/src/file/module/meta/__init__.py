import csv
import json

import os
from typing import Union

from app.src.file.module.meta.templates import BLANK_META
from app.src.file.module.meta.header.create import create_header
from app.src.file.module.meta.header.type.create import CreateDataType


class MetaData:
    """
    : parm: path - Path to the metadata file, which describe file that is represented in table widget
    : parm: data_path - Path to file which data is represented in table
    """

    def __init__(self, metadata_path: str, data_path: str, load=True):
        self.path = metadata_path
        self._data_path = data_path
        self.metadata = None
        if load:
            self.load()

    def load(self):
        """
        Radi se ucitavanje metapodatka iz fajla na putanji  `self.path` - (putanja je unapred izgenerisana
        po utvrdjenom stanrdu)
        U slucaju da meta podaci ne postoje korisnik se pita da li zeli da se meta podaci generisu iz
        fajla na putnaji `self._data_path_c` -
        (NO) `self.meta` ce dobiti vrednost `None` ( Dalje akcije sa fajlom i otvaranjem fajla nisu u nadleznosti klase `Metadata` )
        (YES) poziva se fukcija za izvalcenje meta podatka

        """
        try:
            metadata_file = open(self.path, 'r')
            self.metadata = json.load(metadata_file)
            metadata_file.close()
        except FileNotFoundError:
            new = True
            if new:  # TODO : doadti popUp sa pitanjem da li da se generisu novi podaci
                self._generate_metadata()

    # CREATING NEW METADATA
    def _generate_metadata(self):
        """
        Izvlace se meta podaci iz fajla koji se nalazi na putanji `self._data_path_c`,
        ako meta podaci nisu nadjeni korisniku se nudi opcija da ih sam kreira
        preproduction : Izvuceni meta podaci se zatim otvaruju u Editoru za meta podake da bi
                        korisnik mogao da edituje same podatke po svojoj zelji
        korisnis se pita da li hoce da sacuva meta podatke
        """
        try:
            metadata = self._extract_metadata()
            if metadata is None: ...  # TODO: ponudti korisniku da sam kreira metapodatke
            # TODO : otvoriti generisane meta podatke u prozoru za kreiranje tabele u funkciji editovanja meta podatka
            self.metadata = metadata
        finally:
            save = True  # TODO : pitati korisnika da li hoce da sacuva meta podatke da ne bi moralo
                        # sledeci put opet da se izvlace metapodaci
            if save:
                pass
                #self.save()

    def _extract_metadata(self) -> Union[None, dict]:
        """
        Pod fajlom se oznaca fajl koji se nalzi na putanji proslednjeonoj pod pareametrom
        (data_path_c.path)
        Izvlaci se dialect za fajla( ako nije nadje dialect vraca se None), izvlace se nazivi headera za fajl,
        zatim se od dobijenih podatka generisu metapodaci koji opisuju dati fajl

        :return: type: dict: Vrecaju se genereisani meta podaci za zadati fajl
                type: NoneType: Nije nadjen dialect
        """
        dialect = self._extract_dialect()
        if dialect is None:
            return None
        headers = [header for header in self._extract_header_names(dialect)]

        # TODO: ako je dialect.delimiter = ''( nije nadjen ) ne otvoriti file ili ga otvoriti kao txt

        blank = BLANK_META

        blank["headers"] = [create_header(header,
                                          header,
                                          False,
                                          False,
                                          None,
                                          False,
                                          CreateDataType.create_VARCHAR())
                            for header in headers]
        blank["headers_count"] = len(headers)
        blank["dialect"]["skip_first_line"] = headers[0] == "Column 1"
        blank["dialect"]["delimiter"] = dialect.delimiter
        blank["dialect"]["quoting"] = dialect.quoting

        return blank

        #   Ako prvi elemetn nije "Column 1" znaci
        # nasao je nazive kolona i treba preskocit prvi red(header line)
        # u suprotnom nije nasao nazive kolona i treba prikzati prvi red
        #   Postoji moguce da je doslo do greske da u fajlu postoje
        # nazivi kolona(U prvom redu) ali ih program nije pronaoso,
        # ali rezultat te greske ce biti samo
        # prkzaivanje naziva kolona kao 1. reda u tabeli

    def _extract_dialect(self):
        data_file = None
        try:
            data_file = open(self._data_path, 'r')
            return csv.Sniffer().sniff(data_file.read(2048))
        except FileNotFoundError:
            # TODO: error slucaj ako dataExtras file ne postoji
            pass
        finally:
            if data_file is not None:
                data_file.close()

    def _extract_header_names(self, dialect):  # TODO: documentation
        data_file = open(self._data_path, 'r')
        buffer = data_file.read(2048)  # citamo prvih 2048

        headers = list(filter(None, buffer.split('\n')))
        headers = headers[0].split(dialect.delimiter)

        default_header = [f'Column {index}' for index, _ in enumerate(headers)]

        headers = [header_name.strip('\"') for header_name in headers]

        for header_name in headers:
            if header_name.isdigit():
                return default_header
            if type(header_name) == bool or header_name in ["False", "false", "True", "true"]:
                return default_header

        data_file.seek(0)
        data_file.close()
        return headers

    def __extract_header_names(self, dialect):  # TODO: documentation
        data_file = open(self._data_path, 'r')
        buffer = data_file.read(2048)  # citamo prvih 2048

        possible_header_arr = list(filter(None, buffer.split('\n')))
        # delimo file po novom redu,
        # possible_header_arr sada izgleda ["",
        #                                   ""Broj Indeksa" ,"Ime i prezime"",
        #                                   "",
        #                                   ""20606903", "Marko Markovic"", .....]
        # do praznoh elemenata moze doci ako fajl sadrzi prazna polja
        # zata iz niza izbacujemo prazne redove, odnosno prazne strignove
        # pomocu funkcije list(filter(None, arr)
        possible_header_arr = possible_header_arr[0].split(dialect.delimiter)
        # possible_header_arr sada izgleda [""Broj Indeksa"",""Ime i prezime""]

        possible_header_arr = [header_name.strip('\"') for header_name in possible_header_arr]
        # prolazimo for petljom kroz 'possible_header_arr' i za
        # brisemo dodatne znake navodnika odnosno ako je csv fajl upian sa nekim dodatnim "quoting"

        default_header = []

        for i in range(0, len(possible_header_arr)):
            default_header.append(
                "Column " + str(i + 1))  # pravimo default_header da bude ["Kolona 1", "Kolona 2" .... ]

        for header_name in possible_header_arr:
            if header_name.isdigit():  # proveravamo da li je 'pure digit' jer ime kolone ne moze da bude samo broj
                return default_header
            if type(header_name) == bool:  # proveravamo da li je "bolean" jer ime kolone ne moze da bude "boolean"
                return default_header

        data_file.seek(0)
        data_file.close()
        return possible_header_arr

    # GET HARDER
    def get_headers_names(self) -> list:
        """
        Method create and return list with all headers names( str )

        :rtype: list
        :return: Returns list arr of header names
        """
        return list(map(lambda header: header["name"], self.metadata["headers"]))

    def get_header(self, parm: Union[int, str, dict]) -> Union[None, tuple]:
        """
        Odlucije se koja ce funkcija da se pozove zavinso od toga staje prosledjeno kao parametar
        :param parm:  (INT) - znaci je je poslat index headera i trazi se header na tom indexu
                      (STR) - znaci da je posalt `name` headera odnosno naziv koji je prikazuje korisniku u tabeli
                            i trzi se pozicija i sami podaci headera sa tim nazivmo
                      (DICT) - znaci da je posalt sam header i trazi se njegova pozicija

        :return: Vraca ce vrednost poziva odgovaraju funckoje za taj tip parametra :
                Ako je header nadje Tuple( pos: int, header: dict)
                Ako nije  None
        """

        if type(parm) is int:
            return self._get_header_int(parm)
        if type(parm) is str:
            return self._get_header_str(parm)
        if type(parm) is dict:
            return self._get_header_dict(parm)

    def _get_header_int(self, pos: int) -> Union[None, tuple]:
        """
        dobavlja se pozicija i sami podaci headera, na zadatoj poziciji
        :param pos:  pozicija headera koji se trazi
        :return: u slucaju nadjenog header vrace se tuple( index: int, header: dict )
                u slucaju da nije nadjen header na toj poziciji vraca se NoneType( None )
        """
        if len(self.metadata["headers"]) > pos:
            return None
        return pos, self.metadata["headers"][pos]

    def _get_header_dict(self, header: dict) -> Union[None, tuple]:
        """
        dobavlja se pozicija i sami podaci headera,  trazenog  po paramrtu `header.name`
        :param header:  sam header cija je pozicija u nizu trazi
        :return: u slucaju nadjenog header vrace se tuple( index: int, header: dict )
                u slucaju da nije nadjen header u listi `headers` vraca se NoneType( None )
        """
        for index, header in enumerate(self.metadata["headers"]):
            if header == header:
                return index, header
        return None

    def _get_header_str(self, name: str) -> Union[None, tuple]:
        """
        dobavlja se pozicija i sami podaci headera,  trazenog  po paramrtu `header.name`
        :param name:  `name` hedera koji se trazi( naziv za header koji se prikazuje u tabeli )
        :return: u slucaju nadjenog header vrace se tuple( index: int, header: dict )
                u slucaju da nije nadjen header sa tim `name` vraca se NoneType( None )
        """
        for index, header in enumerate(self.metadata["headers"]):
            if header["name"] == name:
                return index, header
        return None

    # ESSENTIAL FUNCTIONS
    def save(self) -> bool:
        """
        Method for saving metadata file

        :rtype: bool
        :return: Success of saving metadata file, if file already exist it will raise error and false is returned
        """
        try:
            metadata_file = open(self.path, 'w')
            json.dump(self.metadata, metadata_file)
            metadata_file.close()
            return True

        except FileExistsError:
            return False

        finally:
            pass

    def delete(self) -> bool:
        """
        Method for deleting metadata file

        :rtype: bool
        :return: Success of deleting metadata file
        """
        try:
            os.remove(self.path)
            return True
        except FileNotFoundError:
            return False
        finally:
            pass


meta = MetaData("/home/igork/singi/SIMS-S2G2/SIMS-Projekat-1.1/test/data/5m Sales Records_metadata.json",
                "/home/igork/singi/SIMS-S2G2/SIMS-Projekat-1.1/test/data/5m Sales Records.csv", True)

