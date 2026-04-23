#08.02.2026

#1. uzdevums – skaitītājs (number)
#Izmanto ciklu while, lai:
#izvadītu skaitļus no 1 līdz 10
#📌 Padoms: izmanto skaitītāja mainīgo.

skaitlis = 1
while skaitlis < 11:
    print(skaitlis)
    skaitlis += 1


#2. uzdevums – pāra skaitļi
#Izmanto ciklu while, lai:
#izvadītu tikai pāra skaitļus no 1 līdz 20
#📌 Padoms: izmanto if nosacījumu.

i = 1

while i <= 20:
    if i % 2 == 0:
        print(i, "ir pāra skaitlis")
    i += 1


#3. uzdevums – teksts (string)


#Dots teksts: 
#text = "Python" 
#Izmanto ciklu while, lai:
#izvadītu katru burtu atsevišķā rindā
#📌 Padoms: izmanto indeksu (i).

text = "Python"
for letter in text:
    print(letter)


#4. uzdevums – saraksts (list)



#Dots saraksts:
#numbers = [3, 6, 1, 8, 4]
#Izmanto ciklu while, lai:
#izvadītu visus saraksta elementus
#saskaitītu un izvadītu visu skaitļu summu


numbers = [3, 6, 1, 8, 4]

i = 0
summa = 0


while i < len(numbers):
    print(numbers[i])
    summa += numbers[i]
    i += 1
print("Summa:", summa)


#5. uzdevums – nosacījums (⭐)


#Izmanto ciklu while, lai:
#palielinātu skaitli number, līdz tas kļūst lielāks par 50
#number = 5
 

number2 = 5
while number2 <= 50:
    number2 += 1