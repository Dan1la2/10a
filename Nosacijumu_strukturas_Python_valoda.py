#01.02.2026

#Majas darbs nosacījumu strukturas Python valoda

#zveido Python programmu, kas:

#Pieprasa lietotājam ievadīt:
#vārdu 1
#vecumu 2
#iecienītāko programmēšanas valodu 3

vards = input("Ievadi savu vardu:") #1
vecums = int(input("Ievadi savu vēcumu:")) #2
Izvele_programesanas_valoda = input("Ievadi iecienītāko programmēšanas valodu:") #3


#Programma:

#pārbauda, vai lietotājs ir pilngadīgs
#pārbauda, vai ievadītā programmēšanas valoda ir sarakstā
#izvada atbilstošu ziņojumu




programmesanas_valodas = ["Python", "Java", "C++", "JavaScript"]



#vēcuma parbaudīšāna

if vecums >= 18: #matematiski salidzīnas
    print("Tu esi pilngadīgs.") #izpildas, ja nosacijums ir pareiz
else:
    print("Tu vēl neesi pilngadīgs.")#izpildas, ja nosacijums ir nepareiz


#Valodas parbaudīšana ir saraksta vai ne

if Izvele_programesanas_valoda in programmesanas_valodas:
    print("ir viena no populārajām programmēšanas valodām")
else:
    print("nav viena no populārajām programmēšanas valodām.")


