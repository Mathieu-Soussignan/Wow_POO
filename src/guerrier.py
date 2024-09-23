from .personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        super().__init__(nom, sexe, faction, niveau, points_de_vie, arme)
        self.rage = 0

    def cri_de_guerre(self):
        self.rage += 20
        print(f"{self.nom} pousse un cri de guerre ! Sa rage augmente de 20 points.")

    def coup_heroique(self, cible):
        if self.rage >= 30:
            print(f"{self.nom} utilise Coup Héroïque sur {cible.nom} !")
            self.rage -= 30
        else:
            print(f"{self.nom} n'a pas assez de rage pour utiliser Coup Héroïque.")