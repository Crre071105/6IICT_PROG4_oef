# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

woord = ""


veld = tk.Entry(master=venster, font=("Helvetica",14), border=10, borderwidth=5)
veld.grid(row=0, column=0)
# TODO: functie aanmaken gelinkt aan Button knop.

#       Doel van functie is toevoegen van Entry veld aan Label onder de knop.
def invoegen():
    global woord
    zin = veld.get()
    woord += zin
    label_1 = tk.Label(master=venster, text=woord)
    label_1.grid(row=2, column=0)
knop = tk.Button(master=venster, command=invoegen, text="Voeg toe aan string:", width=50)
knop.grid(row=1, column=0, pady=10, padx= 10)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()