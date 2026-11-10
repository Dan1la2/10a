#03.11.2026 
#Izveido Python programmu, kas, izmantojot objektorientēto programmēšanu, modelē bankas kontu kā objektu! Uzdevuma mērķis ir nostiprināt prasmes klases izveidē, konstruktora __init__ un self lietošanā, metožu izstrādē, kuras maina objekta stāvokli, kā arī vienkāršas loģikas izmantošanā, lai novērstu nekorektu darbību. Papildus tiek apgūta ideja par datu sagatavošanu saglabāšanai, pārvēršot objekta datus teksta rindā.
#Tev jāizveido programma, kurā bankas konts tiek aprakstīts ar klasi BankasKonts. Programma demonstrē konta darbību: naudas iemaksu, naudas izņemšanu, informācijas attēlošanu un datu sagatavošanu saglabāšanai. Uzdevumā drīkst izmantot if pārbaudi metodē iznemt, bet nav nepieciešami cikli vai sarežģītas datu struktūras – fokuss ir uz OOP pamatiem un stāvokļa maiņu ar metodēm.



class BankasKonts: 
    def __init__ (self, ipasnieks, numurs): #konta info
        self.ipasnieks = ipasnieks
        self.numurs = numurs
        self.atlikums = 0.0

    def iemaksat(self, summa): # iemaksā
        self.atlikums += summa

    def iznemt(self, summa):  #izņem
        if summa > self.atlikums:
            print("Nepietiek līdzekļu kontā!")
        else:
            self.atlikums -= summa

    def paradit_info(self): #parāda konta informāciju 
        print("Konts ipasnieks", self.ipasnieks)
        print("Konts numurs" ,self.numurs)
        print("Konts atlikums", self.atlikums)

    def uz_failu(self):  #Jāizveido metode uz_failu()
        return self.ipasnieks, self.atlikums, self.numurs

    def uz_failu(self):
        with open("bankas_kods.csv", "w", encoding="utf-8") as f:
          f.write("ipašnieks,konta numurs,atlikums\n")
          f.write(f"{self.ipasnieks}, {self.numurs}, {self.atlikums}\n")
        


Konts1 = BankasKonts("Annija", "LV123BANK777")
print("Konts1 ipašnieks: ", Konts1.ipasnieks)
print("Konts1 numurs:", Konts1.numurs)
print("Konts1 atlikums:", Konts1.atlikums)

Konts1.iemaksat(300)    # iemaksā 300 EUR
print("Pec iemaksās Konts1 atlikums:", Konts1.atlikums)
    
Konts1.iznemt(300)    #izņem 300 EUR
print("Pec izņēmšanas Konts1 atlikums:", Konts1.atlikums)

Konts1.iznemt(300)    #izņem 300 EUR(izņemt summu, kas pārsniedz atlikumu)
print("Pec izņēmšanas Konts1 atlikums:", Konts1.atlikums)
    
print(Konts1.uz_failu()) #parāda konta informāciju pēc veiktajām darbībām;


Konts1.uz_failu()