## pelin aloitus
print("Tervetuloa tietokone visaan!")
print("-" *30)
print("")

## aloituspistemäärä
pisteet = 0

## itse peli
kysymys1 = input("Mikä on yleisin käyttöjärjestelmä pc-tietokoneissa (pelkkä nimi, ei versio numeroita)? ")
if kysymys1 == "Windows":
    print("Aivan oikein!")
    pisteet +=1
elif kysymys1 != "Windows":
    print("Voi ei, väärä vastaus.")
kysymys2 = input("Intelin kilpailija pc-markkinoilla on? ")
if kysymys2 == "AMD":
    print("Hyvin tiedetty, vastauksesi on oikein.")
    pisteet +=1
elif kysymys2 != "AMD":
    print("Voi ei, väärä vastaus.")
kysymys3 = input("Mikä on kolmikirjaiminen tietokonefirma, joka valmisti mm. Thinkpadeja? ")
if kysymys3 == "IBM":
    print("Hyvä sinä, vastauksesi oli oikein.")
    pisteet +=1
elif kysymys3 != "IBM":
    print("Väärin, etkö tosiaan ole ikinä kuullut IBM:stä.")
kysymys4 = int(input("Dual-core prosessorissa ytimiä on? "))
if kysymys4 == 2:
    print("Oikein!")
    pisteet +=1
elif kysymys4 != 2:
    print("Väärin, ytimiä on tietysti kaksi.")
kysymys5 = input("Vuonna 1972 keksitty ohjelmointikieli jolla mm. Linux-ydin on koodattu? ")
if kysymys5 == "C":
    print("Näin on.")
    pisteet +=1
elif kysymys5 != "C":
    print("Väärin, jäit nollille!")
kysymys6 = input("Mikä Nvidian käyttämä lyhenne tarkoittaa että näytönohjain tukee säteenseurantaa? ")
if kysymys6 == "RTX":
    print("Erinomaista!")
    pisteet +=1
elif kysymys6 != "RTX":
    print("Väärä vastaus.")
print("")
print("Sait", pisteet, "pistettä")
