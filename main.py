import streamlit as st
from src.magicien import Magicien
from src.guerrier import Guerrier
from src.chasseur import Chasseur
from src.druide import Druide
from src.voleur import Voleur

# Création des personnages
perso1 = Magicien("Jaina", "féminin", "Alliance", 60, 3487, "Bâton magique")
perso2 = Guerrier("Garrosh", "masculin", "Horde", 60, 2880, "Hache de guerre")
perso3 = Chasseur("Rexxar", "masculin", "Horde", 60, 3100, "Arc long")
perso4 = Druide("Malfurion", "masculin", "Alliance", 60, 3200, "Bâton de la nature")
perso5 = Voleur("Kakashi", "masculin", "Horde", 60, 3500, "Dague de l'ombre")

# Liste des personnages actifs
personnages = [perso1, perso2, perso3, perso4, perso5]

# Liste des attaques disponibles
attaques = {
    "Magicien": ["Boule de feu", "Éclair de givre"],
    "Guerrier": ["Coup héroïque", "Cri de guerre"],
    "Chasseur": ["Tir des arcanes", "Flèche noire"],
    "Druide": ["Lancer d'épines", "Métamorphose"],
    "Voleur": ["Coup de dague", "Chidori"]
}

# Formes de transformation pour le Druide
transformations = ["Forme d'ours", "Forme de félin"]

# Fonction pour afficher les personnages disponibles
def afficher_personnages():
    return [p.nom for p in personnages]

def effectuer_attaque(selected_char, target, selected_attack, transformation=None):
    if selected_char.__class__.__name__ == "Druide" and selected_attack == "Métamorphose":
        if transformation == "Forme d'ours":
            dégâts = 1000
            st.write(f"{selected_char.nom} se transforme en ours et inflige {dégâts} dégâts à {target.nom}!")
        elif transformation == "Forme de félin":
            dégâts = 1500
            st.write(f"{selected_char.nom} se transforme en félin et inflige {dégâts} dégâts à {target.nom}!")
        # Appliquer les dégâts à la cible
        target.points_de_vie -= dégâts
    else:
        # Utilisation de la méthode attaquer pour les autres attaques
        selected_char.attaquer(target)
        
    # Vérification des points de vie de la cible
    if target.points_de_vie <= 0:
        st.write(f"{target.nom} a été vaincu !")
        personnages.remove(target)
    else:
        st.write(f"Il reste {target.points_de_vie} points de vie à {target.nom}.")

# Streamlit Interface
st.title("Simulateur de combat World of Warcraft")

# Vérification si le jeu doit s'arrêter
if len(personnages) == 1:
    st.write(f"Le jeu est terminé, {personnages[0].nom} est le dernier survivant !")
else:
    # Étape 1 : Choix du personnage
    st.header("Choisissez votre personnage")
    selected_char_name = st.selectbox("Sélectionnez un personnage :", afficher_personnages())

    # Récupérer le personnage sélectionné
    selected_char = next(p for p in personnages if p.nom == selected_char_name)

    # Afficher les informations du personnage sélectionné
    st.write("### Informations du personnage")
    st.write(selected_char.afficher_info())

    # Étape 2 : Choix de l'attaque
    st.header(f"Choisissez une attaque pour {selected_char.nom}")
    selected_attack = st.selectbox("Sélectionnez une attaque :", attaques[selected_char.__class__.__name__])

    # Si le personnage est un Druide et que l'attaque choisie est Métamorphose
    if selected_char.__class__.__name__ == "Druide" and selected_attack == "Métamorphose":
        transformation = st.selectbox("Choisissez une transformation :", transformations)
    else:
        transformation = None

    # Étape 3 : Choix de la cible
    st.header("Choisissez votre cible")
    target_name = st.selectbox("Sélectionnez une cible :", [p.nom for p in personnages if p.nom != selected_char.nom])

    # Récupérer la cible sélectionnée
    target = next(p for p in personnages if p.nom == target_name)

    # Afficher les informations de la cible
    st.write("### Informations de la cible")
    st.write(target.afficher_info())

    # Étape 4 : Lancer le combat
    if st.button("Lancer le combat"):
        st.write(f"{selected_char.nom} attaque {target.nom} avec {selected_attack} !")
        # Appel à la fonction d'attaque du personnage
        effectuer_attaque(selected_char, target, selected_attack, transformation)

        # Vérification si tous les personnages sont encore en vie
        if len(personnages) == 1:
            st.write(f"{personnages[0].nom} est le dernier survivant ! Le jeu est terminé.")