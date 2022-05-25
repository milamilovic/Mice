class EmptyListException(Exception):
    pass

class CvorListe(object):
    def __init__(self, vrednost, prethodni=None, sledeci=None):
        self._vrednost = vrednost
        self._prethodni = prethodni
        self._sledeci = sledeci

    def __str__(self):
        return str(self._vrednost)

    @property
    def vrednost(self):
        return self._vrednost
    @vrednost.setter
    def vrednost(self, value):
        self._vrednost = value
    @property
    def prethodni(self):
        return self._prethodni
    @prethodni.setter
    def prethodni(self, value):
        self._prethodni = value
    @property
    def sledeci(self):
        return self._sledeci
    @sledeci.setter
    def sledeci(self, value):
        self._sledeci = value



class Dvostruka(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._duzina = 0
    def __len__(self):
        return self._duzina
    def __iter__(self):
        cvor = self._head
        while cvor != self._tail:
            yield cvor
            cvor = cvor._sledeci
        yield cvor
    def __getitem__(self, index):
        return self._cvor_po_indeksu(index)._vrednost
    def __setitem__(self, index, value):
        self._cvor_po_indeksu(index)._vrednost = value
    def __str__(self):
        rezultat = "["
        for el in self:
            rezultat += str(el)
            if el != self._tail:
                rezultat += ", "
        rezultat += "]"
        return rezultat

    def _cvor_po_indeksu(self, indeks):
        if indeks == 0:
            return self._head
        elif indeks == 1:
            return self._head._sledeci
        elif indeks == self._duzina-1:
            return self._tail
        elif indeks>=self._duzina:
            print("Prekoračena je dužina liste!")
        else:
            cvor = self._head
            while indeks != 1:
                cvor = cvor._sledeci
                indeks -= 1
            return cvor._sledeci
    def prazna(self):
        return self._duzina == 0
    def dodajPrvog(self, vrednost):
        cvor = CvorListe(vrednost)
        if self._duzina == 0:
            self._tail = cvor
        else:
            cvor._sledeci = self._head
        self._head = cvor
        self._duzina += 1
    def dodajPoslednjeg(self, vrednost):
        cvor = CvorListe(vrednost)
        if self._duzina == 0:
            self._head = cvor
        if self._duzina == 1:
            self._tail = cvor
            cvor._prethodni = self._head
            self._head._sledeci = cvor
        else:
            cvor._prethodni = self._tail
        self._tail = cvor
        self._duzina += 1
    def ukloniPrvog(self):
        if self._duzina == 0:
            raise EmptyListException("Lista je prazna!")
        elif self._duzina == 1:
            self._tail = None
            self._head = None
            self._duzina = 0
        else:
            self._head = self._head._sledeci
            self._duzina -= 1
    def ukloniPoslednjeg(self):
        if self._duzina == 0:
            raise EmptyListException("Lista je prazna!")
        elif self._duzina == 1:
            self._tail = None
            self._head = None
            self._duzina = 0
        else:
            cvor = self._tail._prethodni 
            cvor._sledeci = None
    def Prvi(self):
        return self._head._vrednost
    def Poslednji(self):
        return self._tail._vrednost
    def ubaci(self, vrednost, indeks):
        cvor = CvorListe(vrednost)
        if self._duzina == 0:
            self.dodajPrvog(cvor)
        if indeks>=self._duzina:
            print("Indeks izvan opsega!")
        elif indeks == 0:
            self.dodajPrvog(cvor)
            self._duzina += 1
        elif indeks == 1:
            cvor._sledeci = self._head._sledeci
            self._head._sledeci = cvor
            self._duzina += 1
        elif indeks == self._duzina-1:
            self.dodajPoslednjeg(cvor)
            self._duzina += 1
        else:
            cvoric = self._head
            while indeks != 1:
                cvoric = self._head._sledeci
                indeks -= 1
            cvor._sledeci = cvoric._sledeci
            cvoric._sledeci = cvor
            self._duzina += 1



if __name__ == "__main__":
    L1 = Dvostruka()
    L1.dodajPoslednjeg(3)
    L1.dodajPoslednjeg(7)
    for el in L1:
        print(el)
    L1[1] = 9
    print(L1[1])
    print(L1)
    print(len(L1))
    L2 = Dvostruka()
    L2.dodajPoslednjeg(99)
    L2.dodajPoslednjeg(100)

    L1.ubaci("A", 1)
    print(L1)


