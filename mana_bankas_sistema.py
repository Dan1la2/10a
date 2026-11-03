#03.11.2026 
#Izveido Python programmu, kas, izmantojot objektorientēto programmēšanu, modelē bankas kontu kā objektu! Uzdevuma mērķis ir nostiprināt prasmes klases izveidē, konstruktora __init__ un self lietošanā, metožu izstrādē, kuras maina objekta stāvokli, kā arī vienkāršas loģikas izmantošanā, lai novērstu nekorektu darbību. Papildus tiek apgūta ideja par datu sagatavošanu saglabāšanai, pārvēršot objekta datus teksta rindā.
#Tev jāizveido programma, kurā bankas konts tiek aprakstīts ar klasi BankasKonts. Programma demonstrē konta darbību: naudas iemaksu, naudas izņemšanu, informācijas attēlošanu un datu sagatavošanu saglabāšanai. Uzdevumā drīkst izmantot if pārbaudi metodē iznemt, bet nav nepieciešami cikli vai sarežģītas datu struktūras – fokuss ir uz OOP pamatiem un stāvokļa maiņu ar metodēm.



class BankasKonts: 
    def __init__ (self, ipasnieks, numurs): 
        self.ipasnieks = ipasnieks
        self.numurs = numurs
        self.atlikums = 0.0

    def iemaksat(self, summa):
        self.atlikums += summa

    def iznemt(self, summa):
        if summa > self.atlikums:
            print("Nepietiek līdzekļu kontā!")
        else:
            self.atlikums -= summa

    def paradit_info(self):
        print("Konts ipasnieks", self.ipasnieks)
        print("Konts numurs" ,self.numurs)
        print("Konts atlikums", self.atlikums)

    def uz_failu(self):
        return self.ipasnieks, self.atlikums, self.numurs
        


Konts1 = BankasKonts("Annija", "LV123BANK777")
print("Konts1 ipašnieks: ", Konts1.ipasnieks)
print("Konts1 numurs:", Konts1.numurs)
print("Konts1 atlikums:", Konts1.atlikums)

Konts1.iemaksat(300)
print("Pec iemaksās Konts1 atlikums:", Konts1.atlikums)
    
Konts1.iznemt(300)
print("Pec izņēmšanas Konts1 atlikums:", Konts1.atlikums)

Konts1.iznemt(300)
print("Pec izņēmšanas Konts1 atlikums:", Konts1.atlikums)
    
print(Konts1.uz_failu())