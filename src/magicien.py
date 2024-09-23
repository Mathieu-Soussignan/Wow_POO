from .personnage import Personnage

class Magicien(Personnage):
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        super().__init__(nom, sexe, faction, niveau, points_de_vie, arme)
        self.mana = 100

    def lancer_sort(self, sort, cible):
        if self.mana >= 20:
            print(f"{self.nom} lance {sort} sur {cible.nom} !")
            self.mana -= 20
        else:
            print(f"{self.nom} n'a pas assez de mana pour lancer {sort}.")

    def meditation(self):
        self.mana += 30
        print(f"{self.nom} médite et récupère 30 points de mana.")