# Open lied.txt in Python
lied = open("hfst_1/opdrachten/lied.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
# Test inhoud van lied
print(lied)

""" Begin eigen code hier """
nieuwe_dict = {}


lied = lied.split()

for index,waarden in enumerate(lied):
    if waarden in nieuwe_dict:
        nieuwe_dict[waarden] += 1 
    else:
        nieuwe_dict[waarden] = 1
print (nieuwe_dict)

