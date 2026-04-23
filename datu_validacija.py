#23.04.2026
#Tēma - Datu validacija

#lietotāja ievade

vecums = input("Ievadi vecumu: ")
print(vecums)

#Pārbaudīt vai ir skaitlis
if vecums.isdigit(): #parbauda vai dotie dati ir skaitli un atgriež  TRUE/FALSE vērtibu
    print("ir skaitlis")

#vecumu parbaude

    if int(vecums) >= 18:
        print("Skolēns ir pilngadīgs.")
    else:
        print("Skolens nav pilngadīgs.")
else:
    print("nav skaitlis")



