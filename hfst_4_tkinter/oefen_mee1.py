# Maak een GUI met minstens drie aparte labels:
# inhoud van labels is: Hallo, Klas en 6IICT.

# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()


# Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
label = tk.Label(master=venster, text="Hallo")
label1 = tk.Label(master=venster, text="klas")
label2 = tk.Label(master=venster, text="6IICT")
# Label toevoegen aan de master (in dit geval venster).
label.pack()
label1.pack()
label2.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()

