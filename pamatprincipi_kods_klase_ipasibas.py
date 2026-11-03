#27/10/2026

#OOP pamatprincipi

#Objekts
#Objekta īpašības
#Klase, kas ir objekta veidne (template)

#Objekts - Automasina
#Īpašības: marka,modelis, krāsa un ātrums

class Automasina: #Objekta nosaukumu vienmēr sāksim ar lielu burtu
    def __init__ (self, marka, modelis, krasa): #Īpašību definēšana
        self.marka = marka
        self.modelis = modelis
        self.krasa = krasa
        #Īpašība ar noklusējuma vērtību
        self.atrums = 0


#metode
    def paatrinaties(self):
        self.atrums += 10
    def paradit_info(self):
        print("Marka :", self.marka)
        print("Modelis:", self.modelis)
        print("Krāsa:", self.krasa)
        print("Ātrums:", self.atrums)
    


#Pirmā objekta automašīna izveide
mansAuto = Automasina("Audi","A6","pelēka")
print(mansAuto.marka)
print(mansAuto.modelis)
print(mansAuto.krasa)
print(mansAuto.atrums)

mansAuto.atrums = 50
print(mansAuto.atrums)

#Otrā objekta automašīna izveide
tavsAuto = Automasina("Ford", "Ranger","melna")
print(tavsAuto.marka)
print(tavsAuto.modelis)
print(tavsAuto.krasa)
print(tavsAuto.atrums)

tavsAuto.atrums = 110
print("Tavs Auto ātrums",tavsAuto.atrums)
print("Mans Auto ātrums",mansAuto.atrums)


mansAuto.paatrinaties()
tavsAuto.paatrinaties()
print("Tavs Auto ātrums pec paātrināšanas",tavsAuto.atrums)
print("Mans Auto ātrums pec paātrināšanas",mansAuto.atrums)


mansAuto.paradit_info()
tavsAuto.paradit_info()