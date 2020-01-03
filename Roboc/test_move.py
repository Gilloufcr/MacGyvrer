# -*-coding:Utf-8 -*

import os
from getkey import getkey, keys
from pathlib import Path

mon_rep_cartes = Path(__file__).parent / "cartes"


continuer_partie = True
choix_menu = ""


while continuer_partie == True:
    """Tant que la partie n'est pas fini, on a atteint la sortie U"""
    
    """Menu"""
    choix_menu = input("Merci de faire un choix : \n 1-)Selection du niveau, 1, 2, 3 \n 2-)Quitter \n\nVotre choix : ")
        
    if choix_menu == '1':
    
        choix_carte = input("Merci de Choisir une cartes parmis la liste suivante 1,2,3 : ")

        def positions(maps):
            with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
                level = contenu.read()
                macgyvrer = ()
                wall = []
                pipe = ()
                for i, j in enumerate(level.splitlines()):
                    for k, l in enumerate(j):
                        if l == "X":
                            macgyvrer = (i, k)
                        if l == "O":
                            wall.append((i,k))
                        if l == "T":
                            pipe = (i,k)

                    
            print(macgyvrer)
            print(wall)
            print(pipe)
            return macgyvrer, wall

        def display_level(List_level):
            for line in List_level:
                line_to_display = ""
                for elements in line:
                    line_to_display += elements
                print(line_to_display)


        play_level = positions(choix_carte)
        
        
        
        continuer_partie = False
        
    if choix_menu == '2':
        continuer_partie = False






