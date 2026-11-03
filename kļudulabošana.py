#a = 6
#b = 4
#perimetrs = a * b
#print(perimetrs)

#skaitlis = 7
#if skaitlis < 0:
#    print("Pozitīvs")
#else:
#    print("Negatīvs")


#print("Rezultāts:", 5 + 5)

#skaitlis = 0
#rezultats = 20 / skaitlis

#skaits = "10"
#rezultats = skaits + 5
#print(rezultats)

#print("Labdien!"

#vards = "Anna"
#print(vards)

#skaitlis = 8
#if skaitlis > 0:
 #   print("Pozitīvs")

#print("Rezultāts:", 5 + 5)

#

#a = 10
#b = 5
#print(a / b)

#vards = "Anna"
#print(vārds)

#skaits = "10"
#print(int(skaits) + 5)

#vecums = int("18")
#print(vecums)


#a = int(input("Skaitlis: "))
#print(100 / a)

#skaits = "10"
#print(int(skaits) + 5)

#vecums = input("Ievadi vecumu: ")
#print(int(vecums) + 1)

#cena = input("Ievadi cenu: ")
#print(float(cena) * 1.21)

#skaits = "10"
#print(int(skaits) + 5)

#skaitlis = int("10")
#print(skaitlis)

#a = int(input("Ievadi a: "))
#b = int(input("Ievadi b: "))
#print(a / b)

#vecums = input("Ievadi vecumu: ")
#print(vecums + 1)

#cena = input("Cena: ")
#daudzums = 3
#summa = float(cena) * daudzums
#print("Summa:", summa)

def parbaudit_pieteikumus(skaits):
    if skaits == 0:
        return "Nav dalībnieku"

    elif skaits <= 30:
        return "Pieteikšanās pieņemta"
    else:
        return "Vietu nav"

ievade = input("Dalībnieku skaits: ")
skaits = int(ievade)
print(parbaudit_pieteikumus(skaits))

