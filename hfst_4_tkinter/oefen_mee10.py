# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: vertaal input van gebruiker naar het Engels
if kleur == "rood":
    kleurachtergrond = "red"
if kleur == "blauw":
    kleurachtergrond = "blue"
if kleur == "groen":
    kleurachtergrond = "green"
def invoegen():
    label_1 = tk.Label(master=venster, text=f"De kleur is {kleur}",bg=kleurachtergrond)
    label_1.pack()

# TODO: maak functie aan die het label in de ingegeven kleur laat zien.

knop = tk.Button(master=venster, text="Klik op mij!", command=invoegen)
knop.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()