# -*-coding:Utf-8 -*

from clevel import Level
from getkey import getkey, keys

class Caracter():

    def __init__(self, level_game):

        self.position_0 = level_game.positionmc
        self.position_wall = level_game.wall
        self.position_pipe = level_game.pipe
        self.level_game = level_game
        print(self.position_0)
        print(self.position_pipe)
        print(self.position_wall)
        


    def move(self, key):
        
        x,y = self.position_0
        #new_position = (x,y)
        if key == keys.UP:
            self.position_0 = (x,y-1)
            if self.position_0 in self.position_wall:
                print("Dans le Mur")
            else:
                print(self.position_0)
        if key == keys.DOWN:
            self.position_0 = (x,y+1)
            if self.position_0 in self.position_wall:
                print("Dans le Mur")
            else:
                print(self.position_0)
        if key == keys.RIGHT:
            self.position_0 = (x+1,y)
            if self.position_0 in self.position_wall:
                print("Dans le Mur")
            else:
                print(self.position_0)
        if key == keys.LEFT:
            self.position_0 = (x-1,y)
            if self.position_0 in self.position_wall:
                print("Dans le Mur")
            else:
                print(self.position_0)

            