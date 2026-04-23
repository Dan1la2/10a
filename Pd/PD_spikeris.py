#3. uzdevums (3 p.)
#Pareizā secība:

#Plānošana

#Analīze

#Izstrāde

#Testēšana

#Uzturēšana

#Plānošana – nosaka projekta mērķus un prasības.
#Testēšana – pārbauda, vai programma darbojas pareizi.


#7. uzdevums (4 punkti)
#Specifikācija:

#Izveido programmu, kas:

#izveido mainīgo vecums

#izvada tekstu:
#"Tev ir X gadi"

#Ievēro:

#korektu sintaksi

#koda stilu

#vismaz vienu komentāru

# Saglabā lietotāja vecumu
vecums = 16
# Izvada informāciju
print("Tev ir",vecums,"gadi")


#Specifikācija:

#Izveido funkciju kvadrats(skaitlis),
#kas atgriež skaitļa kvadrātu.

#Papildus:

#funkciju izsauc

#izdrukā rezultātu

def kvadrats(skaitlis):
  return skaitlis * skaitlis
rezultats = kvadrats(5)
print(rezultats)


#Specifikācija:

#Izveido programmu, kas:

#pieprasa lietotājam ievadīt atzīmi (0–100)

#ja atzīme ≥ 90 → izvada "Izcili"

#ja atzīme ≥ 70 → izvada "Labi"

#citādi → izvada "Jāuzlabo"

#Programmai jābūt:

#ar komentāriem

#bez sintakses kļūdām

#ar pareizu zarošanos


# Ievada atzīmi
atzime = int(input("Ievadi atzīmi (0-100): "))
# Pārbauda vērtējumu
if atzime >= 90:
  print("Izcili")
elif atzime >= 70:
  print("Labi")
else:
  print("Jāuzlabo")



#Izmanto ciklu while, lai:
#palielinātu skaitli number, līdz tas kļūst lielāks par 50
#number = 5
 

number2 = 5
while number2 <= 50:
    number2 += 1





a = 5

b = 3.2

#Aprēķini šo skaitļu summu.
#Izvadi rezultātu divos veidos

darbiba = a+b

print(darbiba)
print(a + b)

print("Skaitļu summa ir:", darbiba)



teksts1 = "Rīga"

teksts2 = "44"

#teksta garumu

print(len (teksts1))
print(len (teksts2))

#pirmo simbolu
print(teksts1 [0])
print(teksts2 [0])

#tekstu apgrieztā secībā

print(teksts1[::-1])
print(teksts2[::-1])

#zveido sarakstu (list) ar vismaz 5 elementiem

speles = ["minecraft", "CS2", "Dota2", "GTA5", "Resident evil"]

#Izvadi:
#visu sarakstu
print(speles)

#pirmo elementu
print(speles[0])

#pedejo elementu
print(speles[4])

#Pievieno sarakstam vienu jaunu elementu.

speles.append("Fortnite")

#Nomaini vienu esošu elementu sarakstā.

speles[0] = "Rust"

#Izvadi saraksta elementu skaitu.

print(speles)

informacija = {"vards" : "Danila", "vecums" : 16 , "pilseta" : "Viļani"}

#Izvadi katru vērtību atsevišķi, izmantojot atslēgas.

print(informacija["vards"])
print(informacija["vecums"])
print(informacija["pilseta"])

#Pievieno vārdnīcai jaunu atslēgu

informacija["reitings CS2"] = "13444"

#Izmanto un izvada:    .keys() | .values()

print(informacija.keys())

print(informacija.values())

#Izaicinājums: Datu tipu apvienošana

#Izveido sarakstu (list)

kaut_kas = [1990, "Mauzer", {"adrese" : "Maja_Pushkina_iela_kalatuškina"}] 

#Izvadi visu sarakstu

print(kaut_kas)

#izvadi katru elementu atsevišķi

print(kaut_kas[0])
print(kaut_kas[1])
print(kaut_kas[2])

#No vārdnīcas, kas atrodas sarakstā:
#izvada vienu vērtību, izmantojot atslēgu

print(kaut_kas[2]["adrese"])

#Pievieno vārdnīcai jaunu atslēgu–vērtību pāri.

kaut_kas[2]["Diena"] = "22"

print(kaut_kas)

#Izmantojot tekstu no saraksta:
#nosaki teksta garumu
#izvada tekstu ar lielajiem burtiem
#izvada tekstu apgrieztā secībā

teksts = kaut_kas[1]

print(len(teksts)) #1
print(teksts.upper()) #2
print(teksts[::-1])


#4. uzdevums – vārdnīca (dictionary)
#Dots vārdnīcas objekts:

#student = {
#"vārds": "Jānis",
#"vecums": 17,
#"kurss": "Programmēšana I"
#}
 
 #Izmanto ciklu for, lai:

#izvadītu katru atslēgu un tās vērtību šādā formātā:

#vārds : Jānis
#vecums : 17
#kurss : Programmēšana I

student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}

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
