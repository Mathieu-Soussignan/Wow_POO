from .personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        super().__init__(nom, sexe, faction, niveau, points_de_vie, arme)
        self.rage = 0



