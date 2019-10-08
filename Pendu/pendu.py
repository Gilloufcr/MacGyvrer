# -*-coding:Utf-8 -*

from donnees import (MotDico, NbrChance, LstLettresIns, LstLettresUsed, NomJoueur, Score, MotTmp )
from fonctions import (Wscore, MasqueMot)
from random import choice

NomJoueur = input("Merci de Saisir votre Nom :")
print("Votre Nom est :", NomJoueur)

#Choix du mot parmi le dictionnaire
RandomWord = choice(list(MotDico.keys()))
MasqueMot(RandomWord)

LettreSaisie = ''
#Initialisation de la Partie
ContinuerJeux = True

#Partie
while ContinuerJeux == True:
   while MotTmp != RandomWord:
      LettreSaisie += input("\nMerci de saisir une lettre :")
      for IdLtr,LettreMot in enumerate(RandomWord):
         if LettreMot in LettreSaisie:
            MotTmp = LettreMot
            print(MotTmp, end='')
         else:
            print("*", end='')
            