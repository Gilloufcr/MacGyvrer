# -*-coding:Utf-8 -*

from pathlib import Path
from ccaracter import Caracter

mon_rep_cartes = Path(__file__).parent / "cartes"
cartes_temp = Path(__file__).parent / "temp"

class Level():
    
    def __init__(self, maps):
        self.maps = maps
        self.positionmc = (-1, -1)
        self.wall = []
        self.pipe = []
        self.needle = []
        self.ether = []
        self.guardian = []
        self.list_level = self.create_level(maps)
       
    def create_level(self, maps):
        with open(str(cartes_temp) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            list_level = []
            for i, line in enumerate(level.splitlines()):
                list_line = []
                for j, elements in enumerate(line):
                    if elements == "X":
                            self.positionmc = (j, i)
                    if elements == "O":
                            self.wall.append((j,i))
                    if elements == "P":
                            self.pipe.append((j,i))
                    if elements == "N":
                            self.needle.append((j,i))
                    if elements == "E":
                            self.ether.append((j,i))
                    if elements == "G":
                            self.guardian.append((j,i))
                    list_line.append(elements)

                list_level.append(list_line)
            
        return list_level        
    
    def display_level(self):
        for line in self.list_level:
            line_to_display = ""
            for elements in line:
                line_to_display += elements
            print(line_to_display)
                        
        
class Copy():

    def __init__(self, maps):
        self.maps = maps
    
    def copy_level(self, maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            write_maps = contenu.read()
            maps_temps = open(str(cartes_temp) + "/" + maps + ".txt", "w")
            maps_temps.write(write_maps)
            maps_temps.close()


class Write():

    def __init__(self, maps, positionmac, level_game):
        self.maps = maps
        self.positionmac = positionmac
        self.level_positionmc = level_game.positionmc

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
