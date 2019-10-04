# -*-coding:Utf-8 -*

from donnees import (MotDico, NbrChance, LstLettresIns, LstLettresUsed, NomJoueur, Score, MotTmp )
from fonctions import Wscore
from random import choice

NomJoueur = input("Merci de Saisir votre Nom :")
print("Votre Nom est :", NomJoueur)

#Choix du mot parmi le dictionnaire
RandomWord = choice(list(MotDico.keys()))
RandomWordUpp = RandomWord.upper()

LettreSaisieUpp = ''.upper()
#Initialisation de la Partie
ContinuerJeux = True

#Partie
while ContinuerJeux == True:
   if NbrChance > 0:
      while MotTmp != RandomWordUpp:
         LettreSaisieUpp += input("Merci de saisir une lettre :")
         MotTmp = ''
         for LettreATrouver in RandomWordUpp:
            if LettreATrouver in LettreSaisieUpp:
               MotTmp += LettreATrouver
            else:
               MotTmp += "*"
         print(MotTmp)
   else:
      print("Vous n'avez plus d'essais!")
      ContinuerJeux = False