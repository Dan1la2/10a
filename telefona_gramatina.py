class Kontakts: #Objekta nosaukumu vienmēr sāksim ar lielu burtu
    def __init__ (self, vards, uzvards, talrunis): #Īpašību definēšana
        self.vards = vards
        self.uzvards = uzvards
        self.talrunis = talrunis   

    def mainit_talrunis(self, jauns_talrunis):
        self.talrunis = jauns_talrunis

    def paradit_info(self):
        print("Vārds :", self.vards)
        print("Uzvārds:", self.uzvards)
        print("Telefona numurs:", self.talrunis)

#Pirmā objekta talruņa izveide
kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456")
print(kontakts1.vards)
print(kontakts1.uzvards)
print(kontakts1.talrunis)

#Otrā objekta talruņa izveide
kontakts2 = Kontakts("Anna", "Kalniņa", "29876543")
print(kontakts2.vards)
print(kontakts2.uzvards)
print(kontakts2.talrunis)

#numura maiņa
kontakts1.mainit_talrunis("26999999")
print("Pec mainīšanas pirmam kontaktam izmainījas:",kontakts1.talrunis)

#Parāda informāciju par abiem kontaktiem
kontakts1.paradit_info()
kontakts2.paradit_info()