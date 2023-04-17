import tkinter as tk
counter = 0
venster = tk.Tk()
label1 = tk.Label(master=venster, text = "Te doorzoeken tekst", font=("Helvetica",20))
label1.grid(row=1, column=0)

label2 = tk.Label(master=venster, text = "Letter", font=("Helvetica",20))
label2.grid(row=1, column=1)

doorzoek = tk.Entry(master=venster, width=33, font=("Helvetica",14),
                  border=10, borderwidth=5,text ="test")
doorzoek.grid(row=2, column=0)

link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14), 
                  border=10, borderwidth=5)
link_2.grid(row=2, column=1)
test = tk.Entry(venster)
test.grid(row=4, column=0, columnspan=2)
def zoeken():
    global counter
    woord = doorzoek.get()
    letter = link_2.get()
    for x in woord:
        if x == letter:
            counter +=1
    print(counter)
    test.delete(0,tk.END)
    test.insert(0,counter)
    counter =0

knop = tk.Button(master=venster, command=zoeken, text="zoeken", width=75)
knop.grid(row=3, column=0, columnspan=2)

venster.mainloop()