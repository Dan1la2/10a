#02.02.2026

#cikls - for

#for – ja ir zināms, cik reižu vai pa kādiem elementiem jāatkārto darbība

#📌 for ar skaitļiem (number)

for i in range(5):
    print(i) #range() - ļauj apstradāt diapozonu


#📌 for ar tekstu (string)

text = "Python"

for letter in text:
    print(letter)


#📌 for ar sarakstu (list)

numbers = [3, 7, 2, 9]

for n in numbers:
    print(n * 2)


#📌 for ar vārdnīcu (dictionary)

student = {
    "vārds": "Anna",
    "vecums": 16,
    "kurss": "Programmēšana"
}

print(student.items())

for key, value in student.items():
    print(key, ":", value)


#📌 for ar nosacījumu

print(2%2)
print(2%9)

for i in range(1, 11):
    if i % 2 == 0:  #% - dalijums bez atlikuma
        print(i, "ir pāra skaitlis")








#02.02.2026

#cikls while
#while ar skaititāju (number)
skaitlis = 0
while skaitlis < 5:
    print(skaitlis)
    skaitlis += 1 #skaitlis = skaitlis + 1 (tas pats)


parole = ""
while parole != "1234":
    parole = input("Ievadi paroli: ")

print("Pareiza parole!")