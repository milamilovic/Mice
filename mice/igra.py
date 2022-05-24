from mice.tabla import Tabla
import tabla

class Igra(object):

    __slots__ = ["_trenutno_stanje", "_na_potezu"]

    def __init__(self):
        self._trenutno_stanje = Tabla([["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"]], 1)
        self._na_potezu = "▢"           #kompjuter prvi igra

    def igraj():
        pass