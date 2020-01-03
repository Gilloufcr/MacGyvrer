# -*-coding:Utf-8 -*
"""Fichier Principal du jeux de labyrinthe a terminer..."""

import os
from getkey import getkey, keys
from clevel import Level, Copy
from ccaracter import Caracter

continuer_partie = True
choix_menu = ""


while continuer_partie == True:
    """Tant que la partie n'est pas fini, on a atteint la sortie U"""
    
    """Menu"""
    choix_menu = input("Merci de faire un choix : \n 1-)Selection du niveau, 1, 2, 3 \n 2-)Quitter \n\nVotre choix : ")
        
    if choix_menu == '1':
    
        choix_carte = input("Merci de Choisir une cartes parmis la liste suivante 1,2,3 : ")
        
        """On copie le fichier de carte pour effectuer la partie"""
        
        copy_maps = Copy(choix_carte)
        copy_maps.copy_level(choix_carte)

        play_level = Level(choix_carte)
        play_level.display_level()
        macgiver = Caracter(play_level)
        macgiver.move(getkey())
        
        continuer_partie = False
        
    if choix_menu == '2':
        continuer_partie = False
