#04.02.2026


#Treniņa uzdevums: Python cikls for

#1. uzdevums – skaitļi
#Izmanto ciklu for, lai:
#izvadītu visus skaitļus no 1 līdz 10
#izvadītu tikai pāra skaitļus

#1.1
for i in range(1,11):
    print(i)

#1.2
for i in range(1, 11):
    if i % 2 == 0:  #% - dalijums bez atlikuma
        print(i, "ir pāra skaitlis")


#2. uzdevums – teksts (string)
#Izmanto ciklu for, lai:
#izvadītu katru burtu jaunā rindā
#saskaitītu, cik burtu ir tekstā


text = "Programmēšana"

for letter in text:
    print(letter)

print(len(text)) #vai šito vajadzēja darīt tā?


#3. uzdevums – saraksts (list)
#Dots saraksts:
##numbers = [4, 7, 2, 9, 12]
#Izmanto ciklu for, lai:
#izvadītu katru skaitli
#izvadītu tikai tos skaitļus, kas ir lielāki par 5


numbers = [4, 7, 2, 9, 12]

#3.1
print("Skaitļi:")
for n in numbers:
    print(n)



#3.2
for n in numbers:
  if n > 5:
    print(n)




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

print(student.items())

for key, value in student.items():
    print(key, ":", value)


#5. uzdevums – papildus (⭐)
#Izmanto ciklu for, lai:

#saskaitītu visu saraksta numbers skaitļu summu
#izvadītu rezultātu

summa = 0

for n in numbers:
    summa += n
print("Saraksta skaitļu summa:", summa) #Šito atradu kā izpildīt pieprasot maklīgo intelektu jo mans variānts ar (n + n) izvada man skaitļus kuri tika sapluseti pati ar sevi

 



