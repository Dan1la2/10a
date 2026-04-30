#30.04.2026

#CSV datnes nolasišana un datu apstrāde - uzdevums

#📝 Uzdevums 1
#Izveido programmu, kas izvada tikai skolēnus no Jelgavas.

#📝 Uzdevums 2
#Izvada tikai tos skolēnus, kuri jaunāki par 17 gadiem.

#📝 Uzdevums 3 (Cietā rieksta līmenis)
#Saskaiti, cik ierakstu ir datnē.

#⭐ PAPILDUS UZDEVUMS
#Aprēķini vidējo vecumu.


#Pēc uzdevuma izpildes, nosūti to uz github!


with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        if pilseta == "Jelgava": #Pārbaude, vai pilsēta ir Rīga
            print(vards,vecums,pilseta) #Izvada personas vārdu, kas dzīvo Rīgā




with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums,pilseta = rinda.strip().split(",")
        if int(vecums) < 17:
           print(vards,vecums,pilseta)



RinduSkaits = 0


with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        RinduSkaits += 1
    print(RinduSkaits)



with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums,pilseta = rinda.strip().split(",")
        if int(vecums) < 17:
           print(vards,vecums,pilseta)