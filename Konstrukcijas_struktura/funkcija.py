#05.02.2026

#Funkcija

#def funkcijas pamatstruktura(parametri):
# dabības
#return rezultāts

#def - atslēgvārds funkcijas izveidēi
#parametri  - dati, ko funkcija saņem
#return - vērtiba, ko funkcija atgriež (nav obligats)

#funkcija kas apreķina divuskaitļu summu
def summa (a, b):
    return a + b
print(summa(1,1))

def summa (a, b):
    rezultats = a + b
    print(rezultats)
summa(1,1)


def summa (a, b):
    rezultats = a + b
summa(1,2)
print(summa(2,4)+5)

def elementu_skaits(saraksts):
    skaits = 0
    for elements in saraksts:
        skaits += 1
    return skaits
print(elementu_skaits([3, 7, 1, 9]))



#Piemērs ar vardnicu (dictionary)

def vai_ir_atslega(dati, atslega):
    if atslega in dati:
        return "Atslega ir atrasta"
    else:
        return "Atslēga nav atrasta"
students = {
    "vards": "Jānis",
    "vecums": 16
}
print(vai_ir_atslega(students, "vecums"))