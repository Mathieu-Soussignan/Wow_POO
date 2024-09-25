from src.magicien import Magicien
from src.guerrier import Guerrier
from src.chasseur import Chasseur
from src.druide import Druide
from src.voleur import Voleur

# Création des personnages
perso1 = Magicien("Jaina", "féminin", "Alliance", 60, 3487, "Gorehowl")
perso2 = Guerrier("Garrosh", "masculin", "Horde", 60, 2880, "Hache de guerre")
perso3 = Chasseur("Rexxar", "masculin", "Horde", 60, 3100, "Arc long")
perso4 = Druide("Malfurion", "masculin", "Alliance", 60, 3200, "Bâton de la nature")
perso5 = Voleur("Kakashi", "masculin", "Horde", 60, 3500, "Dague de l'ombre")

# Liste des personnages disponibles
personnages = [perso1, perso2, perso3, perso4, perso5]

# Liste des attaques disponibles
attaques = {
    "Magicien": ["Boule de feu", "Eclair de givre"],
    "Guerrier": ["Coup héroïque", "Cri de guerre"],
    "Chasseur": ["Tir des arcanes", "Flèche noire"],
    "Druide": ["Lancer d'épines", "Métamorphose"],
    "Voleur": ["Coup de dague", "Chidori"]
}

# Liste des transformations disponibles pour le Druide
transformations_druide = ["Ours", "Chat", "Corbeau", "Arbre"]

# Fonction pour afficher les personnages disponibles
def afficher_personnages():
    print("\nPersonnages disponibles :")
    for i, personnage in enumerate(personnages):
        print(f"{i + 1}. {personnage.nom} ({personnage.__class__.__name__})")

# Fonction pour demander à l'utilisateur de choisir un personnage
def choisir_personnage():
    while True:
        try:
            afficher_personnages()
            choix = int(input("\nChoisissez un personnage (1-5) : "))
            if 1 <= choix <= 5:
                return personnages[choix - 1]
            else:
                raise ValueError("Choix invalide, veuillez choisir un nombre entre 1 et 5.")
        except ValueError as e:
            print(f"Erreur : {e}")

# Fonction pour choisir une attaque
def choisir_attaque(personnage):
    while True:
        try:
            print(f"\nAttaques disponibles pour {personnage.nom} ({personnage.__class__.__name__}) :")
            for i, attaque in enumerate(attaques[personnage.__class__.__name__]):
                print(f"{i + 1}. {attaque}")
            
            choix_attaque = int(input("\nChoisissez une attaque (1-2) : "))
            if 1 <= choix_attaque <= len(attaques[personnage.__class__.__name__]):
                attaque_choisie = attaques[personnage.__class__.__name__][choix_attaque - 1]
                
                # Si le personnage est un Druide et qu'il choisit Métamorphose
                if isinstance(personnage, Druide) and attaque_choisie == "Métamorphose":
                    return choisir_transformation()
                else:
                    return attaque_choisie
            else:
                raise ValueError("Choix invalide, veuillez choisir un nombre correct.")
        except ValueError as e:
            print(f"Erreur : {e}")

# Fonction pour choisir la transformation du Druide
def choisir_transformation():
    print("\nChoisissez une transformation pour le Druide :")
    for i, transformation in enumerate(transformations_druide):
        print(f"{i + 1}. {transformation}")
    
    while True:
        try:
            choix_transformation = int(input("\nChoisissez une transformation (1-4) : "))
            if 1 <= choix_transformation <= len(transformations_druide):
                return transformations_druide[choix_transformation - 1]
            else:
                raise ValueError("Choix invalide, veuillez choisir un nombre correct.")
        except ValueError as e:
            print(f"Erreur : {e}")

# Fonction principale du combat avec option de continuer
def combat():
    while True:
        personnage = choisir_personnage()
        attaque = choisir_attaque(personnage)
        print(f"\n{personnage.nom} se transforme en {attaque} !")
        
        continuer = input("\nSouhaitez-vous continuer le combat ? (o/n) : ")
        if continuer.lower() != 'o':
            print("\nFin du combat.")
            break

if __name__ == "__main__":
    combat()