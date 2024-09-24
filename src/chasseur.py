from .personnage import Personnage

class Chasseur(Personnage):
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        super().__init__(nom, sexe, faction, niveau, points_de_vie, arme)
        self.focus = 100

    def tir_precis(self, cible):
        if self.focus >= 25:
            print(f"{self.nom} effectue un Tir Précis sur {cible.nom} !")
            self.focus -= 25
        else:
            print(f"{self.nom} n'a pas assez de focus pour effectuer un Tir Précis.")

    def appel_animal(self):
        print(f"{self.nom} appelle un animal de compagnie !")