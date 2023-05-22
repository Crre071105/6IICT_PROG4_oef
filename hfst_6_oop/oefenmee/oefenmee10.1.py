import random 
locaties = ["living", "tuin", "buren", "keuken"]
class Hond:
    def __init__(self,naam,locatie) :
        
        self.naam = naam
        self.locatie = locatie
    def ziet_hond(self,hond2):
        if (self.locatie) == hond2.locatie:
            print(f"{self.naam} ziet {hond2.naam} in de {self.locatie} ")
            x = random.choice(locaties)
            if x != self.locatie: 
                self.locatie = x
                print(f"{self.naam} is bang en rent naar {self.locatie} ")
        else:
            print(f"{self.naam} ziet {hond2.naam} niet ")
        
hond_1 = Hond("Lulu", "keuken")
hond_2 = Hond("Floris", "keuken")
hond_3 = Hond("Ranger", "tuin")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)
     
