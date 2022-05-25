from mice.heuristika import heuristika
from mice.tabla import Tabla
import tabla
from copy import deepcopy
from time import time
import main

class Igra(object):

    __slots__ = ["_trenutno_stanje", "_na_potezu"]

    def __init__(self):
        self._trenutno_stanje = Tabla([["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"]], 1)
        self._na_potezu = "▢"           #kompjuter prvi igra

    def varijabilna_dubina(self, tabla, proteklo_vreme_od_pocetka_poteza):
        if tabla._faza == 1:
            moguci_potezi = len(tabla.validni_potezi_faza1(tabla, self._na_potezu, "broj"))
        else:
            moguci_potezi = len(tabla.validni_potezi_faza2(tabla, self._na_potezu, "broj"))
        if proteklo_vreme_od_pocetka_poteza>=2.5:
            return 1
        elif moguci_potezi<=5:
            return 5
        elif moguci_potezi<=8:
            return 4
        elif moguci_potezi>8:
            return 3

    def kompjuter_potez_faza1(self, stablo, hesmapa, alfa, beta):
        pass

    def kompjuter_potez(self, stablo, hesmapa, alfa, beta):
        pass

    def minimax(tabla, dubina, hash_map, cvor_stabla, igrac, alfa, beta):
        pass

    def igraj(self, stablo, hesmapa):
        for i in range(9):                  #faza 1
            print()
            print("Kompjuter je na potezu!")
            print()
            self.kompjuter_potez_faza1(stablo, hesmapa, None, None)
            self._na_potezu = "■"
            print()
            print("Vi ste na potezu!")
            print()
            potezi = self._trenutno_stanje.validni_potezi_faza1("■", "potezi_koordinate")
            print("Mogući potezi su: ")
            for i in range(1, len(potezi)+1):
                print(str(i) + ". " + potezi[i-1])
            while potez < 1 and potez > len(potezi):
                potez = int(input("Unesite redni broj poteza koji želite da odigrate: "))
            gde = main.koordinata_u_poziciju_faza1(potezi[potez-1])
            novo_stanje = main.nova_lista_faza1(self._trenutno_stanje, "■", gde)
            self._trenutno_stanje = novo_stanje
            self._na_potezu = "▢"
        while heuristika.pobednicka_konfiguracija() != 1000 or heuristika.pobednicka_konfiguranica != -1000:    #faza 2
            if self._na_potezu == "▢":
                print()
                print("Kompjuter je na potezu!")
                print()
                self.kompjuter_potez(stablo, hesmapa, None, None)
                self._na_potezu = "■"
            else:
                print()
                print("Vi ste na potezu!")
                print()
                potezi = self._trenutno_stanje.validni_potezi_faza2("■", "potezi_koordinate")
                print("Mogući potezi su: ")
                for i in range(1, len(potezi)+1):
                    print(str(i) + ". " + potezi[i-1])
                while potez < 1 and potez > len(potezi):
                    potez = int(input("Unesite redni broj poteza koji želite da odigrate: "))
                koji, gde = main.koordinata_u_poziciju(potezi[potez-1])
                novo_stanje = main.nova_lista(self._trenutno_stanje, koji, gde)
                self._trenutno_stanje = novo_stanje
                self._na_potezu = "▢"
        if heuristika.pobednicka_konfiguracija() == 1000:
            print()
            print("Izgubili ste! Računar je pobedio!")
            print()
        elif heuristika.pobednicka_konfiguracija() == -1000:
            print()
            print("Pobedili ste!")
            print()
