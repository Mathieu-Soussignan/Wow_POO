from .personnage import Personnage

class Voleur(Personnage):
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        super().__init__(nom, sexe, faction, niveau, points_de_vie, arme)
        self.chackra = 100

    def coup_de_dague(self, cible):
        if self.chackra >= 25:
            print(f"{self.nom} effectue un Coup de dague sur {cible.nom} !")
            self.chackra -= 25
        else:
            print(f"{self.nom} n'a pas assez de chackra pour effectuer un Coup de dague.")  

    def chidori(self, cible):
        if self.chackra >= 25:
            print(f"{self.nom} lance un Chidori sur {cible.nom} !")
            self.chackra -= 25
        else:
            print(f"{self.nom} n'a pas assez de chackra pour lancer un Chidori.")