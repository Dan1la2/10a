#27.01.2026
#majas darbs datu tipi

#Definē divus skaitļu mainīgos:





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


#PAPILDUS UZDEVUMS MAN IR IZPILDĪTS KOPA AR MAJĀSDARBU