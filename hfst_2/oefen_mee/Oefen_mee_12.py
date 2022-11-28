
import json
# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/Oefen_mee12.json", "r")
dagen = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar
x = input("kies een dag ")
print(dagen[x])
fp_aanpassen = open("hfst_2/oefen_mee/Oefen_mee12.json", "w")
Wijzig = input("Wil je deze dag wijzigen (Y/N)")
if Wijzig == "Y":
    nieuwe_keuze = input("Geef nieuwe activiteit in ")
    dagen[x]=nieuwe_keuze
    json.dump(dagen,fp_aanpassen)
fp_aanpassen.close()
print(dagen)
