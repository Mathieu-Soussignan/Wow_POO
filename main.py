from src.guerrier import Guerrier
from src.magicien import Magicien
from src.chasseur import Chasseur
from src.druide import Druide

def main():
    guerrier = Guerrier("Grommash", "Masculin", "Horde", 60, 3487, "Gorehowl")
    magicien = Magicien("Jaina", "Féminin", "Alliance", 60, 2800, "Bâton de givre")
    chasseur = Chasseur("Rexxar", "Masculin", "Horde", 60, 3100, "Arc long")
    druide = Druide("Malfurion", "Masculin", "Alliance", 60, 3200, "Bâton de la nature")

    personnages = [guerrier, magicien, chasseur, druide]

    for personnage in personnages:
        print(personnage.afficher())
        print("-" * 50)

    # Démonstration des comportements
    guerrier.cri_de_guerre()
    guerrier.coup_heroique(magicien)

    magicien.lancer_sort("Boule de feu", guerrier)
    magicien.meditation()

    chasseur.tir_precis(druide)
    chasseur.appel_animal()

    druide.metamorphose("Ours")
    druide.soin(chasseur)

if __name__ == "__main__":
    main()