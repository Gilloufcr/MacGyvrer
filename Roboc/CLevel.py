# -*-coding:Utf-8 -*

from pathlib import Path

mon_rep_cartes = Path(__file__).parent / "cartes"


class Level():
    
    def __init__(self, maps):
        self.maps = maps
        self.list_level = self.create_level(maps)
        self.position = self.find_mac()
        self.exit = self.find_exit()
        
        
    def create_level(self, maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            list_level = []
            for line in level.splitlines():
                list_level.append(list(line))
        return list_level
    
    def display_level(self):
        for line in self.list_level:
            line_to_display = ""
            for elements in line:
                line_to_display += elements
            print(line_to_display)
            
    def find_mac(self):
        for i, line in enumerate(self.list_level):
            try:
                position = [i, line.index("X")]
            except:
                pass
        return position
    
    def find_exit(self):
        for i, line in enumerate(self.list_level):
            try:
                position = [i, line.index("U")]
            except:
                pass
        return position
                                
        
