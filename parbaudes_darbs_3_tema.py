#21.05.2026
#parbaudes darbs

#2 Datu validācija

#2.1

Vards = input("Ievadi vardu: ") #prasa lietotājam ievadīt vārdu
print(Vards)


#vai sākas ar lielo burtu
if Vards[0].isupper():
        print("Ir ar lielo burtu")
else:
        print("Nav ar lielo burtu")



#3 Datu apstrāde

#3.1

with open("dati_ieskaite.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums = rinda.strip().split(",")
        if int(vecums) >= 18:
           print(vards,vecums)


#3.2


summa = 0
skaits = 0

with open("dati_ieskaite.csv", encoding="utf-8") as fails:
    next(fails)

    for line in fails:
        vards, vecums = line.strip().split(",")

        summa += int(vecums)
        skaits += 1

print(summa/skaits)


#4 Kārtošana

names = ["Laura", "Anna", "Marta", "Jānis"]

#4.1

names.sort(reverse=False)
print(names)

#4.2
#Jo vieglāk orientēties datos. Kad viņus ir daudz piemēram uzvardus saraksta un tev viņi ir sakartoti alfabēta secība tu ievādi pirmo burtu uzvarda un tev izdot uzvardos uz to burtu un tas pavieglina meklēšanu.

skaitli = ["5", "44", "67", "3"]

skaitli.sort(reverse=False)

print("mazakais skaitlis:", skaitli[0])



#5 Meklēšana

#5.1


vardi = ["Anna", "Laura", "Marta"]



if "Laura" in vardi:
    print("Laura ir sarakstā")
else:
    print("Laura nav sarakstā")



#5.2
#Lai atrāk apstradāt un izvadīt datus

#5.3

with open("dati_ieskaite.csv", encoding="utf-8") as fails:
    next(fails)

    for rinda in fails:
        vards, vecums = rinda.strip().split(",")

        if int(vecums) == 20:
            print("Atrasts:", vards, vecums)

