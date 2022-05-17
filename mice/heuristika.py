import main

def heuristika(tabla, faza, boja):
    #mozda da postoji ii neka provera taktike
    if faza == 1:
        pass
    else:
        pass

def novi_mlin(tabla, boja):     #vraca brojcanu vrednost koja oznacava razliku nasih i protivickih novih 
    new_mlin = 0                #mlinova je napravljeno u ovom potezu
    k = tabla.broj_mlinova(tabla, boja) - tabla._roditelj.broj_mlinova(tabla, boja)
    if k >= 1:
        new_mlin += k
    new_mlin2 = 0
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    k = tabla.broj_mlinova(tabla, boja2) - tabla._roditelj.broj_mlinova(tabla, boja2)
    if k >= 1:
        new_mlin2 += k
    return new_mlin - new_mlin2

def broj_mlinova(tabla, boja):          #vraca broj nasih mlinova minus broj mlinova suparnika
    broj_mlinova = 0
    for i in range(3):
        for j in range(1, 8, 2):
            k=j-1
            l=j+1
            if j==7:
                l=0
            if tabla._izgled[i][j] == tabla._izgled[i][k] == tabla._izgled[i][l] == boja:
                broj_mlinova += 1
    for j in range(1, 8, 2):
        if tabla._izgled[0][j] == tabla._izgled[1][j] == tabla._izgled[2][j] == boja:
            broj_mlinova +=1
    broj_mlinova_suparnik = 0
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
            if tabla._izgled[i][j] == tabla._izgled[i][k] == tabla._izgled[i][l] == boja2:
                broj_mlinova_suparnik += 1
    for j in range(1, 8, 2):
        if tabla._izgled[0][j] == tabla._izgled[1][j] == tabla._izgled[2][j] == boja2:
            broj_mlinova_suparnik +=1
    return broj_mlinova - broj_mlinova_suparnik

def broj_blokiranih_suparnikovih_figura(tabla, boja):           #vraca broj blokiranih figura minus od suparnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    broj_blokiranih_suparnikovih_figura = 0
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
                        broj_blokiranih_suparnikovih_figura += 1
                    elif i  == 1 and tabla._izgled[0][j] == tabla._izgled[2][j] == boja:
                        broj_blokiranih_suparnikovih_figura += 1
                    elif tabla._izgled[1][j] == boja:
                        broj_blokiranih_suparnikovih_figura += 1
    for i in range(3):
        for j in range(8):
            sledece = j + 1
            prethodno = j - 1
            if j == 0:
                prethodno = 7
            elif j == 7:
                sledece = 0
            if tabla._izgled[i][j] == boja:
                if tabla._izgled[i][prethodno]==boja2 and tabla._izgled[i][sledece]==boja2:
                    if j in [0, 2, 4, 6]:
                        broj_blokiranih_figura += 1
                    elif i  == 1 and tabla._izgled[0][j] == tabla._izgled[2][j] == boja2:
                        broj_blokiranih_figura += 1
                    elif tabla._izgled[1][j] == boja2:
                        broj_blokiranih_figura += 1
    return broj_blokiranih_figura - broj_blokiranih_suparnikovih_figura

def broj_piona(tabla, boja):            #vraca broj piona minus broj piona suparnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    pioni = 0
    pioni_suparnik = 0
    for i in range(3):
        for j in range(8):
            if tabla._izgled[i][j] == boja:
                pioni += 1
            elif tabla._izgled[i][j] == boja2:
                pioni_suparnik += 1
    return pioni - pioni_suparnik

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

def broj_trojki(tabla, boja):           #vraca broj trojki koje postoje na tabli za jednu boju
    #slovo L bez krajeva, dva paralelna, dva nepovezana skroz
    pozicija=0
    broj_trojki = 0
    for i in range(len(tabla._izgled)):
        for j in range(0, len(tabla._izgled[i]), 2):
            if pozicija != 0:    
                pozicija+=2
            sledece = j + 1
            prethodno = j - 1
            #proveravati red po red mozda
            if j == 0:
                prethodno = 7
            if tabla._izgled[i][j] == boja:
                pass
            elif tabla._izgled[i][j] == "x":
                pass
    return broj_trojki

def nova_prilika_za_mlin(tabla, boja):                              #funkcija vraca broj novih prilika za mlin minus za protivnika
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    k = tabla.broj_dvojki(tabla, boja) - tabla._roditelj.broj_dvojki(tabla, boja)
    l = tabla.broj_dvojki(tabla, boja2) - tabla._roditelj.broj_dvojki(tabla, boja2)
    return k - l
    
def dupli_mlin(tabla, boja):
    pass
    #slovo L bez coska, plus bez preseka, T bez preseka sto je plus bez preseka samo drugi sloj

def pobednicka_konfiguracija(tabla, boja):      #vraca 1000 za pobednicku konfig, a nula ako nije
    if boja == "■":
        boja2 = "▢"
    else:
        boja2 = "■"
    if len(tabla.validni_potezi_faza2(boja2)) == 0 or broj_piona(tabla, boja2) == 2:
        return 1000
    else:
        return 0


