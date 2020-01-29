# -*-coding:Utf-8 -*

from pathlib import Path
from ccaracter import Caracter
import random

mon_rep_cartes = Path(__file__).parent / "cartes"
cartes_temp = Path(__file__).parent / "temp"

class Level():
    
    def __init__(self, maps):
        self.maps = maps
        self.positionmc = (-1, -1)
        self.wall = []
        self.guardian = []
        self.spaces = []
        self.first_elements_position = {}
        self.dict_objects = {}
        self.list_level = []
        self.create_level(self.maps)
       
    def create_level(self, maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            for i, line in enumerate(level.splitlines()):
                list_line = []
                for j, elements in enumerate(line):
                    if elements == "X":
                        self.positionmc = (j, i)
                        self.spaces.append((j, i))
                    elif elements == "O":
                        self.wall.append((j,i))
                    elif elements == "G":
                        self.guardian.append((j,i))
                    elif elements == " ":
                        self.spaces.append((j,i))
 
                    list_line.append(elements)
                
                self.list_level.append(list_line)

            position_P = random.choice(self.spaces)
            del self.spaces[self.spaces.index(position_P)]
            position_N = random.choice(self.spaces)
            del self.spaces[self.spaces.index(position_N)]
            position_E = random.choice(self.spaces)
            del self.spaces[self.spaces.index(position_E)]
            self.dict_objects[position_P] = ("P")
            self.dict_objects[position_N] = ("N")
            self.dict_objects[position_E] = ("E")
            print(self.dict_objects)
            for key in self.dict_objects.keys():
                self.list_level[key[1]][key[0]] = self.dict_objects[key]   

        return self.list_level        
    
    def display_level(self, positionmac=()):
        print("ici", positionmac)
        if positionmac != ():
            self.list_level[self.positionmc[1]][self.positionmc[0]] = " "
            print("position mc", self.positionmc)
            print("position mac", positionmac)
            self.list_level[positionmac[1]][positionmac[0]] = "X"
            self.positionmc = positionmac

        for line in self.list_level:
            line_to_display = ""
            for elements in line:
                line_to_display += elements
            print(line_to_display)

    def copy_level(self, maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            write_maps = contenu.read()
            maps_temps = open(str(cartes_temp) + "/" + maps + ".txt", "w")
            maps_temps.write(write_maps)
            maps_temps.close()

    def write_level(self, maps, positionmac):
        with open(str(cartes_temp) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            p_old0 = self.level_positionmc[0]
            p_old1 = self.level_positionmc[1]
            print("Position (if) P_old0 at the begenin of function", p_old0)
            print("Position (if) P_old1 at the begenin of function", p_old1)
            p_0 = positionmac[1]
            p_1 = positionmac[0]
            maps_to_update = [list(i) for i in level.splitlines()]
            maps_to_update[p_old0][p_old1] = " "
            maps_to_update[p_0][p_1] = "X"
            p_old0 = p_0
            p_old1 = p_1
            print("new position of P_Old0 ",p_old0)
            print("new position  of P_Old1 ",p_old1)
            self.level_positionmc = (p_old0, p_old1)
            print("Position Of Level_Positionmc, After Update",self.level_positionmc)
        
        #print(maps_to_update)
        maps_temps = open(str(cartes_temp) + "/" + maps + ".txt", "w")
        lines = ""
        for line in maps_to_update:
            line_to_display = ""
            for elements in line:
                line_to_display += elements
            lines += line_to_display
            lines += '\n'
            print(line_to_display)
        maps_temps.write(lines)
        maps_temps.close()

