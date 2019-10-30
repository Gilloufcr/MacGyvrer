# -*-coding:Utf-8 -*

from clevel import Level

class Caracter():

    def __init__(self, moove):
        self.moove = moove
        self.position_0 = Level.find_mac()
