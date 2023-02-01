# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

# Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
label_1 = tk.Label(master=venster, text="Hallo")
label_2 = tk.Label(master=venster, text= "klas")
label_3 = tk.Label(master=venster, text= "6IICT!")
label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=1, column=1)
venster.mainloop()