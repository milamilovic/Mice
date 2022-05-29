from mice.heuristika import heuristika, pozicija, pobednicka_konfiguracija
from mice.tabla import Tabla
from copy import deepcopy
from time import time
from main import nova_lista, nova_lista_faza1
from strukture_podataka.stablo import CvorStabla

class Igra(object):

    __slots__ = ["_trenutno_stanje", "_na_potezu"]

    def __init__(self):
        self._trenutno_stanje = Tabla([["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"]], 1, "▢")
        self._na_potezu = "▢"           #kompjuter prvi igra
        
    def uklanjanje_piona(self, tabla, faza, boja, hash_map):               #prosledi se trenutna tabla i vrati senajbolji potez
        moguci_potezi = len(tabla.validno_uklanjanje_piona(boja, "broj"))
        if moguci_potezi<=5:
            dubina = 5
        elif moguci_potezi<=8:
            dubina  = 4
        elif moguci_potezi>8:
            dubina = 3
        proteklo_vreme = 0
        if boja == "▢":
            boja2 = "■"
        else:
            boja2 = "▢"
        koren = CvorStabla(tabla)
        for tabla in tabla.validno_uklanjanje_piona(boja, "broj"):
            koren._dodaj_dete_(tabla)
        potez = self.minimax_uklanjanje(self, tabla, faza, dubina, hash_map, koren,proteklo_vreme, boja, boja2)
        return potez

    def minimax_uklanjanje(self, tabla, faza, dubina, hash_map, cvor, proteklo_vreme, igrac, drugi_igrac, alfa = -10000000000, beta = 10000000000):
        vreme = time()
        if dubina == 0:       #bazni slucaj
            vreme = time()
            try:
                vrednost = hash_map[tabla][0]
            except:
                vrednost = heuristika(cvor, faza, drugi_igrac)
                hash_map[tabla._izgled] = vrednost, Tabla([], faza, igrac), proteklo_vreme
                proteklo_vreme += time() - vreme
                naj_potez = Tabla([], faza, igrac)
            return vrednost, naj_potez, proteklo_vreme           #vraca vrednost, najbolji potez i vreme koje je proteklo do sad
        if igrac == "▢":            #kompjuter, maximizer
            vrednost = -10000000000
            najbolji_potez = Tabla([], 2, igrac)
            potezi = Tabla(cvor._vrednost, 2, igrac).validno_uklanjanje_piona(igrac, "broj")
            for potez in potezi:
                cvoric = CvorStabla(potez._izgled)
                if cvoric not in cvor._deca:
                    if cvoric._vrednost != cvor._vrednost:
                        cvor._dodaj_dete_(cvoric)
            for potez in potezi:
                vrednosti_dece = []
                if cvor._deca == []:
                    for tabla in Tabla(cvor._vrednost, faza, self._na_potezu).validno_uklanjanje_piona(self._na_potezu, "broj"):
                        cvor._dodaj_dete_(CvorStabla(tabla))
                for dete in cvor._deca:
                    vrednosti_dece.append(dete)
                for detence in range(len(vrednosti_dece)):
                    if potez._izgled == vrednosti_dece[detence]._vrednost:
                        privremeni_cvor = vrednosti_dece[detence]
                        break
                    else:
                        privremeni_cvor = CvorStabla(potez._izgled)
                        if privremeni_cvor in cvor._deca:
                            cvor._dodaj_dete_(privremeni_cvor)
                try:
                    nova_vrednost, naj_potez, vreme = hash_map[potez]
                    if naj_potez == Tabla([], faza, igrac):
                        hash_map['3'] = 2
                except:
                    start = time()
                    try:
                        x = cvor
                    except:
                        pass
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax_uklanjanje(potez, faza, dubina - 1, hash_map, privremeni_cvor, proteklo_vreme, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla._izgled] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start
                if nova_vrednost > vrednost:
                    vrednost = nova_vrednost
                    if vrednost > alfa:
                        alfa = vrednost
                    najbolji_potez = potez
                # vrednost = max(vrednost, nova_vrednost)
                # alfa = max(alfa, vrednost)
                # if vrednost == nova_vrednost:
                #     najbolji_potez = potez
                if beta <= alfa:
                    break
                # if proteklo_vreme > 2.5:
                #     break
            if najbolji_potez._izgled == cvor._vrednost:
                pass
            if najbolji_potez._izgled == []:
                pass
            if najbolji_potez == Tabla([], 2, igrac):
                najbolji_potez = Tabla(cvor._vrednost, 2, igrac).validno_uklanjanje_piona(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme
        else:               #igrac, minimizer
            vrednost = 10000000000
            najbolji_potez = Tabla([], 2, igrac)
            potezi = []
            for potez in Tabla(cvor._vrednost, faza, igrac).validno_uklanjanje_piona(igrac, "broj"):
                potezi.append(potez)
                cvoric = CvorStabla(potez._izgled)
                if cvoric not in cvor._deca:
                    cvor._dodaj_dete_(cvoric)
            for potez in potezi:
                vrednosti_dece = []
                for dete in cvor._deca:
                    vrednosti_dece.append(dete)
                for detence in range(len(vrednosti_dece)):
                    if potez._izgled == vrednosti_dece[detence]._vrednost:
                        privremeni_cvor = vrednosti_dece[detence]
                        break
                    else:
                        privremeni_cvor = CvorStabla(potez._izgled)
                        if privremeni_cvor in cvor._deca:
                            cvor._dodaj_dete_(privremeni_cvor)
                try:
                    nova_vrednost, naj_potez, vreme = hash_map[potez]
                except:
                    start = time()
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax_uklanjanje(potez, faza, dubina - 1, hash_map, privremeni_cvor, proteklo_vreme, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla._izgled] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start
                if nova_vrednost < vrednost:
                    vrednost = nova_vrednost
                    if vrednost < beta:
                        beta = vrednost
                    najbolji_potez = potez
                if beta <= alfa:
                    break
                # if proteklo_vreme > 2.5:
                #     break
            if najbolji_potez == Tabla([], faza, igrac):
                najbolji_potez = Tabla(cvor._vrednost, 1, igrac).validno_uklanjanje_piona(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme

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
        # if broj_postavljenih == 0:
        #     return Tabla(nova_lista_faza1([["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"]], self._na_potezu, 5), 1, self._na_potezu)
        proteklo_vreme = 0
        dubina = self.varijabilna_dubina(self._trenutno_stanje, proteklo_vreme)
        potez = self.minimax1(broj_postavljenih, [self._trenutno_stanje, 0], dubina, hash_map, proteklo_vreme, stablo._trenutni, "▢", "■")[1][0]
        return potez

    def kompjuter_potez(self, stablo, hash_map):
        proteklo_vreme = 0
        dubina = self.varijabilna_dubina(self._trenutno_stanje, proteklo_vreme)
        potez = self.minimax2(self._trenutno_stanje, dubina, hash_map, proteklo_vreme, stablo._trenutni, "▢", "■")[1]
        return potez

    def minimax1(self, broj_postavljenih, tabla, dubina, hash_map, proteklo_vreme, cvor_stabla, igrac, drugi_igrac, alfa = -10000000000, beta = 10000000000):
        if dubina == 0 or broj_postavljenih == 10:       #bazni slucaj ili se prebacujemo na minimax2 jer je prosla 1. faza
            vreme = time()
            if dubina == 0:
                try:
                    vrednost = hash_map[tabla[0]][0]
                except:
                    tabla_trenutna = cvor_stabla._vrednost
                    if cvor_stabla._roditelj == None:
                        return 0, [Tabla([], 1, igrac), 0], proteklo_vreme
                    tabla_roditelja = cvor_stabla._roditelj._vrednost
                    if tabla_roditelja == tabla_trenutna:
                        pass
                    pozicija = -1
                    for i in range(3):
                        for j in range(8):
                            pozicija += 1
                            if tabla_trenutna[i][j] != tabla_roditelja[i][j]:
                                trazena = pozicija
                                break
                    pozicije = [1, 2, 3, 15, 24, 23, 22, 10, 4, 5, 6, 14, 21, 20, 19, 11, 7, 8, 9, 13, 18, 17, 16, 12]
                    gde = pozicije[trazena]
                    vrednost = heuristika(cvor_stabla, 1, drugi_igrac, gde)
                    privremena = Tabla(tabla_trenutna, 1, igrac)
                    hash_map[tabla[0]._izgled] = vrednost, [Tabla([], 1, igrac), 0], privremena.validni_potezi_faza1(igrac, "boja")
                    proteklo_vreme += time() - vreme
                    naj_potez = [Tabla([], 1, igrac), 0]
            elif broj_postavljenih == 10:
                vrednost, naj_potezic, proteklo_vreme = self.minimax2(tabla[0], dubina, hash_map, proteklo_vreme, cvor_stabla, igrac, drugi_igrac, alfa, beta)
                proteklo_vreme += time() - vreme
                naj_potez = [naj_potezic, 0]
            return vrednost, naj_potez, proteklo_vreme           #vraca vrednost, najbolji potez i vreme koje je proteklo do sad
        if igrac == "▢":            #kompjuter, maximizer
            vrednost = -10000000000
            najbolji_potez = [Tabla([], 1, igrac), 0]
            potezi = Tabla(cvor_stabla._vrednost, 1, igrac).validni_potezi_faza1(igrac, "broj")
            for potez in potezi:
                cvoric = CvorStabla(potez[0]._izgled)
                if cvoric not in cvor_stabla._deca:
                    if cvoric._vrednost != cvor_stabla._vrednost:
                        cvor_stabla._dodaj_dete_(cvoric)
            for potez in potezi:
                vrednosti_dece = []
                for dete in cvor_stabla._deca:
                    vrednosti_dece.append(dete)
                for detence in range(len(vrednosti_dece)):
                    if potez[0]._izgled == vrednosti_dece[detence]._vrednost:
                        cvor = vrednosti_dece[detence]
                        break
                    else:
                        cvor = CvorStabla(potez[0]._izgled)
                        if cvor in cvor_stabla._deca:
                            cvor_stabla._dodaj_dete_(cvor)
                try:
                    nova_vrednost, naj_potez, vreme = hash_map[potez[0]]
                    if naj_potez == [Tabla([], 1, igrac), 0]:
                        hash_map['3'] = 2
                except:
                    start = time()
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax1(broj_postavljenih + 1, potez, dubina - 1, hash_map, proteklo_vreme, cvor, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla[0]._izgled] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start
                if nova_vrednost > vrednost:
                    vrednost = nova_vrednost
                    if vrednost > alfa:
                        alfa = vrednost
                    najbolji_potez = potez
                # vrednost = max(vrednost, nova_vrednost)
                # alfa = max(alfa, vrednost)
                # if vrednost == nova_vrednost:
                #     najbolji_potez = potez
                if beta <= alfa:
                    break
                # if proteklo_vreme > 2.5:
                #     break
            if najbolji_potez[0]._izgled == cvor_stabla._vrednost:
                pass
            if najbolji_potez[0]._izgled == []:
                pass
            if najbolji_potez == [Tabla([], 1, igrac), 0]:
                najbolji_potez = Tabla(cvor_stabla._vrednost, 1, igrac).validni_potezi_faza1(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme
        else:               #igrac, minimizer
            vrednost = 10000000000
            najbolji_potez = [Tabla([], 1, igrac), 0]
            potezi = []
            for potez in Tabla(cvor_stabla._vrednost, 1, igrac).validni_potezi_faza1(igrac, "broj"):
                potezi.append(potez)
                cvoric = CvorStabla(potez[0]._izgled)
                if cvoric not in cvor_stabla._deca:
                    cvor_stabla._dodaj_dete_(cvoric)
            for potez in potezi:
                vrednosti_dece = []
                for dete in cvor_stabla._deca:
                    vrednosti_dece.append(dete)
                for detence in range(len(vrednosti_dece)):
                    if potez[0]._izgled == vrednosti_dece[detence]._vrednost:
                        cvor = vrednosti_dece[detence]
                        break
                    else:
                        cvor = CvorStabla(potez[0]._izgled)
                        if cvor in cvor_stabla._deca:
                            cvor_stabla._dodaj_dete_(cvor)
                try:
                    nova_vrednost, naj_potez, vreme = hash_map[potez[0]]
                except:
                    start = time()
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax1(broj_postavljenih + 1, potez, dubina - 1, hash_map, proteklo_vreme, cvor, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla[0]._izgled] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start
                if nova_vrednost < vrednost:
                    vrednost = nova_vrednost
                    if vrednost < beta:
                        beta = vrednost
                    najbolji_potez = potez
                if beta <= alfa:
                    break
                # if proteklo_vreme > 2.5:
                #     break
            if najbolji_potez == [Tabla([], 1, igrac), 0]:
                najbolji_potez = Tabla(cvor_stabla._vrednost, 1, igrac).validni_potezi_faza1(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme

    def minimax2(self, tabla, dubina, hash_map, proteklo_vreme, cvor_stabla, igrac, drugi_igrac, alfa = -10000000000, beta = 10000000000):
        vreme = time()
        if dubina == 0:       #bazni slucaj ili se prebacujemo na minimax2 jer je prosla 1. faza
            vreme = time()
            try:
                vrednost = hash_map[tabla][0]
            except:
                if cvor_stabla._roditelj == None:
                    return 0, Tabla([], 2, igrac), proteklo_vreme
                vrednost = heuristika(cvor_stabla, 2, drugi_igrac)
                hash_map[tabla._izgled] = vrednost, Tabla([], 2, igrac), proteklo_vreme
                proteklo_vreme += time() - vreme
                naj_potez = Tabla([], 2, igrac)
            return vrednost, naj_potez, proteklo_vreme           #vraca vrednost, najbolji potez i vreme koje je proteklo do sad
        if igrac == "▢":            #kompjuter, maximizer
            vrednost = -10000000000
            najbolji_potez = Tabla([], 2, igrac)
            potezi = Tabla(cvor_stabla._vrednost, 2, igrac).validni_potezi_faza2(igrac, "broj")
            for potez in potezi:
                cvoric = CvorStabla(potez._izgled)
                if cvoric not in cvor_stabla._deca:
                    if cvoric._vrednost != cvor_stabla._vrednost:
                        cvor_stabla._dodaj_dete_(cvoric)
            for potez in potezi:
                if dubina == 2:
                    pass
                vrednosti_dece = []
                if cvor_stabla._deca == []:
                    for tabla in Tabla(cvor_stabla._vrednost, 2, self._na_potezu).validni_potezi_faza2(self._na_potezu, "broj"):
                        cvor_stabla._dodaj_dete_(CvorStabla(tabla))
                for dete in cvor_stabla._deca:
                    vrednosti_dece.append(dete)
                for detence in range(len(vrednosti_dece)):
                    if potez._izgled == vrednosti_dece[detence]._vrednost:
                        cvor = vrednosti_dece[detence]
                        break
                    else:
                        cvor = CvorStabla(potez._izgled)
                        if cvor in cvor_stabla._deca:
                            cvor_stabla._dodaj_dete_(cvor)
                try:
                    nova_vrednost, naj_potez, vreme = hash_map[potez]
                    if naj_potez == Tabla([], 2, igrac):
                        hash_map['3'] = 2
                except:
                    start = time()
                    try:
                        x = cvor
                    except:
                        pass
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax2(potez, dubina - 1, hash_map, proteklo_vreme, cvor, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla._izgled] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start
                if nova_vrednost > vrednost:
                    vrednost = nova_vrednost
                    if vrednost > alfa:
                        alfa = vrednost
                    najbolji_potez = potez
                # vrednost = max(vrednost, nova_vrednost)
                # alfa = max(alfa, vrednost)
                # if vrednost == nova_vrednost:
                #     najbolji_potez = potez
                if beta <= alfa:
                    break
                # if proteklo_vreme > 2.5:
                #     break
            if najbolji_potez._izgled == cvor_stabla._vrednost:
                pass
            if najbolji_potez._izgled == []:
                pass
            if najbolji_potez == Tabla([], 2, igrac):
                najbolji_potez = Tabla(cvor_stabla._vrednost, 2, igrac).validni_potezi_faza2(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme
        else:               #igrac, minimizer
            vrednost = 10000000000
            najbolji_potez = Tabla([], 2, igrac)
            potezi = []
            for potez in Tabla(cvor_stabla._vrednost, 2, igrac).validni_potezi_faza2(igrac, "broj"):
                potezi.append(potez)
                cvoric = CvorStabla(potez._izgled)
                if cvoric not in cvor_stabla._deca:
                    cvor_stabla._dodaj_dete_(cvoric)
            for potez in potezi:
                vrednosti_dece = []
                for dete in cvor_stabla._deca:
                    vrednosti_dece.append(dete)
                for detence in range(len(vrednosti_dece)):
                    if potez._izgled == vrednosti_dece[detence]._vrednost:
                        cvor = vrednosti_dece[detence]
                        break
                    else:
                        cvor = CvorStabla(potez._izgled)
                        if cvor in cvor_stabla._deca:
                            cvor_stabla._dodaj_dete_(cvor)
                try:
                    nova_vrednost, naj_potez, vreme = hash_map[potez]
                except:
                    start = time()
                    nova_vrednost, naj_potez, rendomvremekojeminetreba = self.minimax2(potez, dubina - 1, hash_map, proteklo_vreme, cvor, drugi_igrac, igrac, alfa, beta)
                    hash_map[tabla._izgled] = nova_vrednost, naj_potez, rendomvremekojeminetreba
                    proteklo_vreme += time() - start
                if nova_vrednost < vrednost:
                    vrednost = nova_vrednost
                    if vrednost < beta:
                        beta = vrednost
                    najbolji_potez = potez
                if beta <= alfa:
                    break
                # if proteklo_vreme > 2.5:
                #     break
            if najbolji_potez == Tabla([], 2, igrac):
                najbolji_potez = Tabla(cvor_stabla._vrednost, 1, igrac).validni_potezi_faza2(igrac, "broj")[0]
            return vrednost, najbolji_potez, proteklo_vreme

    def igraj(self, stablo, hesmapa):
        import main
        for i in range(9):                  #faza 1
            print()
            print("Kompjuter je na potezu!")
            print()
            potez = self.kompjuter_potez_faza1(stablo, hesmapa, i)
            self._trenutno_stanje = potez
            for dete in stablo._trenutni._deca:
                if dete._vrednost == potez._izgled:
                    stablo._trenutni = dete
                    break
            if stablo._trenutni._deca == []:
                for stanje in potez.validni_potezi_faza1("■", "broj"):
                    stablo._trenutni._dodaj_dete_(CvorStabla(stanje[0]._izgled))
            self._na_potezu = "■"
            print("Kompjuter je igrao! Stanje table je sledeće: ")
            print(self._trenutno_stanje)
            print()
            print("Vi ste na potezu!")
            print()
            potezi = self._trenutno_stanje.validni_potezi_faza1("■", "potezi_koordinate")
            print("Mogući potezi su: ")
            for i in range(1, len(potezi)+1):
                print(str(i) + ". " + potezi[i-1])
            potez=-3
            while potez not in range(1, len(potezi)+1):
                try:
                    potez = int(input("Unesite redni broj poteza koji želite da odigrate: "))
                except:
                    pass
            gde = main.koordinata_u_poziciju_faza1(potezi[potez-1])
            novo_stanje = Tabla(main.nova_lista_faza1(self._trenutno_stanje._izgled, "■", gde), 1, self._na_potezu)
            self._trenutno_stanje = novo_stanje
            self._na_potezu = "▢"
            for dete in stablo._trenutni._deca:
                if dete._vrednost == novo_stanje._izgled:
                    stablo._trenutni = dete
                    if stablo._trenutni._deca == []:
                        potezi = self._trenutno_stanje.validni_potezi_faza1(self._na_potezu, "broj")
                        for stanje in potezi:
                            stablo._trenutni._dodaj_dete_(CvorStabla(stanje[0]._izgled))
                    break
            print("Odigrali ste Vaš potez! Stanje table je sledeće: ")
            print(self._trenutno_stanje)
        while pobednicka_konfiguracija(stablo._trenutni, self._na_potezu) != 1000 or pobednicka_konfiguracija(stablo._trenutni, self._na_potezu) != -1000:    #faza 2
            if self._na_potezu == "▢":
                print()
                print("Kompjuter je na potezu!")
                print()
                potez = self.kompjuter_potez(stablo, hesmapa)
                self._trenutno_stanje = potez
                for dete in stablo._trenutni._deca:
                    if dete._vrednost == potez._izgled:
                        stablo._trenutni = dete
                        break
                if stablo._trenutni._deca == []:
                    for stanje in potez.validni_potezi_faza2("■", "broj"):
                        stablo._trenutni._dodaj_dete_(CvorStabla(stanje[0]._izgled))
                self._na_potezu = "■"
                print("Kompjuter je igrao! Stanje table je sledeće: ")
                print(self._trenutno_stanje)
            else:
                print()
                print("Vi ste na potezu!")
                print()
                potezi = self._trenutno_stanje.validni_potezi_faza2("■", "potezi_koordinate")
                print("Mogući potezi su: ")
                for i in range(1, len(potezi)+1):
                    print(str(i) + ". " + potezi[i-1])
                potez=-3
                while potez not in range(1, len(potezi)+1):
                    try:
                        potez = int(input("Unesite redni broj poteza koji želite da odigrate: "))
                    except:
                        pass
                koji, gde = main.koordinata_u_poziciju(potezi[potez-1])
                novo_stanje = Tabla(main.nova_lista(self._trenutno_stanje._izgled, koji, gde), 2, self._na_potezu)
                self._trenutno_stanje = novo_stanje
                self._na_potezu = "▢"
                for dete in stablo._trenutni._deca:
                    if dete._vrednost == novo_stanje._izgled:
                        stablo._trenutni = dete
                        if stablo._trenutni._deca == []:
                            potezi = self._trenutno_stanje.validni_potezi_faza2(self._na_potezu, "broj")
                            for stanje in potezi:
                                stablo._trenutni._dodaj_dete_(CvorStabla(stanje[0]._izgled))
                        break
                print("Odigrali ste Vaš potez! Stanje table je sledeće: ")
                print(self._trenutno_stanje)
        if heuristika.pobednicka_konfiguracija(stablo._trenutni, 2) == 1000:
            print()
            print("Izgubili ste! Računar je pobedio!")
            print()
        elif heuristika.pobednicka_konfiguracija(stablo._trenutni, 2) == -1000:
            print()
            print("Pobedili ste!")
            print()
