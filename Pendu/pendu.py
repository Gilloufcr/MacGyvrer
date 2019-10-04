# -*-coding:Utf-8 -*

from donnees import (MotDico, NbrChance, LstLettresIns, LstLettresUsed, NomJoueur, Score)
from fonctions import Wscore


NomJoueur = input("Merci de Saisir votre Nom :")
print("Votre Nom est :", NomJoueur)

Wscore(NomJoueur,Score)
