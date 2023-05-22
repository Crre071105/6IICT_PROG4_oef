class Hond:
    def benoem(self,benaming):
        self.naam = benaming    
    def blaf(self):
        print(f"{self.naam} zegt blaf")
    def massa(self,gewicht):
        self.kilo=gewicht
    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.kilo}kg")


hond  = Hond()
hond.benoem("sem")
hond.blaf()
hond.massa()
hond.weegschaal()