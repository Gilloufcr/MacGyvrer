# -*-coding:Utf-8 -*

from pathlib import Path

mon_rep_cartes = Path(__file__).parent / "cartes"


class Level():
    
    def __init__(self, maps):
        self.maps = maps
        self.list_level = self.create_level(maps)
        
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
    
    def display_level(self):
        for line in self.list_level:
            line_to_display = ""
            for elements in line:
                line_to_display += elements
            print(line_to_display)
            
                                
        
