#16.04.2026
#🧩 Treniņuzdevums
#Izpildes nosacījumi
#🎮 Spēles punktu aprēķins
#Problēma
#Tiek veidota vienkārša datorspēle, kurā spēlētājs krāj punktus. Punktu skaits ir atkarīgs no spēles līmeņa, savāktajiem bonusiem un tā, vai spēlētājs ir izmantojis “dubulto punktu” režīmu.

#📄 Specifikācija
#● Funkcijai rekini_punktus ir trīs parametri:
#rekini_punktus(limenis, bonusi, dubultie)

#limenis — vesels skaitlis (spēles līmenis)
#bonusi — vesels skaitlis (savākto bonusu skaits)
#dubultie — Būla tipa mainīgais (True vai False)
#● Punktu aprēķins:

#par katru līmeni: 100 punkti
#par katru bonusu: 20 punkti
#● Ja dubultie ir True:

#visi punkti tiek dubultoti
#● Ja kopējais punktu skaits pārsniedz 1000:

#tiek piešķirts papildus bonuss 150 punkti
#❓ Uzdevumi
#Vai specifikācijā ir minēts viss nepieciešamais?
#Kāda papildu informācija būtu vajadzīga?
#Kādus jautājumus tu uzdotu skolotājam?
#💻 Praktiskā daļa
#Uzdod jautājumus un uzprogrammē funkciju!

#Pārbaude:
 
#rekini_punktus(5, 10, True)


#funkcijas izveidošana

def rekini_punktus(limenis, bonusi, dubultie):

    #Punktu aprēķins - pamata punkti
    #par katru līmeni: 100 punkti
    #par katru bonusu: 20 punkti
    pamataPunkti = limenis * 100 + bonusi * 20 

    #● Ja dubultie ir True:
    #visi punkti tiek dubultoti
    if dubultie: #dubultie == True
        punkti = pamataPunkti * 2


    #● Ja kopējais punktu skaits pārsniedz 1000:
    #tiek piešķirts papildus bonuss 150 punkti
    if punkti > 1000:
        punkti = punkti + 150
    else:
        punkti = punkti + 150

    return punkti

print(rekini_punktus(100, 10, False))



