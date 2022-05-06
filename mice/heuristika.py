def heuristika(tabla, faza, boja):
    if faza == 1:
        pass
    elif faza == 2:
        pass
    else:
        pass
        #da li ovo uopšte treba da postoji???

def novi_mlin(tabla, boja):
    pass
    #k = tabla.broj_mlinova() - tabla._roditelj.broj_mlinova()
    # if k >= 1:
    #   novi_mlin += k
    #mozda da se svostruko ili trostruko poena dobije za 2 milina odjednom

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

def broj_dvojki(tabla, boja):
    pass

def broj_trojki(tabla, boja):
    pass

def nova_prilika_za_mlin(tabla, boja):
    pass
    #k = tabla.broj_dvojki() - tabla._roditelj.broj_dvojki()
    # if k >=1:
    #   broj_prilika += k 
    
def dupli_mlin(tabla, boja):
    pass
    #dva mlina paralelno ili cosak mada to je losije

def pobednicka_konfiguracija(tabla, boja):
    pass
    #if broj_mogucih_poteza(tabla, boja2) == 0 or broj_piona(tabla, boja2) == 2:
    #   return 1000
    #else:
    #   return 0


