class Guerrier:

    def __init__(self, nom, sexe, faction, niveau, points_de_vie, armes):
        self.nom = nom
        self.sexe = sexe
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.armes = armes
        
    def afficher(self):
        return (f"Le/La Guerrier(e) s'appelle {self.nom}, il/elle est de sexe {self.sexe},"
                f"il/elle apparait à la faction {self.faction}, il/elle est de niveau {self.niveau},"
                f"il/elle a {self.points_de_vie} points de vies, et il/elle manie un(e) {self.armes}.")
    
guerrier1 = Guerrier("Grommash", "Masculin", "Horde", 60, 3487, "Gorehowl")
guerrier2 = Guerrier("Garrosh", "Masculin", "Horde", 60, 3269, "Gorehowl")
print(guerrier1.afficher())
print(guerrier2.afficher())
