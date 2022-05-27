from mice.ispisTable import *
from mice.heuristika import *
import main
from main import pozicija_u_koordinatu, koordinata_u_poziciju, koordinata_u_poziciju_faza1, nova_lista, nova_lista_faza1, pozicija_u_koordinatu_faza1

class Tabla(object):
    def __init__(self, lista, faza):
        self._izgled = lista
        self._roditelj = None
        self._deca = []
        self._faza = faza
        self._boja = "▢"
    def __str__(self):
        ispisTable.ispisTable(self._izgled)
        return ""
    def __lt__(self, other):
        heuristickavrednost1 = heuristika(self._izgled, self._faza, self._boja)
        heuristickavrednost2 = heuristika(other._izgled, other._faza, self._boja)
        return heuristickavrednost1 < heuristickavrednost2
    def __eq__(self, other):
        heuristickavrednost1 = heuristika(self._izgled, self._faza, self._boja)
        heuristickavrednost2 = heuristika(other._izgled, other._faza, self._boja)
        return heuristickavrednost1 == heuristickavrednost2

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
    def __len__(self):
        return len(self._izgled)

    def validni_potezi_faza1(self, boja, potreba):
        potezi = []
        pozicija=0
        koordinate = []
        for i in range(3):
            for j in range(8):
                if j == 7:
                    sledece = 0
                else:
                    sledece = j + 1
                pozicija+=1
                if self._izgled[i][j] == "x":
                    if potreba == "broj":
                        lista = nova_lista_faza1(self._izgled, boja, i*8+sledece)
                        potezi.append(Tabla(lista, self._faza))
                    elif potreba == "potezi_koordinate":
                        koordinate.append(pozicija_u_koordinatu_faza1(pozicija))
        if potreba == "broj":
            return potezi
        elif potreba == "potezi_koordinate":
            return koordinate


    def validni_potezi_faza2(self, boja, potreba):   #vraca listu objekata tipa tabla koji su u stvari sva deca ove table???
        potezi = []                         #nzm svakako vraca listu tabli
        pozicija=0
        koordinate = []
        for i in len(self._izgled):
            for j in len(self._izgled[i]):
                pozicija+=1
                if j == 0:
                    prethodno = 7
                elif j == 7:
                    sledece = 0
                if self._izgled[i][j] == boja:
                    if self._izgled[i][prethodno] == "x":
                        if potreba == "broj":
                            lista = nova_lista(self._izgled, pozicija, i*8+prethodno)  #pozicije idu od 1 do 24
                            potezi.append(Tabla(lista))
                        elif potreba == "potezi_koordinate":
                            koordinate.append(pozicija_u_koordinatu(pozicija, i*8+prethodno))
                    if self._izgled[i][sledece] == "x":
                        if potreba == "broj":
                            lista = nova_lista(self._izgled, pozicija, i*8+sledece)
                            potezi.append(Tabla(lista))
                        elif potreba == "potezi_koordinate":
                            koordinate.append(pozicija_u_koordinatu(pozicija, i*8+sledece))
                    if j in [1, 3, 5, 7] and i in [0, 2]:
                        if self._izgled[1][j] == "x":
                            if potreba == "broj":
                                lista = nova_lista(self._izgled, pozicija, j+9)
                                potezi.append(Tabla(lista))
                            elif potreba == "potezi_koordinate":
                                koordinate.append(pozicija_u_koordinatu(pozicija, j+9))
                    elif j in [1, 3, 5, 7] and i==1:
                        if self.izgled[0][j] == "x":
                            if potreba == "broj":
                                lista = nova_lista(self._izgled, pozicija, 2)
                                potezi.append(Tabla(lista))
                            elif potreba == "potezi_koordinate":
                                koordinate.append(pozicija_u_koordinatu(pozicija, 2))
                        elif self.izgled[2][j] == "x":
                            if potreba == "broj":
                                lista = nova_lista(self._izgled, pozicija, 18)
                                potezi.append(Tabla(lista))
                            elif potreba == "potezi_koordinate":
                                koordinate.append(pozicija_u_koordinatu(pozicija, 18))
        if potreba == "broj":
            return potezi
        elif potreba == "potezi_koordinate":
            return koordinate

    def da_li_je_kraj_igre(self):
        if self._boja == "■":
            boja2 = "▢"
        else:
            boja2 = "■"
        if len(self.validni_potezi_faza2(boja2, "broj")) == 0 or heuristika.broj_piona(self._izgled, boja2) == 2:
            return "pobeda"
        elif len(self.validni_potezi_faza2(self._boja, "broj")) == 0 or heuristika.broj_piona(self._izgled, self._boja) == 2:
            return "poraz"
        else:
            return ""

    def da_li_je_potez_validan_faza2(self, koji, gde, faza="2"):
        if self._boja == "■":
            boja2 = "▢"
        else:
            boja2 = "■"
        if nova_lista(self._izgled, koji, gde) in self.validni_potezi_faza2(boja2, "broj"):
            return True
        else:
            return False
