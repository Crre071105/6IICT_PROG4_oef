class Familie:
    def __init__(self, ras,geslacht,haar,leeftijd,naam) :
        self.ras = ras
        self.geslacht = geslacht
        self.haar = haar
        self.leeftijd = leeftijd
        self.naam = naam
    def is_leeftijd (self):
        return self.leeftijd
    def is_geslacht(self):
        return self.geslacht
    def verjaardag (self):
        self.leeftijd=self.leeftijd+1
        print(f"Gefeliciteerd {self.naam}, je bent nu {self.leeftijd}")
    def verf_haar(self,nieuwe_kleur):
        self.haar = nieuwe_kleur
        print(f"{self.naam} heeft nu {self.haar} haar")
    def uitleg(self):
        print(f"{self.naam}: {self.geslacht}, {self.leeftijd}, {self.haar}, {self.ras}")
        
fam = Familie("mens","Man","paars",39,"Sem")

print(fam.is_leeftijd())
print(fam.is_geslacht())
fam.verjaardag()
fam.verf_haar("rood")
fam.uitleg()