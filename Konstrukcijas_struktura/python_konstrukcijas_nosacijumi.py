#29.01.2026

#nosacijumi - if, elif, else

#Piemērs ar skaitli
vecums = int(input("Ievadi savu vecumu: "))

if vecums >= 18: #matematiski salidzīnas
    print("Tu esi pilngadīgs.") #izpildas, ja nosacijums ir pareiz
else:
    print("Tu vēl neesi pilngadīgs.")#izpildas, ja nosacijums ir nepareiz

#Piemērs ar tekstu
    vards = input("Ievadi savu vārdu: ") 

if vards == "Anna": #Simbola salīdzināšana izmantojam ==
    print("Sveika, Anna!")
else:
    print("Sveiki, lietotāj!")

    # if – elif – else struktūra

    atzime = int(input("Ievadi atzīmi (1–10): "))

if atzime >= 9:
    print("Izcili!")
elif atzime >= 6:
    print("Ieskaite")
else:
    print("Nepietiekami")

    #Piemērs ar sarakstu

    augli = ["ābols", "banāns", "bumbieris"]

izvele = input("Ievadi augļa nosaukumu: ")

if izvele in augli:
    print("Šis auglis ir sarakstā.")
else:
    print("Šī augļa sarakstā nav.")

    #1 variants ar in

if izvele in augli:
    print("Šis auglis ir sarakstā.")
else:
    print("Šī augļa sarakstā nav.")


    #2. variants ar salidzināšanu

izvele == augli[0]
 



lietotajvards = input("Ievadi lietotājvārdu: ")
parole = input("Ievadi paroli: ")

    #1. variants
if lietotajvards == "admins" and parole == "1234":
    print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")

    #2. variants
if lietotajvards == "admins":
  if parole == "1234":
        print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")

