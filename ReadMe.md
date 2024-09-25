# Projet World of Warcraft en Programmation Orientée Objet (POO)

## Table des matières

1. [Introduction](#introduction)
2. [Concepts clés de la POO utilisés dans ce projet](#concepts-clés-de-la-poo-utilisés-dans-ce-projet)
3. [Structure du projet](#structure-du-projet)
4. [Explication détaillée](#explication-détaillée)
   - [La classe de base : Personnage](#la-classe-de-base--personnage)
   - [Les classes spécifiques : Guerrier, Magicien, Chasseur, Druide](#les-classes-spécifiques--guerrier-magicien-chasseur-druide)
   - [Gestion du sexe et de la faction](#gestion-du-sexe-et-de-la-faction)
   - [Polymorphisme](#polymorphisme)
   - [Combat et continué](#combat-et-continué)
   - [Transformation du Druide](#transformation-du-druide)
   - [Utilisation des classes](#utilisation-des-classes)
5. [Conclusion](#conclusion)

## Introduction

Ce projet est une simulation simplifiée de personnages inspirés du jeu World of Warcraft, réalisée en utilisant les principes de la Programmation Orientée Objet (POO) en Python. L’objectif est de comprendre les concepts fondamentaux de la POO à travers un exemple concret et amusant.

## Concepts clés de la POO utilisés dans ce projet

	1.	**Classes** : Modèles pour créer des objets.
	2.	**Objets** : Instances concrètes de classes.
	3.	**Attributs** : Caractéristiques des objets.
	4.	**Méthodes** : Comportements des objets.
	5.	**Héritage** : Création de nouvelles classes basées sur des classes existantes.
	6.	**Polymorphisme** : Capacité des objets de différentes classes à répondre à la même méthode de manière différente.
	7.	**Encapsulation** : Regroupement des données et des comportements dans une même entité (la classe).

## Structure du projet

Le projet est composé de plusieurs fichiers Python, chacun ayant un rôle spécifique :

1. `personnage.py` : Contient la classe de base `Personnage`.
2. `guerrier.py` : Définit la classe `Guerrier`.
3. `magicien.py` : Définit la classe `Magicien`.
4. `chasseur.py` : Définit la classe `Chasseur`.
5. `druide.py` : Définit la classe `Druide`.
6. `voleur.py` : Définit la classe `Voleur`.
7. `main.py` : Script principal qui démontre l'utilisation des classes.

## Explication détaillée

### La classe de base : Personnage

La classe `Personnage` sert de modèle pour tous les types de personnages. Elle définit les attributs et méthodes communs à tous les personnages :

- Attributs : nom, sexe, faction, niveau, points_de_vie, arme
- Méthodes :
- afficher() : Méthode qui adapte la description du personnage en fonction de son sexe et de sa faction (ex. “Le magicien” ou “La magicienne”, “la Horde” ou “l’Alliance”).
- attaquer() : Peut être redéfinie dans les sous-classes pour refléter des attaques spécifiques.

Cette classe utilise le concept d’encapsulation en regroupant les données (attributs) et les comportements (méthodes) liés à un personnage.

### Les classes spécifiques : Guerrier, Magicien, Chasseur, Druide

Ces classes **héritent** de la classe `Personnage`, ce qui signifie qu’elles obtiennent tous les attributs et méthodes de la classe de base. Elles ajoutent ensuite leurs propres attributs et méthodes spécifiques.

Par exemple, la classe `Guerrier` ajoute :
- Un attribut `rage`
- Des méthodes `cri_de_guerre()` et `coup_heroique()`

Ceci illustre le concept d’**extension** de classe par héritage.

### Gestion du sexe et de la faction

La méthode afficher() dans la classe Personnage a été adaptée pour prendre en compte le sexe du personnage et ajuster l’article et le nom de la classe en conséquence. Par exemple :

- Pour un personnage de sexe féminin de la classe Magicien, la sortie sera “La magicienne” plutôt que “Le magicien”.
- Les factions sont également gérées, en affichant “la Horde” ou “l’Alliance” selon le choix du personnage.

### Polymorphisme

Bien que toutes les classes héritent de Personnage, elles peuvent avoir des comportements différents pour les mêmes méthodes. Par exemple, la méthode attaquer() pourrait être redéfinie dans chaque classe pour refléter le style de combat unique de chaque type de personnage. C’est ce qu’on appelle le **polymorphisme**.

### Combat et continué

Le système de combat permet à l’utilisateur de choisir le personnage qui entre en combat et d’effectuer une attaque. Après chaque attaque, l’utilisateur a la possibilité de continuer le combat jusqu’à ce que l’un des personnages soit à court de points de vie. En cas de mauvaise saisie (par exemple, un mauvais choix de personnage ou d’attaque), une erreur est affichée et l’utilisateur est invité à refaire un choix valide.

### Transformation du Druide

Lorsque le Druide entre en combat, il a la possibilité de se métamorphoser en différentes formes. L’utilisateur peut choisir parmi plusieurs transformations : forme d’ours, de chat, de corbeau et d’arbre, chacune ayant des effets et des attaques spécifiques.

### Utilisation des classes

Dans le fichier main.py, nous créons des instances (objets) de chaque classe de personnage. Cela démontre comment les classes servent de “moules” pour créer des objets concrets.
Nous avons également utilisé des listes pour stocker les personnages et les attaques disponibles, ce qui permet une gestion plus facile des données.

## Conclusion

Ce projet illustre comment la POO permet de créer un code structuré, réutilisable et facile à comprendre. En modélisant les personnages comme des objets avec des attributs et des comportements, nous créons une représentation intuitive du monde du jeu.