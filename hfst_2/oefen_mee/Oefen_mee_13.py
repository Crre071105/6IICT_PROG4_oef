import json
import xdrlib
fp  = open("hfst_2/oefen_mee/Oefen_mee13.json", "r")
dagen = json.load(fp)
for index, dag in enumerate(dagen):
    if index >=1:
        waarden_dagen = dag["Cases"]
        waarden_vorige_dag = dagen[index-1]["Cases"]
        waarden_verschil = waarden_dagen-waarden_vorige_dag
        print(f'{dag["Date"]} waren er {waarden_verschil} besmettingen')
    else:
        print(f'{dag["Date"]} waren er geen besmettingen')
        waarden_verschil = 0
    dag["New_Cases"]=waarden_verschil
fp.close()
fp_aanpassen = open("hfst_2/oefen_mee/Oefen_mee13.json", "w")
json.dump(dagen,fp_aanpassen)
fp_aanpassen.close()
