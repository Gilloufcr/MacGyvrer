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
        self.pipe = (-1, -1)
        self.list_level = self.create_level(maps)
       
    def create_level(self, maps):
        with open(str(cartes_temp) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            list_level = []
            for i, line in enumerate(level.splitlines()):
                list_line = []
                for j, elements in enumerate(line):
                    if elements == "X":
                            self.positionmc = (i, j)
                    if elements == "O":
                            self.wall.append((i,j))
                    if elements == "T":
                            self.pipe = (i,j)
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

    def __init__(self, maps, positionmac):
        self.maps = maps
        self.positionmac = positionmac

    def write_level(self, maps, positionmac):
        with open(str(cartes_temp) + "/" + maps + ".txt", 'r') as contenu:
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
            
            p_1 = positionmac[0]
            p_2 = positionmac[1]
            self.positionmac_ok = [p_1, p_2]
            print(self.positionmac_ok)
            

        for line in list_level:
            line_to_write = ""
            for elements in line:
                line_to_write += elements
            print(line_to_write)
