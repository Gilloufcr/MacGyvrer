# -*-coding:Utf-8 -*

from clevel import Level
from getkey import getkey, keys

class Caracter():

    def __init__(self, level_game):

        self.position_0 = level_game.position
        print(self.position_0)



    def move(self, key):
        
        x,y = self.position_0
        if key == keys.UP:
            self.position_0 = [x+1,y]

        print(self.position_0)