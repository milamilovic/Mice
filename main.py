#Autor: Mila Milović SV22-2021
#Projekat iz predmeta Algoritmi i strukture podataka
#Program za igru mice (Nine Men's Morris)

import strukture_podataka
from strukture_podataka.stablo import *
from strukture_podataka.hashmap import *
import mice
from mice.igra import *
from copy import deepcopy

def Pravila():
    print()
    print()
    print("-------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Dobrodošli u igru mice!")
    print()
    print("Kada je vaš red da igrate biće ispisani svi mogući potezi u formatu 'n. polje1 ---> polje2'")
    print("Treba da upišete redni broj poteza koji želite da odigrate (n)")
    print("'polje1' predstavlja polje sa pionom koji se pomera, a 'polje2' polje na koje se taj pion pomera")
    print("Vi ste crni igrač. Srećno!")
    print()
    print("-------------------------------------------------------------------------------------------------------------------------")
    print()
    print()

def pozicija_u_koordinatu(koje, gde):       #dobijemo brojeve do 1 do 24 koji pion gde pomeramo
    koordinate = ["A1", "A4", "A7", "B2", "B4", "B6", "C3", "C4", "C5", "D1", "D2", "D3", "D5", "D6", "D7", "E3", "E4", "E5", "F2", "F4", "F6", "G1", "G4", "G7"]
    koji_pion = koordinate[koje-1]
    gde_pomeramo = koordinate[gde - 1]
    return koji_pion + " ---> " + gde_pomeramo

def pozicija_u_koordinatu_faza1(gde):
    koordinate = ["A1", "A4", "A7", "B2", "B4", "B6", "C3", "C4", "C5", "D1", "D2", "D3", "D5", "D6", "D7", "E3", "E4", "E5", "F2", "F4", "F6", "G1", "G4", "G7"]
    gde_pomeramo = koordinate[gde - 1]
    return "Postaviti pion na koordinatu " + gde_pomeramo

def koordinata_u_poziciju_faza1(potez):
    koji_pion = potez[-2:]
    pozicije = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    koordinate = ["A1", "A4", "A7", "B2", "B4", "B6", "C3", "C4", "C5", "D1", "D2", "D3", "D5", "D6", "D7", "E3", "E4", "E5", "F2", "F4", "F6", "G1", "G4", "G7"]
    koji = pozicije[koordinate.index(koji_pion)]
    return koji

def koordinata_u_poziciju(potez):
    koji_pion = potez[:2]
    gde_pomeramo = potez[-2:]
    pozicije = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    koordinate = ["A1", "A4", "A7", "B2", "B4", "B6", "C3", "C4", "C5", "D1", "D2", "D3", "D5", "D6", "D7", "E3", "E4", "E5", "F2", "F4", "F6", "G1", "G4", "G7"]
    koji = pozicije[koordinate.index(koji_pion)]
    gde = pozicije[koordinate.index(gde_pomeramo)]
    return koji, gde

def nova_lista(stara_lista, koja_pozicija, gde):        #pretpostavlja se da je ispravno poslato tj da je gde slobodna
    lista=[[], [], []]
    for i in len(stara_lista):
        for j in len(stara_lista[i]):
            lista[i].append(stara_lista[i][j])
    kojai = koja_pozicija//8
    kojaj = koja_pozicija%8
    gdei = gde//8
    gdej = gde%8
    lista[kojai][kojaj], lista[gdei][gdej] = lista[gdei][gdej], lista[kojai][kojaj]
    return lista

def nova_lista_faza1(stara_lista, boja, gde):
    lista = [[], [], []]
    for i in range(len(stara_lista)):
        for j in range(len(stara_lista[i])):
            lista[i].append(stara_lista[i][j])
    gdei = gde//8
    gdej = gde%8
    lista[gdei][gdej] = boja
    return lista

if __name__ == "__main__":
    Pravila()
    i = mice.igra.Igra()
    koren = strukture_podataka.stablo.CvorStabla(deepcopy(i._trenutno_stanje))
    stablo = strukture_podataka.stablo.Stablo(koren)
    for potez in i._trenutno_stanje.validni_potezi_faza1(i._na_potezu, "broj"):
        potencijalna_tabla = deepcopy(potez)
        stablo.dodaj_dete(koren, potencijalna_tabla)
    hash_map = strukture_podataka.hashmap.HashMap()
    boja = "▢"
    i.igraj(stablo, hash_map)
    # boja="55555"
    # while boja not in ["1", "2"]:
    #     if boja != "55555":
    #         print("Niste uneli validnu opciju! Pokušajte ponovo!")
    #     print("Unesite broj 1 ako želite da igrate kao beli igrač, a 2 ako želite da igrate kao crni:")
    #     boja = input(">>")
    # if boja == "1":
    #     boja, boja2 = "▢", "■"
    # else:
    #      boja, boja2 = "■", "▢"
