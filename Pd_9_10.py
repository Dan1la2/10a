
#9 uzd

def laukums(platums, garums): #definēju funkciju
    return platums * garums #aprēķina laukumu
print(laukums(2,7)) #Izvada rezultatu


#10 Uzd

skaitlis1 =float(input("Ludzu ievadi skaitli: ")) #pieprasa lietotājam ievadit pirmo skaitli
skaitlis2 =float(input("Ludzu ievadi skaitli: ")) #pieprasa lietotājam ievadit otro skaitli
print("Tavs skaitlis ir: ", skaitlis1 + skaitlis2)

summa = skaitlis1 + skaitlis2 

if summa <= 100: #matematiski salidzīnas
    print("Mazs rezultatas.") #Ja summa ir vienāda vai mazāka par 100 
else:
    print("Liels rezultāts.") #Ja summa ir lielaka