class Hond:
    def __init__(self,benoem,gewicht):
        self.benoem=benoem
        self.gewicht=gewicht 
    def blaf(self):
        print(f"{self.benoem} zegt blaf{self.gewicht}")



hond  = Hond("Floris",10)
hond.blaf()

hond2 = Hond("fido",9)
hond2.blaf()