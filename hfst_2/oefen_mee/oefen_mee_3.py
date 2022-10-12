import csv #importteer csv 

fp = open( "volcanic-eruptions-EU.csv", "r" )#Open file "volcanic-eruptions-EU.csv" in read modus 
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") #lees het bestand en deel de zin op na elke ; 
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []# maakt lijst aan
for rij in csv_reader:# doorloop alle rijen in csv_read
    eruptions_ll.append(rij)# voeg toe aan de lijst 

fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ll:# voor alle eruption in eruptions_ll
    print(eruption)#print eruption

fp = open( "volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    print(rij)
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")
print(eruptions_ld)
