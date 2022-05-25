class ElementMape(object):
    def __init__(self, kljuc, vrednost):
        self._kljuc = kljuc
        self._vrednost = vrednost

    @property
    def kljuc(self):
        return self._kljuc
    @property
    def vrednost(self):
        return self._vrednost
    @vrednost.setter
    def vrednost(self, value):
        self._vrednost = value


class Mapa(object):
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def __contains__(self, trazeni_kljuc):
        for element in self._data:
            if element._kljuc == trazeni_kljuc:
                return True
            return False
    def __iter__(self):
        for element in self._data:
            yield element._kljuc
    
    def get_element(self, trazeni_kljuc):
        for element in self._data:
            if element._kljuc == trazeni_kljuc:
                return element._vrednost
        print("Ne postoji element sa ključem " + str(trazeni_kljuc))
    def set_element(self, trazeni_kljuc, nova_vrednost):
        for element in self._data:
            if element._kljuc == trazeni_kljuc:
                element._vrednost = nova_vrednost
                return
        self._data.append(ElementMape(trazeni_kljuc, nova_vrednost))
    def obrisi_element(self, trazeni_kljuc):
        for i in range(len(self._data)):
            if self._data[i]._kljuc == trazeni_kljuc:
                self._data.pop(i)
                return
        print("Ne postoji element sa ključem " + str(trazeni_kljuc))
    def items(self):
        for element in self._data:
            yield element._kljuc, element._vrednost
    def kljucevi(self):
        for element in self._data:
            yield element._kljuc
    def vrednosti(self):
        for element in self._data:
            yield element._vrednost
    def clear(self):
        self._data = []


