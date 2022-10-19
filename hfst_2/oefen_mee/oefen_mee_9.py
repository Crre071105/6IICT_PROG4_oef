import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/Oefen_mee_9.json", "r")
dagen = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar
print(dagen)
