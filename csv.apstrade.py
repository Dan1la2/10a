#27.04.2026

#CSV datnes atveršana, nolasīšana un datu apstrāde

with open("students.csv", encoding="utf-8" ) as fails: #ar funkciju open tiek atverts CSV fails
    print(fails) #Izvada faila informaciju (ne saturu)
    #for rinda in fails:
        #print(rinda) #izvada informaciju, iekļaujot tab
    for rinda in fails:
        print(rinda.strip()) #izvada informaciju, noņemot atstarpes



print("Datu sadališanas kolonas")
#izlaižam kolona nosaukumu
with open("students.csv", encoding="utf-8" ) as fails: #ar funkciju open tiek atverts CSV fails
    next(fails) #funkcija next() izlaiž vienu rindu faila
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabajam datus mainigos, sadalot pēc atdalitāja
        print(vards,uzvards,pilseta) #izvada informaciju


#Tikai vārdu izvadīšana
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        print(vards) #Izvada tikai vārdu




#Datu apstrādāšana - izvada tikai personas, kas dzīvo Jelgava
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        if pilseta == "Rīga": #Pārbaude, vai pilsēta ir Jelgava
            print(vards) #Izvada personas vārdu, kas dzīvo Jelgava