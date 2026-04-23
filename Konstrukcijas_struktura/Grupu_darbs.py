def pasuti_tkreklus(skaits, apdruka, piegade):  #definē cenas

    cenas = {
        "TEKSTS": 5,
        "ZIME": 7,
        "FOTO": 20
    }

    summa = skaits * cenas[apdruka] #Apreķina vertību

#Parbauda vai ir atlaide
    if summa > 100:
        summa = summa * 0.95

    if piegade:
        if summa < 50:
            summa = summa + 15

    return summa

piegade = True   # klients izvēlējās piegādi
piegade = False  # klients neizvēlējās piegādi




#Parbaude
print(pasuti_tkreklus(6, "FOTO", True))