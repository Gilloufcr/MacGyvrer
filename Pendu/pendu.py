# -*-coding:Utf-8 -*

from donnees import (MotDico, NbrChance, LstLettresIns, LstLettresUsed, NomJoueur, Score)
from fonctions import (Wscore, ChoixMot)


NomJoueur = input("Merci de Saisir votre Nom :")
print("Votre Nom est :", NomJoueur)

LettreSaisie = input("Merci de Saisir une Lettre")

#Wscore(NomJoueur,Score)

ChoixMot(MotDico)