import random

class Personnage:
    def __init__(self, nom, sexe, faction, niveau, points_de_vie, arme):
        self.__nom = nom
        self.sexe = sexe
        self.faction = faction
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.__arme = arme
        self.__experience = 500

    @property
    def nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    @property
    def experience(self):
        return self.__experience

    @property
    def arme(self):
        return self.__arme

    # Mutateurs
    def set_arme(self, arme):
        self.__arme = arme

    def gagner_experience(self, points):
        if points > 0:
            self.__experience += points
            print(f"{self.nom} a gagné {points} points d'expérience.")
        else:
            print("Les points d'expérience doivent être positifs.")

    def subir_dégâts(self, dégâts):
        self.points_de_vie -= dégâts
        print(f"{self.nom} subit {dégâts} dégâts ! Il reste {self.points_de_vie} points de vie.")
        if self.points_de_vie <= 0:
            print(f"{self.nom} a été vaincu.")

    def attaquer(self, cible):
        dégâts = random.randint(200, 3500)
        print(f"{self.nom} attaque {cible.nom} avec {self.arme} et inflige {dégâts} dégâts.")
        cible.subir_dégâts(dégâts)

    # Nouvelle méthode pour Streamlit
    def afficher_info(self):
        return f"Nom : {self.nom}, Niveau : {self.niveau}, Points de vie : {self.points_de_vie}, Arme : {self.arme}"