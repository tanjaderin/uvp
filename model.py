import random, copy, time

NEDOVOLJENA_POTEZA = 'X'
ZMAGA = '+'
PORAZ = '-'

class Pozicija:
    def __init__(self, vrsta, stolp):
        self.vrsta = vrsta
        self.stolp = stolp
        self.odkrita = False
        self.st_bombic_okoli = 0


class Polje:
    def __init__ (self, st_vrstic = 9, st_stolpcev = 9, st_bombic = 10):
        self.nastavitev(st_vrstic, st_stolpcev, st_bombic)

    def nastavitev(self, st_vrstic = 9, st_stolpcev = 9, st_bombic = 10):
        self.st_vrstic = st_vrstic
        self.st_stolpcev = st_stolpcev
        self.st_bombic = st_bombic

        
        polje = []
        for i in range(self.st_vrstic):
            vrstica = []
            for j in range(self.st_stolpcev):
                vrstica.append(Pozicija(i, j))
            polje.append(vrstica)
        
        self.polje = polje

        self.st_polj = st_vrstic * st_stolpcev
        self.st_odkritih = 0

        self.zmaga = False
        self.poraz = False


    def postavitev_bombic (self):
        #nakljucno postavimo bombice oznacimo s crko B
        n = 0
        while n < self.st_bombic:
            i = randint(0, self.st_vrstic)
            j = randint(0, self.st_stolpcev)
            if self.polje[i][j] == 'B':
                n = n - 1
            else:
                self.polje[i][j] = 'B'
            n  = n + 1
            
        

    def oznaci_polja (self):
        #ostevilcimo polja glede na stevilo sosednjih bombic
        for i in range(self.st_vrstic):
            for j in range(self.st_stolpcev):
                if not self.polje[i][j] == 'B':
                    st_sosednjih_bombic = 0
                    for sosed_y in range(-1, 2):
                        for sosed_x in range(-1, 2):
                            if 0 <= i + sosed_y < self.st_vrstic and 0 <= j + sosed_x < self.st_stolpcev:
                                if self.polje[sosed_y + i][sosed_x + j] == 'B':
                                    st_sosednjih_bombic += 1
                    self.polje[i][j].st_bombic_okoli += st_sosednjih_bombic
                    self.polje[i][j] = str(self.polje[i][j].st_bombic_okoli)
        


    def odkrij_prazne(self, vrsta, stolp):
        #odkrijemo prazna polja okoli praznih
        for sosed_x in range(-1, 2):
            for sosed_y in range(-1, 2):
                    if 0 <= vrsta + sosed_y < self.st_vrstic and 0 <= stolp + sosed_x < self.st_stolpcev:
                        if self.polje[vrsta + sosed_y][stolp + sosed_x].odkrita == False:
                            self.polje[vrsta + sosed_y][stolp + sosed_x].odkrita = True
                            self.st_odkritih += 1
                        if self.polje[vrsta + sosed_y][stolp + sosed_x].st_bombic_okoli == 0:
                            self.odkrij_prazne(vrsta + sosed_y, stolp + sosed_x) 



    def odkrivanje(self, vrsta, stolp):
        if self.polje[vrsta][stolp].odkrita == True:
            return NEDOVOLJENA_POTEZA
        
        if self.st_odkritih == 0:
            self.postavitev_bombic()
            self.oznaci_polja()

            if self.polje[vrsta][stolp] == 'B':
                self.polje[vrsta][stolp].odkrita = True
                self.poraz = True
                
            else:
                self.polje[vrsta][stolp].odkrita = True
                self.st_odkritih += 1
                if self.polje[vrsta][stolp].st_bombic_okoli == 0:
                    self.odkrij_prazne(vrsta, stolp)
                if self.st_polj == self.st_odkritih + self.st_bombic:
                    self.zmaga = True
        
        else :
            if self.polje[vrsta][stolp] == 'B':
                self.polje[vrsta][stolp].odkrita = True
                self.poraz = True
                
            else:
                self.polje[vrsta][stolp].odkrita = True
                self.st_odkritih += 1
                if self.polje[vrsta][stolp].st_bombic_okoli == 0:
                    self.odkrij_prazne(vrsta, stolp)
                if self.st_polj == self.st_odkritih + self.st_bombic:
                    self.zmaga = True
                    
                

    def postavi_zastavo(self, vrsta, stolp):
        if self.polje[vrsta][stolp].odkrita == True:
            pass
        else :
            self.polje[vrsta][stolp].odkrita == True
            self.st_odkritih += 1



    def zacetek_igre(st_vrstic, st_stolpcev, st_bombic):
        return Polje()









