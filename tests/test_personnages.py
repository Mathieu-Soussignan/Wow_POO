import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.personnage import Personnage
from src.magicien import Magicien
from src.guerrier import Guerrier
from src.chasseur import Chasseur
from src.druide import Druide

# Test de la création d'un personnage de base
def test_personnage_creation():
    perso = Personnage("Thrall", "masculin", "Horde", 10, 100, "épée")
    assert perso.nom == "Thrall"
    assert perso.sexe == "masculin"
    assert perso.faction == "Horde"
    assert perso.niveau == 10
    assert perso.points_de_vie == 100
    assert perso.arme == "épée"

# Test de la méthode afficher()
def test_personnage_afficher():
    perso = Personnage("Thrall", "masculin", "Horde", 10, 100, "épée")
    result = perso.afficher()
    assert "Le personnage s'appelle Thrall" in result
    assert "il appartient à la faction de la Horde" in result

def test_magicien_afficher_feminin():
    mage = Magicien("Jaina", "féminin", "Alliance", 20, 80, "bâton")
    result = mage.afficher()
    assert "La magicienne s'appelle Jaina" in result
    assert "elle appartient à la faction de l'Alliance" in result
    assert "elle a gagné 500 points d'expérience" in result

def test_guerrier_attributs_specifiques():
    guerrier = Guerrier("Garrosh", "masculin", "Horde", 15, 120, "hache")
    assert guerrier.rage == 0
    assert guerrier.niveau == 15

# Test des classes spécifiques
def test_chasseur_creation():
    chasseur = Chasseur("Sylvanas", "féminin", "Horde", 18, 90, "arc")
    assert chasseur.focus == 100
    assert chasseur.arme == "arc"

def test_druide_creation():
    druide = Druide("Malfurion", "masculin", "Alliance", 22, 110, "bâton")
    assert druide.points_de_vie == 110
    assert druide.arme == "bâton"