#29.01.2026




#Izveido Python programmu, kas:
#Pajautā lietotājam:
#vārdu (string)
#vecumu (number)
#trīs iecienītākās krāsas (list)
#Saglabā datus vārdnīcā (dictionary)
#Izvada visu informāciju vienā print() komandā


lietotajs = {}
lietotajs["vards"] = input("Ievadi vārdu: ")
lietotajs["vecums"] = int(input("Ievadi vecumu: "))

lietotajs["krasa"] = []

lietotajs["krasa"].append(input("Ievadi savu patikamo krāsu 1. : "))
lietotajs["krasa"].append(input("Ievadi savu patikamo krāsu 2. : "))
lietotajs["krasa"].append(input("Ievadi savu patikamo krāsu 3. : "))

print("Lietotāja dati:", lietotajs)