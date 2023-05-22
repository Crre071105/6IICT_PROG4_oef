class Auto:
    def __init__(self,verbruik,kleur,tank_vol,tank_huidig):
        self.verbruik=verbruik
        self.kleur=kleur
        self.tank_vol = tank_vol
        self.tank_huidig = tank_huidig
    def verven(self,nieuwe_kleur):
        self.kleur=nieuwe_kleur
        print(f"mijn auto is nu {self.kleur}")
    def check_tank(self):
        afstand = self.tank_huidig*self.verbruik
        print(f"Met een tank van {self.tank_huidig}L, kan je nog { afstand }km rijden")
    def tanken(self):
        hoeveelheid = self.tank_vol-self.tank_huidig
        self.tank_huidig=self.tank_vol
        print(f"Je hebt {hoeveelheid}L getankt, er zit nu {self.tank_huidig}L in de tank")
    def rijden(self,afstand):
        if self.tank_huidig*self.verbruik >= afstand:
            x = afstand/self.verbruik
            self.tank_huidig = self.tank_huidig-x
            print(f"{afstand} afgelegd, nog {self.tank_huidig}L in de tank")
        else:
            print(f"je kan niet zover rijden op een tank van {self.tank_huidig}L")

auto = Auto(20,"rood",100,30)
auto.verven("blauw") # Mijn auto is nu blauw.

auto.check_tank()    # Met een tank van 30 liter, kan ik nog 600km rijden.
auto.rijden(400)     # 400km afgelegd, nog 10.0 liter over.
auto.check_tank()    # Met een tank van 10 liter, kan ik nog 200km rijden.
5
auto.rijden(400)     # Kan niet zover rijden op een tank van 10.0 liter.
auto.tanken()
auto.check_tank()    # Met een tank van 100 liter, kan ik nog 2000km rijden.