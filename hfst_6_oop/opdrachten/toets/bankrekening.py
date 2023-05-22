class Bankrekening():
    bank = "KBC"
    def __init__(self, eigenaar, geld, leeftijd ):
        self.eigenaar = eigenaar
        self.geld = geld
        self.leeftijd = leeftijd
    def storten(self,bedrag,bericht):
        self.geld = self.geld + bedrag
        print(f"{bedrag} euro toegevoegd. Reden: {bericht}")
    def afhalen(self,bedrag,bericht):
        if self.leeftijd >=16:
            if bedrag <=self.geld:
                self.geld = self.geld - bedrag
                print(f"{bedrag} euro afgehaald. Reden: {bericht}")
            else:
                print(f"{self.eigenaar} heeft te weinig geld op zijn rekening")
        else:
            print(f"{self.eigenaar} is te jong om geld af te halen")
    def overzicht(self):
        print(f"{self.eigenaar} heeft {self.geld} euro staan bij {Bankrekening.bank}")
    def overschrijven(self,bedrag,andere_rekening):
        ## indien regel 22 in commentaar staat dan werkt hij wel (rekening_1.overschrijven(10, "GEEN REKENING"))
        if self.geld >=bedrag:
            andere_rekening.geld = andere_rekening.geld + bedrag
            self.geld = self.geld - bedrag
