#26/01/2026

#datu ievade

#input()

#Ļoti SVARĪĢI: funkcija input() vienmēr atgriež tekstu
#vards = input("Ievadi sāvu vārdu")

#print(vards)

#skaitlis ievade

skaitlis =float(input("Ludzu ievadi savu miļaku skaitli: "))
print("Tavs miļākais skaitlis +5 ir: ", skaitlis+5)

#datu ievade un saglabašana saraksta

prieksmeti = []
prieksmeti.append(input("Ievadi 1. priekšmetu: ")) #ar metodi .append(), pievienojām vertību
prieksmeti.append(input("Ievadi 2. priekšmetu: "))

print("Tavi priekšmeti:", prieksmeti)

#Datu ievade un saglabašana vārdnica

skolens = {} #vārdnīca izvade
skolens["vards"] = input("Ievadi vārdu: ")
skolens["vecums"] = int(input("Ievadi vecumu: "))

print("Skolēna dati:", skolens)