#26.04.2026
#PRAKTISKAIS DARBS - datu validācija

#Varda ievade

Vards = input("Ievadi vardu: ") #prasa lietotājam ievadīt vārdu
print(Vards)

#Pārbaudīt vai ievade nav tukša
if len(Vards) > 0: #vai ievade nav tukša
    print("OK")


#vai sākas ar lielo burtu

    if Vards[0].isupper():
        print("OK")
    else:
        print("Nepareizi")
else:
    print("Nepareizi")