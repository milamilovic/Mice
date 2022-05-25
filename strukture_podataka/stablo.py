from red import Queue

class CvorStabla(object):
    def __init__(self, vrednost):
        self._vrednost = vrednost
        self._roditelj = None
        self._deca = []
    def __str__(self):
        return str(self._vrednost)

    @property
    def vrednost(self):
        return self._vrednost
    @vrednost.setter
    def vrednost(self, value):
        self._vrednost = value
    @property
    def roditelj(self):
        return self._roditelj
    @roditelj.setter
    def roditelj(self, value):
        self._roditelj = value
    @property
    def deca(self):
        return self._deca
    @deca.setter
    def deca(self, value):
        self._deca = value

    def _is_root_(self):
        return self._roditelj == None
    def _is_leaf_(self):
        return self._deca == []
    def _dodaj_dete_(self, vrednost):
        vrednost._roditelj = self
        if len(self._deca) == 0:
            self._deca.append(vrednost)
        elif vrednost<self._deca[-1]:
            self._deca.append(vrednost)
        else:
            for i in range(len(self._deca)):                   #sortirana deca, od najveće vrednosti do najmanje
                if self._deca[i]._vrednost <= vrednost._vrednost:
                    self._deca.insert(i, vrednost)
    def _ukloni_dete_(self, vrednost):
        self._deca.remove(vrednost)
    def nadji_roditelja(self):
        return self._roditelj
    def ko_su_deca(self):
        return self._deca
    def broj_dece(self):
        return len(self._deca)



class Stablo(object):
    def __init__(self, koren=None):
        self._root = koren

    def preorder(self, cvor):
        if self._is_empty_ != True:
            print(cvor)
            for dete in cvor.ko_su_deca():
                self.preorder(dete)
    def postorder(self, cvor):
        if self._is_empty_ != True:
            for dete in cvor.ko_su_deca():
                self.postorder(dete)
            print(cvor)
    def breadth_first(self):
        if self._is_empty_ != True:
            red = Queue(100)
            red.enqueue(self._root)
            while red.is_empty != False:
                if red.is_empty() == True:
                    return
                else:
                    novi = red.dequeue()
                    print(novi)
                    for dete in novi._deca:
                        red.enqueue(dete)
    def dodaj_dete(self, cvor, dete):
        cvor._dodaj_dete_(dete)
    def ukloni_dete(self, cvor, dete):
        cvor._ukloni_dete_(dete)
    def len(self):
        return self._root._deca
    def _is_empty_(self):
        return self._root == None
    def cvorovi(self):
        print(self.preorder(self._root))
    def koren(self):
        return self._root
    def zameni(self, cvor, novi):
        novi._roditelj = cvor._roditelj
        novi._deca = cvor._deca
        cvor._roditelj = None
        cvor._deca = []
    def dubina(self, cvor):
        if cvor._is_root_():
            return 0
        else:
            return 1 + self.dubina(cvor.nadji_roditelja())
    def visina(self, cvor=None):
        if cvor==None:
            cvor = self._root
        if cvor._is_leaf_():
            return 0
        else:
            return 1 + max(self.visina(dete) for dete in cvor.ko_su_deca())



if __name__ == "__main__":
    # instanca stabla
    t = Stablo()
    t._root = CvorStabla(0)

    # kreiranje relacija između novih čvorova
    a = CvorStabla(1)
    b = CvorStabla(2)
    c = CvorStabla(3)

    a._dodaj_dete_(b)
    t._root._dodaj_dete_(a)
    t._root._dodaj_dete_(c)

    # visina stabla
    print('Visina = %d' % t.visina())

    # dubina čvora
    print('Dubina(a) = %d' % t.dubina(a))

    # obilazak po dubini - preorder
    print('PREORDER')
    t.preorder(t._root)

    # obilazak po dubini - postorder
    print('POSTORDER')
    t.postorder(t._root)

    # obilazak po širini
    print('BREADTH FIRST')
    t.breadth_first()
