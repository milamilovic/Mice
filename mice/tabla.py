import figura
import ispisTable
import heuristika
import main

class Tabla(object):
    def __init__(self, lista):
        self._izgled = lista
        self._roditelj = None
        self._deca = []
        self._faza = 1
        self._boja = main._boja
    def __str__(self):
        ispisTable.ispisTable(self._izgled)
        return ""
    def __lt__(self, other):
        vrednost1 = heuristika.heuristika(self._izgled, self._faza, main.boja)
        vrednost2 = heuristika.heuristika(other._izgled, other._faza, main.boja2)
        return vrednost1 < vrednost2
    def __eq__(self, other):
        vrednost1 = heuristika.heuristika(self._izgled, self._faza, main.boja)
        vrednost2 = heuristika.heuristika(other._izgled, other._faza, main.boja2)
        return vrednost1 == vrednost2

    @property
    def izgled(self):
        return self._izgled
    @izgled.setter
    def izgled(self, value):
        self._izgled = value
    @property
    def roditelj(self):
        return self._roditelj
    @roditelj.setter
    def roditelj(self, value):
        self._roditelj = value
    @property
    def deca(self):
        return self._deca
    @deca.setter
    def deca(self, value):
        self._deca = value
    @property
    def faza(self):
        return self._faza
    @faza.setter
    def faza(self, value):
        self._faza = value

    def _is_root_(self):
        return self._roditelj == None
    def _is_leaf_(self):
        return self._deca == []
    def _dodaj_dete_(self, vrednost):
        vrednost._roditelj = self
        if len(self._deca) == 0:
            self._deca.append(vrednost)
        elif vrednost<=self._deca[-1]:
            self._deca.append(vrednost)
        else:
            for i in range(len(self._deca)):                   #sortirana deca, od najveće vrednosti do najmanje
                if self._deca[i]._vrednost <= vrednost._vrednost:
                    self._deca.insert(i+1, vrednost)
    def _ukloni_dete_(self, vrednost):
        self._deca.remove(vrednost)
    def nadji_roditelja(self):
        return self._roditelj
    def ko_su_deca(self):
        return self._deca
    def broj_dece(self):
        return len(self._deca)