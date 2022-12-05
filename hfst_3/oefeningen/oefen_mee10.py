import json

""" Volgende info ontbreekt in oefen_mee10.json:
 - De koningin.
 - Het aantal lopers.

""" 
def schaak_info(info):
        for stuk, stuk_info in info.items():
            zin = f"""Er zijn {stuk_info['aantal']} {stuk}. 
                    De engelse naam is {stuk_info['engelse_naam']}. 
                    Ze bewegen {stuk_info['beweging']}"""
            print(zin)
try:   
    fp = open("oefen_mee10.json", "r")
    info = json.load(fp)
    schaak_info(info)
    fp.close()
except FileNotFoundError:
    print("Kon het opegeven bestand helaas niet vinden, neem contact met ons op. Op onderstaand nummer.")
