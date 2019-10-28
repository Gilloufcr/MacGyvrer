# -*-coding:Utf-8 -*

from pathlib import Path

mon_rep_cartes = Path(__file__).parent / "cartes"


class Level():
    
    def __init__(self, maps):
        self.maps = maps
        
        
    def create_level(maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            list_level = []
            for line in level.splitlines():
                list_level.append(list(line))
            print(list_level[3][8])
                
        
