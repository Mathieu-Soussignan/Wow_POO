class Personnage:
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        self.nom = nom
        self.sexe = sexe
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.__arme = arme
        self.__experience = 500
    
    @property
    def experience(self):
        return self.__experience
    
    @property
    def arme(self):
        return self.__arme
    
    #Mutateurs
    def set_arme(self, arme):
        self.__arme = arme
    
    def gagner_experience(self, points):
        if points > 0:
            self.__experience += points
            print(f"{self.nom} a gagné {points} points d'expérience.")
        else:
            print("Les points d'expérience doivent être positifs.")

        
    def afficher(self):
        # Détermination des articles et pronoms en fonction du sexe
        pronom = "La" if self.sexe == "féminin" else "Le"
        pronom_possessif = "elle" if self.sexe == "féminin" else "il"
        article_faction = "l'" if self.faction == "Alliance" else "la "

        nom_classe = self.__class__.__name__.lower()
        # Construction de la phrase
        return (f"{pronom} {nom_classe} s'appelle {self.nom}, {pronom_possessif} est de sexe {self.sexe}, "
                f"{pronom_possessif} appartient à la faction de {article_faction}{self.faction}, "
                f"{pronom_possessif} est de niveau {self.niveau}, "
                f"{pronom_possessif} a {self.points_de_vie} points de vie, "
                f"et {pronom_possessif} manie un(e) {self.arme}, {pronom_possessif} a gagné {self.__experience} points d'expérience.")

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec {self.arme}!")