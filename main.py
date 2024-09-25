import random
from src.magicien import Magicien
from src.guerrier import Guerrier
from src.chasseur import Chasseur
from src.druide import Druide
from src.voleur import Voleur

# Création des personnages
perso1 = Magicien("Jaina", "féminin", "Alliance", 60, 3487, "Baton magique")
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

# Fonction pour choisir la cible à attaquer
def choisir_cible(personnage_actuel):
    while True:
        try:
            print("\nChoisissez une cible pour l'attaque :")
            for i, personnage in enumerate(personnages):
                if personnage != personnage_actuel:  # Exclure le personnage attaquant de la liste des cibles
                    print(f"{i + 1}. {personnage.nom} ({personnage.points_de_vie} PV)")
            
            choix_cible = int(input("\nChoisissez une cible (1-5) : "))
            cible = personnages[choix_cible - 1]
            if cible != personnage_actuel:
                return cible
            else:
                print("Vous ne pouvez pas vous attaquer vous-même.")
        except (ValueError, IndexError) as e:
            print(f"Erreur : {e}")


# Fonction principale du combat avec option de continuer
def combat():
    while True:
        attaquant = choisir_personnage()  # Le joueur choisit son personnage
        attaque = choisir_attaque(attaquant)  # Le joueur choisit l'attaque
        cible = choisir_cible(attaquant)  # Le joueur choisit la cible

        if isinstance(attaquant, Druide) and attaque in transformations_druide:
            print(f"\n{attaquant.nom} s'est transformé en {attaque} !")

            degats_transformation = random.randint(10, 3500)

            cible.points_de_vie -= degats_transformation
            print(f"{attaquant.nom}, sous forme de {attaque}, inflige {degats_transformation} points de dégâts à {cible.nom} !")

            if cible.points_de_vie <= 0:
                print(f"\n{cible.nom} a été vaincu !")
                personnages.remove(cible)  # Retirer le personnage vaincu de la liste
                if len(personnages) == 1:
                    print(f"\n{attaquant.nom} est le dernier survivant !")
                    break  # Fin du combat si un seul personnage reste
        else:
            print(f"\n{attaquant.nom} lance l'attaque {attaque} contre {cible.nom} !")
            attaquant.attaquer(cible)  # Le personnage attaque la cible et inflige des dégâts

            if cible.points_de_vie <= 0:
                print(f"\n{cible.nom} a été vaincu !")
                personnages.remove(cible)  # Retirer le personnage vaincu de la liste
                if len(personnages) == 1:
                    print(f"\n{attaquant.nom} est le dernier survivant !")
                    break  # Fin du combat si un seul personnage reste

        continuer = input("\nSouhaitez-vous continuer le combat ? (o/n) : ")
        if continuer.lower() != 'o':
            print("\nFin du combat.")
            break

if __name__ == "__main__":
    combat()