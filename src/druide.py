class Druide:
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
druide1= Druide("Malfurion", "Masculin", "Alliance", 60, 200, ["Baton", "Potion de soin"])
druide1.afficher()