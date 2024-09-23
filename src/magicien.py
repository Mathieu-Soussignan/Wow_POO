class Magicien:
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, armes):
        self.nom = nom
        self.sexe = sexe
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.armes = armes

    def afficher(self):
        return (f"Le/La Magicien(ne) s'appelle {self.nom}, il/elle est de sexe {self.sexe},"
                f"il/elle apparait à la faction {self.faction}, il/elle est de niveau {self.niveau},"
                f"il/elle a {self.points_de_vie} points de vies, et il/elle manie un(e) {self.armes}.")
        

#initialisation d'un chasseur 
magicien1 = Magicien("Gandalf", "Masculin", "Alliance", 13, 90, ["Baton"])
print(magicien1.afficher())
