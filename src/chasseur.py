class Chasseur:
    def __init__(self, nom, sex, faction, niveau, points_de_vie, armes):
        self.nom = nom
        self.sex = sex
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.armes = armes

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Sexe: {self.sex}")
        print(f"Faction: {self.faction}")
        print(f"Niveau: {self.niveau}")
        print(f"Points de vie: {self.points_de_vie}")
        print(f"Armes: {', '.join(self.armes)}")
        
    

#initialisation d'un chasseur 
chasseur1 = Chasseur("Legolas", "Masculin", "Alliance", 9, 110, ["Arc", "Dagues"])
chasseur1.afficher()
