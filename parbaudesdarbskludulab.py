def rezervacija(skaits):
    if skaits ==0:
        return "Izvēlies vismaz vienu grāmatu"
    if skaits < 0:
        return "Nederīgs skaitlis"

    elif skaits <= 3:
        return "Rezervācija pieņemta"
    else:
        return "Vienā reizē drīkst rezervēt ne vairāk kā 3 grāmatas"

ievade = input("Cik grāmatas vēlies rezervēt? ")
skaits = int(ievade)
print(rezervacija(skaits))
