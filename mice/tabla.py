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

    def validni_potezi_faza2(self, boja):   #vraca listu objekata tipa tabla koji su u stvari sva deca ove table???
        potezi = []                         #nzm svakako vraca listu tabli
        pozicija=0
        for i in len(self._izgled):
            for j in len(self._izgled[i]):
                pozicija+=1
                if j == 0:
                    prethodno = 7
                elif j == 7:
                    sledece = 0
                if self._izgled[i][j] == boja:
                    if self._izgled[i][prethodno] == "x":
                        lista = main.nova_lista(self._izgled, pozicija, i*8+prethodno)
                        potezi.append(Tabla(lista))
                    if self._izgled[i][sledece] == "x":
                        lista = main.nova_lista(self._izgled, pozicija, i*8+sledece)
                        potezi.append(Tabla(lista))
                    if j in [1, 3, 5, 7] and i in [0, 2]:
                        if self._izgled[1][j] == "x":
                            lista = main.nova_lista(self._izgled, pozicija, j+9)
                            potezi.append(Tabla(lista))
                    elif j in [1, 3, 5, 7] and i==1:
                        if self.izgled[0][j] == "x":
                            lista = main.nova_lista(self._izgled, pozicija, 2)
                            potezi.append(Tabla(lista))
                        elif self.izgled[2][j] == "x":
                            lista = main.nova_lista(self._izgled, pozicija, 18)
                            potezi.append(Tabla(lista))
        return potezi