#1. uzdevums — Datu kvalitāte (6 p)
#1.1. Nosaki, kuri dati ir kvalitatīvi. Pamato. (4 p)
#Laura,17,Rīga
#???,-15,Mēness
#Jānis,18
#1.2. Pārveido dotos nestrukturētos datus strukturētā tabulā. (2 p)
#“Marta dzīvo Jelgavā un viņai ir 16 gadi.”

#2. uzdevums — Datu validācija (8 p)
#2.1. Uzraksti programmu, kas pārbauda, vai ievadītais skaitlis ir robežās no 1 līdz 10. (5 p)
#2.2. Paskaidro, kāpēc validācija ir svarīga programmās. (3 p)
#3. uzdevums — Datu apstrāde CSV failā (10 p)
#Dota datne:

 
#produkts,cena
#Piens,1.50
#Maize,2.00
#Sula,3.20
#Cepumi,4.50
 
 
#3.1. Uzraksti programmu, kas izvada tikai produktus, kuru cena ir lielāka par 2.00. (5 p)
#3.2. Aprēķini visu produktu kopējo summu. (5 p)
#4. uzdevums — Kārtošana (8 p)
#4.1. Sakārto sarakstu dilstošā secībā. (3 p)
 
#scores = [7, 10, 5, 8, 9]
 
 
#4.2. Paskaidro, kur dzīvē izmanto datu kārtošanu. Min vienu piemēru. (2 p)
#4.3. Uzraksti programmu, kas izvada 2 lielākos skaitļus sarakstā. (3 p)
#5. uzdevums — Meklēšana (8 p)
#5.1. Uzraksti programmu, kas pārbauda, vai skaitlis 15 atrodas sarakstā. (3 p)
 
#numbers = [5, 12, 15, 20]
 
 
#5.2. Paskaidro, kāpēc meklēšana lielās sistēmās var būt lēnāka. (2 p)
#5.3. Uzraksti programmu, kas CSV failā atrod produktu “Sula”. (3 p)


1.1
#Laura,17,Rīga jo ir visi vajadzīgie dati vards, vecums, pilseta,


1.2

#vards pilseta vecums
#Marta,Jelgava,16

2.1

skaitlis = input("Ievadi skaitli: ")
 
if skaitlis.isdigit():
    skaitlis = int(skaitlis)
 
    if 1 <= skaitlis <= 10:
        print("OK")
    else:
        print("Nav diapazonā")
else:
    print("Kļūda")



2.2

#Lai parbaudītu vai viss ir pareizi izdarīts pec noteikumiem
#Datu validācija — tā ir ievadīto datu pārbaude, lai tie būtu pareizi un atbilstu noteikumiem

3.1 

with open("fails.csv", encoding="utf-8") as f:
    next(f)
 
    for rinda in f:
        produkts, cena = rinda.strip().split(",")
 
        if float(cena) > 2.00:
            print(produkts)


3.2

with open("fails.csv", encoding="utf-8") as f:
    next(f)

    kopā = 0

    for rinda in f:
        produkts, cena = rinda.strip().split(",")
        cena = float(cena)

        if cena > 2.00:
            print(produkts)

        kopā += cena

print("Kopējā summa:", kopā)

4.1

scores = [7, 10, 5, 8, 9]

scores.sort(reverse=True)
print(scores)
                                      #.sort() sakarto augoša secība reverse dara lai to sakartot dilstoša secība
4.2

#Datu kārtošanu izmanto, piemēram, skolā, lai sakārtotu skolēnu atzīmes no lielākās uz mazāko vai lai noteiktu labākos rezultātus konkursā.


4.3

scores = [7, 10, 5, 8, 9]

scores.sort(reverse=True)

print("1. lielākais:", scores[0])
print("2. lielākais:", scores[1])

5.1


numbers = [5, 12, 15, 20]

if 15 in numbers:
    print("15 ir sarakstā")
else:
    print("15 nav sarakstā")


5.2
#Lielās sistēmās meklēšana var būt lēnāka, jo ir ļoti daudz datu, un programmai var nākties pārbaudīt katru ierakstu pa vienam.

5.3

with open("fails.csv", encoding="utf-8") as f:
    next(f)

    for rinda in f:
        produkts, cena = rinda.strip().split(",")

        if produkts == "Sula":
            print("Atrasts:", produkts, cena)








#Skolotajas risinajums 


1. #uzdevums
1.1.
#Laura,17,Rīga → kvalitatīvi
#???,-15,Mēness → nekvalitatīvi
#Jānis,18 → nepilnīgi dati
1.2.
#Vārds	Vecums	Pilsēta
#Marta	16	Jelgava
2. #uzdevums
2.1.
 
skaitlis = input("Ievadi skaitli: ")
 
if skaitlis.isdigit():
    skaitlis = int(skaitlis)
 
    if 1 <= skaitlis <= 10:
        print("OK")
    else:
        print("Nav diapazonā")
else:
    print("Kļūda")
 
 
2.2.
#Validācija palīdz novērst kļūdainus datus un programmas kļūdas.

3. uzdevums
3.1.
 
with open("fails.csv", encoding="utf-8") as f:
    next(f)
 
    for rinda in f:
        produkts, cena = rinda.strip().split(",")
 
        if float(cena) > 2.00:
            print(produkts)
 
 
3.2.
 
summa = 0
 
with open("fails.csv", encoding="utf-8") as f:
    next(f)
 
    for rinda in f:
        produkts, cena = rinda.strip().split(",")
        summa += float(cena)
 
print(summa)
 
 
4. uzdevums
4.1.
 
rezultati = [7, 10, 5, 8, 9]
 
rezultati.sort(reverse=True)
print(rezultati)
 
 
4.2.
#Piemēram, internetveikalos preces kārto pēc cenas.

4.3.
 
rezultati = [7, 10, 5, 8, 9]
 
rezultati.sort(reverse=True)
print(rezultati[:2])
 
 
5. #uzdevums
5.1.
 
skaitli = [5, 12, 15, 20]
 
if 15 in skaitli:
    print("Atrasts")
 
 
5.2.
#Jo sistēmai jāpārbauda ļoti daudz datu, tāpēc meklēšana var aizņemt vairāk laika.

5.3.
 
with open("fails.csv", encoding="utf-8") as f:
    next(f)
 
    for rinda in f:
       produkts, cena = rinda.strip().split(",")
 
       if produkts == "Sula":
           print("Atrasts")









Videjas apreķinašana


#Aprēķina vidējo atzīmi
summa = 0
skaits = 0

with open("klase.csv", encoding="utf-8") as f:
    next(f)

    for line in f:
        vards, atzime = line.strip().split(",")

        summa += int(atzime)
        skaits += 1





Majas darbs ko es nesapratu 


#12/05/2025

#Mājasdarbs

"""
Izveido CSV failu ar:

5 produktiem
cenu
Uzraksti programmu, kas:

aprēķina kopējo summu
izvada dārgāko produktu
Paveikto aizsūti uz GitHub.
"""
#CSV faila izveide ar 5 produktiem un to cenu
with open("datu apstrade un aprekini\produkti.csv","w",encoding="utf-8") as f:
    f.write("Maize,2\n")
    f.write("Piens,1.2\n")
    f.write("Siers,5.6\n")
    f.write("Kūka,12.4\n")
    f.write("Saldējums,0.68\n")
   

#aprēķina kopējo summu
#izvada dārgāko produktu
with open("datu apstrade un aprekini\produkti.csv", encoding="utf-8") as f:

    summa = 0
    lielakaCena = 0
   
    for rinda in f:
        produkts,cena = rinda.strip().split(",")
        summa += float(cena)
        if float(cena) > lielakaCena:
            lielakaCena = float(cena)

print("Kopējā summa:",summa)
print("Lielākā produkta cena:",lielakaCena)