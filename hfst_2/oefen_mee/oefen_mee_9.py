import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/Oefen_mee_9.json", "r")
quiz = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar
print(quiz)
for key,onderwerp in quiz["quiz"].items():
        for key3,vraag in onderwerp.items():
            print(vraag["vraag"])
            print(vraag["opties"])
            antwoord = input("Kies het juiste antwoord \n")
            if antwoord == (vraag["antwoord"]):
                print("juist")
            else:
                print("fout")