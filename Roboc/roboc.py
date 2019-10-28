# -*-coding:Utf-8 -*
"""Fichier Principal du jeux de labyrinthe"""

import os
from pathlib import Path
from Roboc.classes import Moove

continuer_partie = True
choix_carte = ""
choix_menu = ""
X = Moove()
mon_rep_cartes = Path(__file__).parent / "cartes"


while continuer_partie == True:
    """Tant que la partie n'est pas fini, on a atteint la sortie U"""
    
    """Menu"""
    choix_menu = input("Merci de faire un choix : \n 1-)Selection du niveau, 1, 2, 3 \n 2-)Quitter \n\nVotre choix : ")
        
    if choix_menu == '1':
    
        choix_carte = input("Merci de Choisir une cartes parmis la liste suivante 1,2,3 : ")

        with open(str(mon_rep_cartes) + "/" + choix_carte + ".txt", 'r') as contenu:
            level = contenu.read()
        print(level)
        continuer_partie = False
        
    if choix_menu == '2':
        continuer_partie = False
