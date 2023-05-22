class Hond:
    def __init__(self,naam,gewicht):
        self.naam=naam
        self.gewicht=gewicht
    def praat(self):
        print(f"{self.naam} weegt {self.gewicht}kilo")
    def benoem(self,nieuweNaam):
        print(f"{self.naam} heet nu {nieuweNaam}")
        self.naam=nieuweNaam
    def eten(self,hoeveelheid):
        for i in range(3):
            self.gewicht = self.gewicht+(0.3*hoeveelheid)
            print(f"{self.naam} weegt {self.gewicht}")




hond = Hond("Floris",4)
hond.praat()
hond.benoem("sem")
hond.eten(0.5)

# hond2 = Hond("fido",9)
# hond2.praat()