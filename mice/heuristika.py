import main

def heuristika(tabla, faza, boja, gde=0):
    if boja == "■":
            boja2 = "▢"
    else:
        boja2 = "■"
    if faza == 1:
        stanje_table =  novi_mlin(tabla, boja)*20 + broj_mlinova(tabla, boja)*15 + broj_blokiranih_figura(tabla, boja)*10 + broj_piona(tabla, boja)*5 + (broj_dvojki(tabla, boja)-broj_dvojki(tabla, boja2))*25 + (broj_trojki(tabla, boja)-broj_trojki(tabla, boja2))*30
        vrednost_pozicije = pozicija(gde)
        return stanje_table + vrednost_pozicije*2
    else:
        return novi_mlin(tabla, boja)*30 + broj_mlinova(tabla, boja)*15 + broj_blokiranih_figura(tabla, boja)*15 + broj_piona(tabla, boja)*5 + nova_prilika_za_mlin(tabla, boja)*25 + dupli_mlin(tabla, boja)*40 + pobednicka_konfiguracija(tabla, boja)

def pozicija(gde):
    if gde in [5, 11, 14, 20]:
        return 50
    elif gde in [1, 3, 24, 22, 4, 6, 19, 21, 7, 9, 16, 18]:
        return 15
    else:
        return 30

def paralelni_mlinovi(tabla, boja):
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
        if tabla[1][j]=="x" and tabla[0][sledece]==tabla[0][j-1]==tabla[1][sledece]==tabla[1][j-1]==boja:
            paralelni += 1
        elif tabla[1][j]=="x" and tabla[0][sledece]==tabla[0][j-1]==tabla[1][sledece]==tabla[1][j-1]==boja2:
            paralelni -= 1
        elif tabla[0][j] == "x" and tabla[0][sledece]==tabla[0][j-1]==tabla[1][sledece]==tabla[1][j-1]==boja:
            paralelni += 1
        elif tabla[0][j] == "x" and tabla[0][sledece]==tabla[0][j-1]==tabla[1][sledece]==tabla[1][j-1]==boja2:
            paralelni -= 1
        elif tabla[2][j] == "x" and tabla[2][sledece]==tabla[2][j-1]==tabla[1][sledece]==tabla[1][j-1]==boja:
            paralelni += 1
        elif tabla[2][j] == "x" and tabla[2][sledece]==tabla[2][j-1]==tabla[1][sledece]==tabla[1][j-1]==boja2:
            paralelni -= 1

def novi_mlin(tabla, boja):     #vraca brojcanu vrednost koja je broj mlinova napravljenih u ovom potezu
    return tabla.broj_mlinova(tabla, boja) - tabla._roditelj.broj_mlinova(tabla, boja)

def broj_mlinova(tabla, boja):          #vraca broj nasih mlinova minus broj mlinova suparnika
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
            if tabla._izgled[i][j] == tabla._izgled[i][k] == tabla._izgled[i][l] == boja:
                broj_mlinova += 1
            elif tabla._izgled[i][j] == tabla._izgled[i][k] == tabla._izgled[i][l] == boja2:
                broj_mlinova -= 1
    for j in range(1, 8, 2):
        if tabla._izgled[0][j] == tabla._izgled[1][j] == tabla._izgled[2][j] == boja:
            broj_mlinova +=1
        elif tabla._izgled[0][j] == tabla._izgled[1][j] == tabla._izgled[2][j] == boja2:
            broj_mlinova -= 1
    return broj_mlinova

def broj_blokiranih_figura(tabla, boja):           #vraca broj blokiranih figura minus od suparnika
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
            if tabla._izgled[i][j] == boja2: #ako je protivnikova figurica tamo
                if tabla._izgled[i][prethodno]==boja and tabla._izgled[i][sledece]==boja:
                    if j in [0, 2, 4, 6]:
                        broj_blokiranih_figura -= 1
                    elif i  == 1 and tabla._izgled[0][j] == tabla._izgled[2][j] == boja:
                        broj_blokiranih_figura -= 1
                    elif tabla._izgled[1][j] == boja:
                        broj_blokiranih_figura -= 1
            elif tabla._izgled[i][j] == boja:   #ako je nasa figura tamo
                if tabla._izgled[i][prethodno]==boja2 and tabla._izgled[i][sledece]==boja2:
                    if j in [0, 2, 4, 6]:
                        broj_blokiranih_figura += 1
                    elif i  == 1 and tabla._izgled[0][j] == tabla._izgled[2][j] == boja2:
                        broj_blokiranih_figura += 1
                    elif tabla._izgled[1][j] == boja2:
                        broj_blokiranih_figura += 1
    return broj_blokiranih_figura

def broj_piona(tabla, boja):            #vraca broj piona minus broj piona suparnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    pioni = 0
    for i in range(3):
        for j in range(8):
            if tabla._izgled[i][j] == boja:
                pioni += 1
            elif tabla._izgled[i][j] == boja2:
                pioni -= 1
    return pioni

def broj_dvojki(tabla, boja):           #vraca broj dvojki koje postoje na tabli za jednu boju
    pozicija=0
    broj_dvojki = 0
    for i in range(len(tabla._izgled)):
        for j in range(1, len(tabla._izgled[i]), 2):
            pozicija+=2
            sledece = j + 1
            prethodno = j - 1
            if j == 7:
                sledece = 0
            if tabla._izgled[i][j] == boja:
                if tabla._izgled[i][prethodno] == "x" and tabla._izgled[i][sledece] == boja:
                    broj_dvojki += 1
                elif tabla._izgled[i][prethodno] == boja and tabla._izgled[i][sledece] == "x":
                    broj_dvojki += 1
                if i in [0, 2]:
                    if tabla._izgled[1][j] == "x" and tabla._izgled[abs(i - 2)][j] == boja:
                        broj_dvojki += 1
                    elif tabla._izgled[1][j] == boja and tabla._izgled[abs(i - 2)][j] == "x":
                        broj_dvojki += 1
                elif i==1:
                    if tabla._izgled[0][j] == "x" and tabla._izgled[2][j] == boja:
                        broj_dvojki += 1
                    elif tabla._izgled[0][j] == boja and tabla._izgled[2][j] == "x":
                        broj_dvojki += 1
            elif tabla._izgled[i][j] == "x":
                if tabla._izgled[i][prethodno] == boja and tabla._izgled[i][sledece] == boja:
                    broj_dvojki += 1
                if i in [0, 2]:
                    if tabla._izgled[1][j] == boja and tabla._izgled[abs(i - 2)][j] == boja:
                        broj_dvojki += 1
                elif i==1:
                    if tabla._izgled[0][j] == boja and tabla._izgled[2][j] == boja:
                        broj_dvojki += 1
    return broj_dvojki

def broj_trojki(tabla, boja):           #vraca broj trojki koje postoje na tabli za jednu boju, važi za prvu fazu
    dva = broj_dvojki(tabla, boja)
    return ( dva * (dva - 1) ) / 2

def nova_prilika_za_mlin(tabla, boja):       #funkcija vraca broj novih prilika za mlin minus za protivnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    k = tabla.broj_dvojki(tabla, boja) - tabla._roditelj.broj_dvojki(tabla, boja)
    l = tabla.broj_dvojki(tabla, boja2) - tabla._roditelj.broj_dvojki(tabla, boja2)
    return k - l
    
def dupli_mlin(tabla, boja):        #vraca razliku nasih i protivnikovih mlinova
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
            if tabla[i][j] == "x":
                if tabla[i][prethodno]==tabla[i][prethodno2]==tabla[i][sledece]==tabla[i][sledece2]==boja:
                    broj_duplih += 1
                elif tabla[i][prethodno]==tabla[i][prethodno2]==tabla[i][sledece]==tabla[i][sledece2]==boja2:
                    broj_duplih -= 1
    for j in range(1, 8, 2):
        if j==7:
            sledece=0
        else:
            sledece = j + 1
        if tabla[1][j]=="x" and tabla[0][j]==tabla[2][j]==tabla[1][sledece]==tabla[1][j-1]==boja:
            broj_duplih += 1
        elif tabla[1][j]=="x" and tabla[0][j]==tabla[2][j]==tabla[1][sledece]==tabla[1][j-1]==boja2:
            broj_duplih -= 1
        elif tabla[0][j] == "x" and tabla[0][j-1]==tabla[0][sledece]==tabla[1][j]==tabla[2][j]==boja:
            broj_duplih += 1
        elif tabla[0][j] == "x" and tabla[0][j-1]==tabla[0][sledece]==tabla[1][j]==tabla[2][j]==boja2:
            broj_duplih -= 1
        elif tabla[2][j] == "x" and tabla[2][j-1]==tabla[2][sledece]==tabla[1][j]==tabla[0][j]==boja:
            broj_duplih += 1
        elif tabla[2][j] == "x" and tabla[2][j-1]==tabla[2][sledece]==tabla[1][j]==tabla[0][j]==boja2:
            broj_duplih -= 1
    return broj_duplih

def pobednicka_konfiguracija(tabla, boja):      #vraca 1000 za pobednicku konfig, a nula ako nije, -1000 ako je gubitak
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    if len(tabla.validni_potezi_faza2(boja2, "broj")) == 0 or broj_piona(tabla, boja2) == 2:
        return 1000
    elif len(tabla.validni_potezi_faza2(boja, "broj")) == 0 or broj_piona(tabla, boja) == 2:
        return -1000
    else:
        return 0
