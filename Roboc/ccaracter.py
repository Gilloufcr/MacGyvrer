# -*-coding:Utf-8 -*

from getkey import getkey, keys

class Caracter():

    def __init__(self, level_game):

        self.position_0 = level_game.positionmc
        self.position_wall = level_game.wall
        self.position_pipe = level_game.pipe
        self.position_needle = level_game.needle
        self.position_ether = level_game.ether
        self.position_guardian = level_game.guardian
        self.position_spaces = level_game.spaces
        self.level_game = level_game 
        self.new_positionmc = ()
        self.objects = []
        self.end = False
        print("Position of Mac when Level Is Created", self.position_0)
        #print(self.position_pipe)
        #print(self.position_wall)
        


    def move(self, key):
        
        x,y = self.position_0
        objects = ""
        if key == keys.UP:
            print("Position in UP time", self.position_0)
            self.new_positionmc = (x,y-1)
            if self.new_positionmc in self.position_spaces:
                self.position_0 = (x,y-1)
                self.position_spaces.append(self.position_0)
            if self.new_positionmc in self.position_wall:
                #self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.objects.append("Pipe")
                self.position_pipe = (-15,-15)
                self.position_0 = (x,y-1)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_needle:
                self.objects.append("Needle")
                self.position_needle = (-15,-15)
                self.position_0 = (x,y-1)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_ether:
                self.objects.append("Ether")
                self.position_ether = (-15,-15)
                self.position_0 = (x,y-1)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_guardian:
                self.position_0 = (x,y-1)
                self.end = True
            else:
                print("Position in move Key Selected", self.new_positionmc)
        
        if key == keys.DOWN:
            print("Position in DOWN time", self.position_0)
            self.new_positionmc = (x,y+1)
            if self.new_positionmc in self.position_spaces:
                self.position_0 = (x,y+1)
                self.position_spaces.append(self.position_0)
            if self.new_positionmc in self.position_wall:
                #self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.objects.append("Pipe")
                self.position_pipe = (-15,-15)
                self.position_0 = (x,y+1)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_needle:
                self.objects.append("Needle")
                self.position_needle = (-15,-15)
                self.position_0 = (x,y+1)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_ether:
                self.objects.append("Ether")
                self.position_ether = (-15,-15)
                self.position_0 = (x,y+1)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_guardian:
                self.position_0 = (x,y+1)
                self.end = True
            else:
                print("Position in move Key Selected", self.new_positionmc)
        
        if key == keys.RIGHT:
            print("Position in RIGHT time", self.position_0)
            self.new_positionmc = (x+1,y)
            if self.new_positionmc in self.position_spaces:
                self.position_0 = (x+1,y)
                self.position_spaces.append(self.position_0)
            if self.new_positionmc in self.position_wall:
                #self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.objects.append("Pipe")
                self.position_pipe = (-15,-15)
                self.position_0 = (x+1,y)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_needle:
                self.objects.append("Needle")
                self.position_needle = (-15,-15)
                self.position_0 = (x+1,y)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_ether:
                self.objects.append("Ether")
                self.position_ether = (-15,-15)
                self.position_0 = (x+1,y)
                self.position_spaces.append(self.position_0)
                print(objects)
            if (self.new_positionmc in self.position_guardian and len(self.objects) == 3):
                self.position_0 = (x+1,y)
                self.end = True
            else:
                print("Position in move Key Selected", self.new_positionmc)
        
        if key == keys.LEFT:
            print("Position in LEFT time", self.position_0)
            self.new_positionmc = (x-1,y)
            if self.new_positionmc in self.position_spaces:
                self.position_0 = (x-1,y)
                self.position_spaces.append(self.position_0)
            if self.new_positionmc in self.position_wall:
                #self.new_positionmc = (x,y)
                print("Dans le Mur")
            if self.new_positionmc in self.position_pipe:
                self.objects.append("Pipe")
                self.position_pipe = (-15,-15)
                self.position_0 = (x-1,y)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_needle:
                self.objects.append("Needle")
                self.position_needle = (-15,-15)
                self.position_0 = (x-1,y)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_ether:
                self.objects.append("Ether")
                self.position_ether = (-15,-15)
                self.position_0 = (x-1,y)
                self.position_spaces.append(self.position_0)
                print(objects)
            if self.new_positionmc in self.position_guardian:
                self.position_0 = (x-1,y)
                self.end = True
            else:
                print("Position in move Key Selected", self.new_positionmc)
        return self.end
        
