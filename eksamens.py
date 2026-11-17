class Gramata: #Objekta nosaukumu vienmēr sāksim ar lielu burtu
    def __init__ (self, nosaukums , lappusu_skaits, ISBN, autors, žanrs, izdosanas_gads, pieejamibas_statuss ): #Īpašību definēšana
        self.nosaukums = nosaukums
        self.lappusu_skaits = lappusu_skaits
        self.ISBN = ISBN
        self.autors = autors
        self.žanrs = žanrs
        self.izdosanas_gads = izdosanas_gads
        self.pieejamibas_statuss = pieejamibas_statuss



gramata = Gramata("Epifānijas", "304", "Imants Ziedonis", "dzeja", "2022", "pieejama")
print("gramatas nosaukums: ", gramata.nosaukums)
print("lappušu skaits:", gramata.lappusu_skaits)
print("gramatas ISBN:", gramata.ISBN)



harijs = Fantazija(
    nosaukums: „Harijs Poters un Filozofu akmens”;
    lappušu skaits: 223;
    ISBN: 9780747532699;
    autors: Dž. K. Roulinga;
    žanrs: fantāzija;
    izdošanas gads: 1997;
    pieejamības statuss: pieejama
)

def aprekinat(self,kaveto_dienu_skaits):
    if kaveto_dienu_skaits>=5:
        kavejumaMaksa = super().aprekinat(kaveto_dienu_skaits)
        kavejumaMaksaFantazijasZanrs = kavejumaMaksa * 1.01
        return round(kavejumaMaksaFantazijasZanrs,2)
    return
pass


def pievienot(self,gramata):
    self.gramata.append(gramata)
    print(f'Grāmata "{gramata.nosaukums}" ir veiksmīgi pievienota')


katalogs = GramatuKatalogs()

katalogs.pievienot(epifanijas)
katalogs.pievienot(harijs)

#katalogs.atjauninat.statusu

def atjaunat_statusu(self,ISBN, jauns_statuss):
    for gramata in self.gramatas:
        if gramata.ISBN == ISBN:
            gramata.pieejamibasStatuss = jauns_statuss
            print(f'Grāmatai ar ISBN "gramata.ISBN" statuss ir atjaunināts uz "nav pieejama".')



def nonemt(self,ISBN):
    for gramata in self.gramatas:
        if gramata.ISBN == ISBN:
            self.gramata.remove(gramata)
            print(f'Grāmata ar ISBN "{gramata.ISBN}" nav atrasta katalogā. ')
            return
    print(f'Grāmata ar ISBN "{gramata.ISBN}" nav atrasta katalogā. ')
