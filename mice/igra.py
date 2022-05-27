from mice.heuristika import heuristika, pozicija
from mice.tabla import Tabla
from copy import deepcopy
from time import time
from main import nova_lista, nova_lista_faza1
from strukture_podataka.stablo import CvorStabla

class Igra(object):

    __slots__ = ["_trenutno_stanje", "_na_potezu"]

    def __init__(self):
        self._trenutno_stanje = Tabla([["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"]], 1)
        self._na_potezu = "▢"           #kompjuter prvi igra

    def varijabilna_dubina(self, tabla, proteklo_vreme_od_pocetka_poteza):
        if tabla._faza == 1:
            moguci_potezi = len(tabla.validni_potezi_faza1(self._na_potezu, "broj"))
        else:
            moguci_potezi = len(tabla.validni_potezi_faza2(self._na_potezu, "broj"))
        if proteklo_vreme_od_pocetka_poteza>=2.5:
            return 1
        elif moguci_potezi<=5:
            return 5
        elif moguci_potezi<=8:
            return 4
        elif moguci_potezi>8:
            return 3

    def kompjuter_potez_faza1(self, stablo, hash_map, broj_postavljenih):
        proteklo_vreme = 0
        dubina = self.varijabilna_dubina(self._trenutno_stanje, proteklo_vreme)
        potez = self.minimax1(broj_postavljenih, self._trenutno_stanje, dubina, hash_map, proteklo_vreme, stablo._trenutni, "▢", "■")
        return potez

    def kompjuter_potez(self, stablo, hash_map):
        proteklo_vreme = 0
        dubina = self.varijabilna_dubina(self._trenutno_stanje, proteklo_vreme)
        potez = self.minimax2(self._trenutno_stanje, dubina, hash_map, proteklo_vreme, stablo._trenutni, "▢", "■")
        return potez

    def minimax1(self, broj_postavljenih, tabla, dubina, hash_map, proteklo_vreme, cvor_stabla, igrac, drugi_igrac, alfa = -10000000000, beta = 10000000000):
        if dubina == 0 or broj_postavljenih == 8:       #bazni slucaj ili se prebacujemo na minimax2 jer je prosla 1. faza
            vreme = time()
            if dubina == 0:
                try:
                    vrednost = hash_map[tabla]
                except:
                    tabla_trenutna = cvor_stabla._vrednost
                    tabla_roditelja = cvor_stabla._roditelj._vrednost
                    pozicija = -1
                    for i in range(3):
                        for j in range(8):
                            pozicija += 1
                            if tabla_trenutna[i][j] != tabla_roditelja[i][j]:
                                trazena = pozicija
                                break
                    pozicije = [1, 2, 3, 15, 24, 23, 22, 10, 4, 5, 6, 14, 21, 20, 19, 11, 7, 8, 9, 13, 18, 17, 16, 12]
                    gde = pozicije[trazena]
                    vrednost = heuristika(tabla, 1, igrac, gde)
                    privremena = Tabla(tabla_trenutna)
                    hash_map[tabla] = vrednost, tabla_trenutna, privremena.validni_potezi_faza1
            elif broj_postavljenih == 8:
                vrednost = self.minimax2(self, tabla, dubina - 1, hash_map, proteklo_vreme, cvor_stabla, igrac, drugi_igrac, alfa = -10000000000, beta = 10000000000)
            proteklo_vreme += time() - vreme()
            return vrednost, None, proteklo_vreme           #vraca vrednost, najbolji potez i vreme koje je proteklo do sad
        if igrac == "▢":            #kompjuter, maximizer
            vrednost = -100000000000000
            najbolji_potez = ''
            for potez in cvor_stabla._vrednost.validni_potezi_faza1(igrac, "broj"):
                cvoric = CvorStabla(potez._izgled)
                if cvoric not in cvor_stabla._deca:
                    cvor_stabla._dodaj_dete_(cvoric)
            for potez in cvor_stabla._vrednost.validni_potezi_faza1(igrac, "broj"):
                vrednosti_dece = []
                for dete in cvor_stabla._deca:
                    vrednosti_dece.append(dete._vrednost)
                for detence in vrednosti_dece:
                    if potez._izgled == detence:
                        cvor = CvorStabla(detence)
                        break
                    else:
                        cvor = CvorStabla(potez._izgled)
                        cvor_stabla._dodaj_dete(cvor)
                try:
                    hash_map[potez] = nova_vrednost, najbolji_potez, vreme
                except:
                    start = time()
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax1(broj_postavljenih - 1, potez, dubina - 1, hash_map, proteklo_vreme, cvor, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start()
                vrednost = max(vrednost, nova_vrednost)
                alfa = max(alfa, vrednost)
                if beta < alfa:
                    break
                if vrednost == nova_vrednost:
                    najbolji_potez = potez
                if proteklo_vreme >= 2.5:
                    break
            if najbolji_potez == '':
                najbolji_potez = Tabla(cvor_stabla._vrednost, 1).validni_potezi_faza1(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme
        else:               #igrac, minimizer
            vrednost = 100000000000000
            najbolji_potez = ''
            for potez in cvor_stabla._vrednost.validni_potezi_faza1(igrac, "broj"):
                cvoric = CvorStabla(potez._izgled)
                if cvoric not in cvor_stabla._deca:
                    cvor_stabla._dodaj_dete_(cvoric)
            for potez in cvor_stabla._vrednost.validni_potezi_faza1(igrac, "broj"):
                vrednosti_dece = []
                for dete in cvor_stabla._deca:
                    vrednosti_dece.append(dete._vrednost)
                for detence in vrednosti_dece:
                    if potez._izgled == detence:
                        cvor = CvorStabla(detence)
                        break
                    else:
                        cvor = CvorStabla(potez._izgled)
                        cvor_stabla._dodaj_dete(cvor)
                try:
                    hash_map[potez] = nova_vrednost, najbolji_potez, vreme
                except:
                    start = time()
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax1(broj_postavljenih - 1, potez, dubina - 1, hash_map, proteklo_vreme, cvor, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start()
                vrednost = min(vrednost, nova_vrednost)
                beta = min(beta, vrednost)
                if beta < alfa:
                    break
                if vrednost == nova_vrednost:
                    najbolji_potez = potez
                if proteklo_vreme >= 2.5:
                    break
            if najbolji_potez == '':
                najbolji_potez = Tabla(cvor_stabla._vrednost, 1).validni_potezi_faza1(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme

    def minimax2(igra, tabla, dubina, hash_map, proteklo_vreme, cvor_stabla, igrac, drugi_igrac, alfa = -10000000000, beta = 10000000000):
        vreme = time()
        if dubina == 0:             #bazni slucaj
            try:
                vrednost = hash_map[tabla]
            except:
                vrednost = heuristika(tabla, 2, igrac)
                privremena = Tabla(cvor_stabla._vrednost)
                hash_map[tabla] = vrednost, cvor_stabla._vrednost, privremena.validni_potezi_faza1
        proteklo_vreme += time() - vreme
        return vrednost, None, proteklo_vreme               #vraca vrednost, najbolji potez i vreme koje je proteklo do sad

    def igraj(self, stablo, hesmapa):
        import main
        for i in range(9):                  #faza 1
            print()
            print("Kompjuter je na potezu!")
            print()
            potez = Tabla(self.kompjuter_potez_faza1(stablo, hesmapa, i))
            self._trenutno_stanje = potez
            for dete in stablo._trenutni._deca:
                if dete == potez:
                    stablo._trenutni = dete
            self._na_potezu = "■"
            print()
            print("Vi ste na potezu!")
            print()
            potezi = self._trenutno_stanje.validni_potezi_faza1("■", "potezi_koordinate")
            print("Mogući potezi su: ")
            for i in range(1, len(potezi)+1):
                print(str(i) + ". " + potezi[i-1])
            potez=-3
            while potez not in range(1, len(potezi)+1):
                potez = int(input("Unesite redni broj poteza koji želite da odigrate: "))
            gde = main.koordinata_u_poziciju_faza1(potezi[potez-1])
            novo_stanje = Tabla(main.nova_lista_faza1(self._trenutno_stanje._izgled, "■", gde), 1)
            self._trenutno_stanje = novo_stanje
            self._na_potezu = "▢"
        while heuristika.pobednicka_konfiguracija() != 1000 or heuristika.pobednicka_konfiguranica != -1000:    #faza 2
            if self._na_potezu == "▢":
                print()
                print("Kompjuter je na potezu!")
                print()
                self.kompjuter_potez(stablo, hesmapa)
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
