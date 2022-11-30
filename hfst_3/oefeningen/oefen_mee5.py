""" Niveau 1 & 2
Wat gaat hier mis?
"""
try:
    fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )
    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except ValueError:
    print("je moest een cijfer opgeven")
except IndexError:
    print("opgegeven getal gaat buiten de lijst")


""" Niveau 3 (haal uit commentaar) """
while True:
    fruit = input("Element aan lijst toevoegen: ")
    
    if fruit == "":
        break # Loop stopt wanneer gebruiker een lege string ingeeft.
    else:
        fruit_lijst.append(fruit)

print(fruit_lijst)
