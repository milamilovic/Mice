#Autor: Mila Milović SV22-2021
#Projekat iz predmeta Algoritmi i strukture podataka
#Program za igru mice (Nine Men's Morris)

import mice

def Pravila():
    print("Dobrodošli u igru mice!")
    print("")

def nova_lista(stara_lista, koja_pozicija, gde):
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

if __name__ == "__main__":
    Pravila()
    boja="55555"
    while boja not in ["1", "2"]:
        if boja != "55555":
            print("Niste uneli validnu opciju! Pokušajte ponovo!")
        print("Unesite broj 1 ako želite da igrate kao beli igrač, a 2 ako želite da igrate kao crni:")
        boja = input(">>")
    if boja == "1":
        boja, boja2 = "▢", "■"
    else:
        boja, boja2 = "■", "▢"
    dubina = 0
    while dubina not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        if dubina != 0:
            print("Niste uneli validnu opciju! Pokušajte ponovo!")
        dubina=input("Unesite broj izmedju 1 i 8 koji označava do koje dubine želite da se ispituje dalji dok igre(stablo igre): ")
    dubina = int(dubina)