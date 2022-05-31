from mice.tabla import Tabla

def heuristika(cvor, faza, boja, gde=0):
    from main import pozicija_u_koordinatu, koordinata_u_poziciju, koordinata_u_poziciju_faza1, nova_lista, nova_lista_faza1
    if cvor._vrednost == []:
        return -1000000000000000000
    if boja == "■":
            boja2 = "▢"
    else:
        boja2 = "■"
    if faza == 1:
        blokirane = broj_blokiranih_figura(cvor, boja)
        pioni = broj_piona(cvor, boja)
        dvojke = broj_dvojki(cvor, boja)-broj_dvojki(cvor, boja2)
        trojke = broj_trojki(cvor, boja)-broj_trojki(cvor, boja2)
        mobilnost = mobilnost_piona(cvor, boja) - mobilnost_piona(cvor, boja2)
        # vrednost_pozicije = pozicija(gde)
        stanje_table = blokirane*20 + pioni*5 + mobilnost*10 - broj_mlinova(cvor, boja2)*3 + dvojke*25# +novi_mlinovi*20 + broj_mlinova_na_tabli*15 + trojke*30
        return stanje_table
    else:
        novi_mlinovi = novi_mlin(cvor, boja) 
        broj_mlinova_na_tabli = broj_mlinova(cvor, boja) - broj_mlinova(cvor, boja2)
        blokirane = broj_blokiranih_figura(cvor, boja)
        pioni = broj_piona(cvor, boja)
        dvojke = broj_dvojki(cvor, boja)-broj_dvojki(cvor, boja2)
        trojke = broj_trojki(cvor, boja)-broj_trojki(cvor, boja2)
        return novi_mlinovi*30 + broj_mlinova_na_tabli*15 + blokirane*15 + pioni*5 + nova_prilika_za_mlin(cvor, boja)*25 + dupli_mlin(cvor, boja)*40 + pobednicka_konfiguracija(cvor, boja)

def pozicija(gde):
    if gde in [5, 11, 14, 20]:
        return 50
    elif gde in [1, 3, 24, 22, 4, 6, 19, 21, 7, 9, 16, 18]:
        return 15
    else:
        return 30

def mobilnost_piona(cvor, boja):
    mobilnost = len(Tabla(cvor._vrednost, 1, boja).validni_potezi_faza1(boja, "broj"))
    return mobilnost

def paralelni_mlinovi(cvor, boja):
    paralelni = 0
    for j in range(1, 8, 2):
        if j==7:
            sledece = 0
        else:
            sledece = j+1
        if boja == "■":
            boja2 = "▢"
        else:
            boja2 = "■"
        if cvor._vrednost[1][j]=="x" and cvor._vrednost[0][sledece]==cvor._vrednost[0][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[0][j]==boja:
            paralelni += 1
        elif cvor._vrednost[1][j]=="x" and cvor._vrednost[0][sledece]==cvor._vrednost[0][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[0][j]==boja2:
            paralelni -= 1
        elif cvor._vrednost[0][j] == "x" and cvor._vrednost[0][sledece]==cvor._vrednost[0][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[1][j]==boja:
            paralelni += 1
        elif cvor._vrednost[0][j] == "x" and cvor._vrednost[0][sledece]==cvor._vrednost[0][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[1][j]==boja2:
            paralelni -= 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[2][sledece]==cvor._vrednost[2][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[2][j]==boja:
            paralelni += 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[2][sledece]==cvor._vrednost[2][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[2][j]==boja2:
            paralelni -= 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[2][sledece]==cvor._vrednost[2][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[1][j]==boja:
            paralelni += 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[2][sledece]==cvor._vrednost[2][j-1]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==cvor._vrednost[1][j]==boja2:
            paralelni -= 1
    return paralelni

def novi_mlin(cvor, boja):     #vraca brojcanu vrednost koja je broj mlinova napravljenih u ovom potezu
    if cvor._vrednost == [["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x", "x", "x", "x"]]:
        return 0
    k = broj_mlinova(cvor, boja) - broj_mlinova(cvor._roditelj, boja)
    if k > 0:
        return k
    else:
        broj_novih_mlinova = 0
        for i in range(3):
            for j in range(1, 8, 2):
                k=j-1
                l=j+1
                if j==7:
                    l=0
                if cvor._vrednost[i][j] == cvor._vrednost[i][k] == cvor._vrednost[i][l] == boja:
                    if cvor._roditelj._vrednost[i][j] == cvor._roditelj._vrednost[i][k] == cvor._roditelj._vrednost[i][l] == boja:
                        pass
                    else:
                        broj_novih_mlinova += 1
        for j in range(1, 8, 2):
            if cvor._vrednost[0][j] == cvor._vrednost[1][j] == cvor._vrednost[2][j] == boja:
                if cvor._vrednost[0][j] == cvor._vrednost[1][j] == cvor._vrednost[2][j] == boja:
                    pass
                else:
                    broj_novih_mlinova +=1
        return broj_novih_mlinova


def broj_mlinova(cvor, boja):          #vraca broj nasih mlinova minus broj mlinova suparnika
    broj_mlinova = 0
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    for i in range(3):
        for j in range(1, 8, 2):
            k=j-1
            l=j+1
            if j==7:
                l=0
            if cvor._vrednost[i][j] == cvor._vrednost[i][k] == cvor._vrednost[i][l] == boja:
                broj_mlinova += 1
            elif cvor._vrednost[i][j] == cvor._vrednost[i][k] == cvor._vrednost[i][l] == boja2:
                broj_mlinova -= 1
    for j in range(1, 8, 2):
        if cvor._vrednost[0][j] == cvor._vrednost[1][j] == cvor._vrednost[2][j] == boja:
            broj_mlinova +=1
        elif cvor._vrednost[0][j] == cvor._vrednost[1][j] == cvor._vrednost[2][j] == boja2:
            broj_mlinova -= 1
    return broj_mlinova

def broj_blokiranih_figura(cvor, boja):           #vraca broj blokiranih figura minus od suparnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    broj_blokiranih_figura = 0
    for i in range(3):
        for j in range(8):
            sledece = j + 1
            prethodno = j - 1
            if j == 0:
                prethodno = 7
            elif j == 7:
                sledece = 0
            if cvor._vrednost[i][j] == boja2: #ako je protivnikova figurica tamo
                if cvor._vrednost[i][prethodno]==boja and cvor._vrednost[i][sledece]==boja:
                    if j in [0, 2, 4, 6]:
                        broj_blokiranih_figura -= 1
                    elif i  == 1 and cvor._vrednost[0][j] == cvor._vrednost[2][j] == boja:
                        broj_blokiranih_figura -= 1
                    elif cvor._vrednost[1][j] == boja:
                        broj_blokiranih_figura -= 1
            elif cvor._vrednost[i][j] == boja:   #ako je nasa figura tamo
                if cvor._vrednost[i][prethodno]==boja2 and cvor._vrednost[i][sledece]==boja2:
                    if j in [0, 2, 4, 6]:
                        broj_blokiranih_figura += 1
                    elif i  == 1 and cvor._vrednost[0][j] == cvor._vrednost[2][j] == boja2:
                        broj_blokiranih_figura += 1
                    elif cvor._vrednost[1][j] == boja2:
                        broj_blokiranih_figura += 1
    return broj_blokiranih_figura

def broj_piona(cvor, boja):            #vraca broj piona minus broj piona suparnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    pioni = 0
    for i in range(3):
        for j in range(8):
            if cvor._vrednost[i][j] == boja:
                pioni += 1
            elif cvor._vrednost[i][j] == boja2:
                pioni -= 1
    return pioni

def broj_dvojki(cvor, boja):           #vraca broj dvojki koje postoje na tabli za jednu boju
    broj_dvojki = 0
    for i in range(3):
        for j in range(1, 8, 2):
            sledece = j + 1
            prethodno = j - 1
            if j == 7:
                sledece = 0
            if cvor._vrednost[i][j] == boja:
                if cvor._vrednost[i][prethodno] == "x" and cvor._vrednost[i][sledece] == boja:
                    broj_dvojki += 1
                elif cvor._vrednost[i][prethodno] == boja and cvor._vrednost[i][sledece] == "x":
                    broj_dvojki += 1
            elif cvor._vrednost[i][j] == "x":
                if cvor._vrednost[i][prethodno] == boja and cvor._vrednost[i][sledece] == boja:
                    broj_dvojki += 1
    for j in range(1, 8, 2):
        if cvor._vrednost[1][j] == "x" and cvor._vrednost[0][j] == cvor._vrednost[2][j] == boja:
                broj_dvojki += 1
        elif cvor._vrednost[0][j] == "x" and cvor._vrednost[1][j] == cvor._vrednost[2][j] == boja:
                broj_dvojki += 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[1][j] == cvor._vrednost[0][j] == boja:
                broj_dvojki += 1
    return broj_dvojki

def broj_trojki(cvor, boja):           #vraca broj trojki koje postoje na tabli za jednu boju, važi za prvu fazu
    dva = broj_dvojki(cvor, boja)
    return ( dva * (dva - 1) ) / 2

def nova_prilika_za_mlin(cvor, boja):       #funkcija vraca broj novih prilika za mlin minus za protivnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    k = broj_dvojki(cvor, boja) - broj_dvojki(cvor._roditelj, boja)
    l = broj_dvojki(cvor, boja2) - broj_dvojki(cvor._roditelj, boja2)
    return k - l
    
def dupli_mlin(cvor, boja):        #vraca razliku nasih i protivnikovih mlinova
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    broj_duplih = 0
    for i in range(3):
        for j in range(0, 8, 2):
            sledece = j + 1
            sledece2 = j + 2
            prethodno = j - 1
            prethodno2 = j - 2
            if j == 0:
                prethodno = 7
                prethodno2 = 6
            elif j == 6:
                sledece2 = 0
            if cvor._vrednost[i][j] == "x":         #proveravamo da li ima "L bez coska"
                if cvor._vrednost[i][prethodno]==cvor._vrednost[i][prethodno2]==cvor._vrednost[i][sledece]==cvor._vrednost[i][sledece2]==boja:
                    broj_duplih += 1
                elif cvor._vrednost[i][prethodno]==cvor._vrednost[i][prethodno2]==cvor._vrednost[i][sledece]==cvor._vrednost[i][sledece2]==boja2:
                    broj_duplih -= 1
    for j in range(1, 8, 2):
        if j==7:
            sledece=0
        else:
            sledece = j + 1
        if cvor._vrednost[1][j]=="x" and cvor._vrednost[0][j]==cvor._vrednost[2][j]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==boja:
            broj_duplih += 1        #"+" bez sredine
        elif cvor._vrednost[1][j]=="x" and cvor._vrednost[0][j]==cvor._vrednost[2][j]==cvor._vrednost[1][sledece]==cvor._vrednost[1][j-1]==boja2:
            broj_duplih -= 1
        elif cvor._vrednost[0][j] == "x" and cvor._vrednost[0][j-1]==cvor._vrednost[0][sledece]==cvor._vrednost[1][j]==cvor._vrednost[2][j]==boja:
            broj_duplih += 1        #"T bez preseka"
        elif cvor._vrednost[0][j] == "x" and cvor._vrednost[0][j-1]==cvor._vrednost[0][sledece]==cvor._vrednost[1][j]==cvor._vrednost[2][j]==boja2:
            broj_duplih -= 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[2][j-1]==cvor._vrednost[2][sledece]==cvor._vrednost[1][j]==cvor._vrednost[0][j]==boja:
            broj_duplih += 1
        elif cvor._vrednost[2][j] == "x" and cvor._vrednost[2][j-1]==cvor._vrednost[2][sledece]==cvor._vrednost[1][j]==cvor._vrednost[0][j]==boja2:
            broj_duplih -= 1
    return broj_duplih

def pobednicka_konfiguracija(cvor, boja):      #vraca 1000 za pobednicku konfig, a nula ako nije, -1000 ako je gubitak
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    if len(Tabla(cvor._vrednost, 2, boja).validni_potezi_faza2(boja2, "broj")) == 0 or broj_piona(cvor, boja2) == 2:
        return 1000
    elif len(Tabla(cvor._vrednost, 2, boja).validni_potezi_faza2(boja, "broj")) == 0 or broj_piona(cvor, boja) == 2:
        return -1000
    else:
        return 0
