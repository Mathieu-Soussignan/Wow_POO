class Personnage:
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        self.nom = nom
        self.sexe = sexe
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.arme = arme
    
    def afficher(self):
        return (f"Le/La {self.__class__.__name__} s'appelle {self.nom}, il/elle est de sexe {self.sexe}, "
                f"il/elle appartient à la faction {self.faction}, il/elle est de niveau {self.niveau}, "
                f"il/elle a {self.points_de_vie} points de vie, et il/elle manie un(e) {self.arme}.")
    
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec {self.arme}!")