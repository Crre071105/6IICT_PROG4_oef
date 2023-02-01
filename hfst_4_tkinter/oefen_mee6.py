# Zoek de betekenis van een aantal parameters uit.
# Zijn deze parameters bruikbaar bij Button en/of Label?
import tkinter as tk

venster = tk.Tk()

# Functie maakt een label aan wanneer opgeroepen.
def knop_klik():
    label =tk.Button(master=venster, text="Klik op mij!", command=knop_klik)
    label.pack()

# Knop aanmaken.
    # master: geef aan tot welke GUI de knop behoort.
    # text: boodschap van de knop.
    # command: aan welke functie is de knop gelinkt.
knop = tk.Button(master=venster, text="Klik op mij!", command=knop_klik)

knop.pack()

venster.mainloop()