def analize_vertejumus(vertejumi):
    # 1️ Aprēķinām vērtējumu skaitu
    skaits = 0
    for v in vertejumi:
        skaits += 1

    # 2️ Aprēķinām kopējo summu, lai iegūtu vidējo
    summa = 0
    for v in vertejumi:
        summa += v

    if skaits > 0:
        videjais = summa / skaits
    else:
        videjais = 0  # ja saraksts tukšs

    # 3️ Nosakām augstāko vērtējumu
    if skaits > 0:
        augstakais = vertejumi[0]
        for v in vertejumi:
            if v > augstakais:
                augstakais = v
    else:
        augstakais = None  # ja saraksts tukšs

    # 4️ Nosakām teksta novērtējumu
    if videjais >= 7:
        vertejums = "labi"
    elif videjais >= 4:
        vertejums = "vidēji"
    else:
        vertejums = "jāuzlabo"

    # 5️ Sagatavojam vārdnīcu ar rezultātiem
    rezultats = {
        "skaits": skaits,
        "videjais": videjais,
        "augstakais": augstakais,
        "vertejums": vertejums
    }

    return rezultats


#Pārbaude
parbaude = [6, 8, 7, 9]
rezultats = analize_vertejumus(parbaude)
print(rezultats)