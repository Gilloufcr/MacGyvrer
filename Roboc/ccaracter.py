# -*-coding:Utf-8 -*

from getkey import getkey, keys

class Caracter():

    def __init__(self, level_game):

        self.position_0 = level_game.positionmc
        self.position_wall = level_game.wall
        self.position_pipe = level_game.pipe
        self.position_needle = level_game.needle
        self.position_ether = level_game.ether
        self.level_game = level_game 
        self.new_positionmc = (-1, -1)
        self.list_objects = []
        #print(self.position_0)
        #print(self.position_pipe)
        #print(self.position_wall)
        


    def move(self, key):
        
        x,y = self.position_0
        self.list_objects = []
        if key == keys.UP:
            self.position_0 = (x,y-1)
            self.new_positionmc = self.position_0
            if self.new_positionmc in self.position_wall:
                self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.list_objects.append("Pipe")
            if self.new_positionmc in self.position_needle:
                self.list_objects.append("Needle")
            if self.new_positionmc in self.position_ether:
                self.list_objects.append("Ether")
            else:
                print(self.new_positionmc)
        if key == keys.DOWN:
            self.position_0 = (x,y+1)
            self.new_positionmc = self.position_0
            if self.new_positionmc in self.position_wall:
                self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.list_objects.append("Pipe")
            if self.new_positionmc in self.position_needle:
                self.list_objects.append("Needle")
            if self.new_positionmc in self.position_ether:
                self.list_objects.append("Ether")
            else:
                print(self.position_0)
        if key == keys.RIGHT:
            self.position_0 = (x+1,y)
            self.new_positionmc = self.position_0
            if self.new_positionmc in self.position_wall:
                self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.list_objects.append("Pipe")
            if self.new_positionmc in self.position_needle:
                self.list_objects.append("Needle")
            if self.new_positionmc in self.position_ether:
                self.list_objects.append("Ether")
            else:
                print(self.position_0)
        if key == keys.LEFT:
            self.position_0 = (x-1,y)
            self.new_positionmc = self.position_0
            if self.new_positionmc in self.position_wall:
                self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.list_objects.append("Pipe")
            if self.new_positionmc in self.position_needle:
                self.list_objects.append("Needle")
            if self.new_positionmc in self.position_ether:
                self.list_objects.append("Ether")
            else:
                print(self.position_0)

        

            