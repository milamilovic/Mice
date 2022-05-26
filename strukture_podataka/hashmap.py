import strukture_podataka
from strukture_podataka import mapa
from strukture_podataka.mapa import ElementMape, Mapa
import random
from operator import __xor__, xor

class HashMap(object):          #kolizije se resavaju ulancavanjem
    def __init__(self, inicijalni_kapacitet = 64):
        self._data = inicijalni_kapacitet * []
        self._kapacitet = inicijalni_kapacitet
        self._prost_broj = 2637245579
        self._velicina = 0
        self._vrednost_table = self._init_tabla()
        self._hes = random.randint(0, 255)
        self._a = 1+random.randrange(self._prost_broj-1)
        self._b = random.randrange(self._prost_broj)
    def __len__(self):
        return len(self._data)
    def _init_tabla(self):
        tabla = []
        for i in range(3):
            sloj = []
            for j in range(8):
                sloj.append([random.randint(0, 255), random.randint(0, 255)])
            tabla.append(sloj)
        return tabla
                
    def _hash(self, tabla):                         #tzv zobrist hesiranje, popularno u sahu
        hesirana = self._hes                        #svako polje table ima random 2 vrednosti 0-255
        for i in range(3):                          #kada hesiramo tablu uzmemo 1. za belu tj drugu vrednost 
            for j in range(8):                      #ako je crno polje i hes koji racunamo xor-ovanjem svih tih  
                polje = tabla[i][j]                 #rendom vrednosti podignemo na stepen te random vrednosti
                vrednost_polja = self._vrednost_table[i][j]
                if polje == "▢":
                    vrednost = vrednost_polja[1]
                elif polje == "■":
                    vrednost = vrednost_polja[2]
                else:
                    vrednost = 1
                hesirana = xor(hesirana, vrednost)
        return ((hesirana*self._a + self._b) % self._prost_broj) % self._kapacitet      #kompresovanje kljuca

    def resize(self, novi_kapacitet):
        stari_podaci = list(self.items())
        self._data = novi_kapacitet * [None]
        self.size = 0
        for (kljuc, vrednost) in stari_podaci:
            self[kljuc] = vrednost

    def __getitem__(self, kljuc):
        bucket_index = self._hash(kljuc)
        return self.bucket_get_element(bucket_index, kljuc)
    def __setitem__(self, kljuc, vrednost):
        bucket_index = self._hash(kljuc)
        self.bucket_set_element(bucket_index, kljuc, vrednost)
        trenutni_kapacitet = len(self._data)
        if self._velicina > trenutni_kapacitet // 2:
            self.resize(2*trenutni_kapacitet - 1)
    def __delitem__(self, bucket_index, kljuc):
        bucket = self._data[bucket_index]
        del bucket[kljuc] 
    def items(self):
        for bucket in self._data:
            if len(bucket) != 0:
                for item in range(len(bucket)):
                    yield bucket[item]
    def bucket_get_element(self, bucket_index, kljuc):
        return self._data[bucket_index][kljuc]
    def bucket_set_element(self, bucket_index, kljuc, vrednost):
        bucket = self._data[bucket_index]
        if bucket is None:
            self._data[bucket_index] = Mapa()
        trenutna_velicina = len(self._data[bucket_index])
        self._data[bucket_index][kljuc] = vrednost
        if len(self._data[bucket_index]) > trenutna_velicina:
            self._velicina += 1
    def __iter__(self):
        for bucket in self._data:
            if bucket is not None:
                for kljuc in bucket:
                    yield kljuc
