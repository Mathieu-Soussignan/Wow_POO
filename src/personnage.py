class Personnage:
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        self.nom = nom
        self.sexe = sexe
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.arme = arme
    
    # def afficher(self):
    #     if self.sexe == "Féminin" and self.faction == "Horde":
    #         return (f"La {self.__class__.__name__} s'appelle {self.nom}, elle est de sexe {self.sexe}, "
    #             f"elle appartient à la faction de la {self.faction}, elle est de niveau {self.niveau}, "
    #             f"elle a {self.points_de_vie} points de vie, et elle manie un(e) {self.arme}.")
    #     elif self.sexe == "Féminin" and self.faction == "Alliance":
    #         return (f"La {self.__class__.__name__} s'appelle {self.nom}, elle est de sexe {self.sexe}, "
    #             f"elle appartient à la faction de l'{self.faction}, elle est de niveau {self.niveau}, "
    #             f"elle a {self.points_de_vie} points de vie, et elle manie un(e) {self.arme}.")
    #     elif self.sexe == "Masculin" and self.faction == "Horde":
    #         return (f"Le {self.__class__.__name__} s'appelle {self.nom}, il est de sexe {self.sexe}, "
    #             f"il appartient à la faction de la {self.faction}, il est de niveau {self.niveau}, "
    #             f"il a {self.points_de_vie} points de vie, et il manie un(e) {self.arme}.")
    #     elif self.sexe == "Masculin" and self.faction == "Alliance":
    #         return (f"Le {self.__class__.__name__} s'appelle {self.nom}, il est de sexe {self.sexe}, "
    #             f"il appartient à la faction de l'{self.faction}, il est de niveau {self.niveau}, "
    #             f"il a {self.points_de_vie} points de vie, et il manie un(e) {self.arme}.")
        
    def afficher(self):
        # Détermination des articles et pronoms en fonction du sexe
        pronom = "La" if self.sexe == "Féminin" else "Le"
        pronom_possessif = "elle" if self.sexe == "Féminin" else "il"
    
        # Choisir l'article correct avant la faction
        article_faction = "l'" if self.faction == "Alliance" else "la "
    
        # Construction de la phrase
        return (f"{pronom} {self.__class__.__name__} s'appelle {self.nom}, {pronom_possessif} est de sexe {self.sexe}, "
                f"{pronom_possessif} appartient à la faction de {article_faction}{self.faction}, "
                f"{pronom_possessif} est de niveau {self.niveau}, "
                f"{pronom_possessif} a {self.points_de_vie} points de vie, "
                f"et {pronom_possessif} manie un(e) {self.arme}.")
       
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec {self.arme}!")