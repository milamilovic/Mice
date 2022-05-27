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
    koordinate = ["A1", "A4", "A7", "D7", "G7", "G4", "G1", "D1", "B2", "B4", "B6", "D6", "F6", "F4", "F2", "D2", "C3", "C4", "C5", "D5", "E5", "E4", "E3", "D3"]
    koji_pion = koordinate[koje-1]
    gde_pomeramo = koordinate[gde - 1]
    return koji_pion + " ---> " + gde_pomeramo

def pozicija_u_koordinatu_faza1(gde):
    koordinate = ["A1", "A4", "A7", "D7", "G7", "G4", "G1", "D1", "B2", "B4", "B6", "D6", "F6", "F4", "F2", "D2", "C3", "C4", "C5", "D5", "E5", "E4", "E3", "D3"]
    gde_pomeramo = koordinate[gde - 1]
    return "Postaviti pion na koordinatu " + gde_pomeramo

def koordinata_u_poziciju_faza1(potez):
    koji_pion = potez[-2:]
    pozicije = [1, 2, 3, 15, 24, 23, 22, 10, 4, 5, 6, 14, 21, 20, 19, 11, 7, 8, 9, 13, 18, 17, 16, 12]
    koordinate = ["A1", "A4", "A7", "D7", "G7", "G4", "G1", "D1", "B2", "B4", "B6", "D6", "F6", "F4", "F2", "D2", "C3", "C4", "C5", "D5", "E5", "E4", "E3", "D3"]
    koji = pozicije[koordinate.index(koji_pion)]
    return koji

def koordinata_u_poziciju(potez):
    koji_pion = potez[:2]
    gde_pomeramo = potez[-2:]
    pozicije = [1, 2, 3, 15, 24, 23, 22, 10, 4, 5, 6, 14, 21, 20, 19, 11, 7, 8, 9, 13, 18, 17, 16, 12]
    koordinate = ["A1", "A4", "A7", "D7", "G7", "G4", "G1", "D1", "B2", "B4", "B6", "D6", "F6", "F4", "F2", "D2", "C3", "C4", "C5", "D5", "E5", "E4", "E3", "D3"]
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
    # potezip = i._trenutno_stanje.validni_potezi_faza1(i._na_potezu, "broj")
    # potezi = []
    # for potez in potezip:
    #     potezi.append(potez._izgled)
    # for potez in potezi:
    #     stablo.dodaj_dete(koren, CvorStabla(potez))
    hash_map = strukture_podataka.hashmap.HashMap()
    boja = "▢"
    pocetak = input("Pritisnite bilo koji taster za pocetak igre: ")
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
