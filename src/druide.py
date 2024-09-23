from .personnage import Personnage

class Druide(Personnage):
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        super().__init__(nom, sexe, faction, niveau, points_de_vie, arme)
        self.forme = "Humaine"

    def metamorphose(self, nouvelle_forme):
        print(f"{self.nom} se transforme en forme {nouvelle_forme} !")
        self.forme = nouvelle_forme

    def soin(self, cible):
        print(f"{self.nom} soigne {cible.nom} !")
