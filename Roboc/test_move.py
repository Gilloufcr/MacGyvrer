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



def create_level(self, maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            list_level = []
            for i, line in enumerate(level.splitlines()):
                list_line = []
                for j, element in enumerate(line):
                    if element == "X":
                        self.position = [i, j]
                        list_line.append(" ")
                    else:
                        list_line.append(element)

                list_level.append(list_line)
            
        return list_level




   def findChar(self):

       indexR = 0
       indexC = 0
       found = False
       for r in self.mapTile:
           indexC = 0
           for c in r:
               if c == "X":
                   found = True
                   break
               indexC +=1
           if found:
               break
           indexR +=1
       pos = Position(indexR, indexC)
       self.lastPos.addPosition(pos)



  for line in maps_to_update:
            line_to_display = ""
            for elements in line:
                maps_temps = open(str(cartes_temp) + "/" + maps + ".txt", "a")
                line_to_display += elements
            
            maps_temps.write(line_to_display)
            maps_temps.close()      
            


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
       level_to_write = Write(choix_carte, play_level.positionmac, play_level)
       while macgiver.end is not True:
           macgiver.move(key)
           level_to_write.write_level(choix_carte, macgiver.new_positionmc)
           macgiver.end = True
       continuer_partie = False

   if choix_menu == '2':
       continuer_partie = False