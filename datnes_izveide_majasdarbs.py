# datnes_izveide_majasdarbs.py

produkti = []


produkti.append(input("Ievadi 1. produktu: "))
produkti.append(input("Ievadi 2. produktu: "))
produkti.append(input("Ievadi 3. produktu: "))


# Saglabā failā produkti.txt
with open("produkti.txt", "w", encoding="utf-8") as f:
    for produkts in produkti:
        f.write(produkts + "\n")

print("Produkti saglabāti failā produkti.txt")