# -*-coding:Utf-8 -*

from donnees import (MotDico, NbrChance, LstLettresIns, LstLettresUsed, NomJoueur, Score, MotTmp )
from fonctions import (Wscore, MasqueMot, VerifLettreSaisie)
from random import choice

NomJoueur = input("Merci de Saisir votre Nom :")
print("Votre Nom est :", NomJoueur)

#Choix du mot parmi le dictionnaire
RandomWord = choice(list(MotDico.keys()))
MotTmp = MasqueMot(RandomWord)
LenRandomword = len(RandomWord)

print("Le mot à trouver est de :", LenRandomword, "lettres")

LettreSaisie = ''
#Initialisation de la Partie
ContinuerJeux = True
Perdu = False

#Partie
while ContinuerJeux == True:
   while MotTmp.decode("utf-8") != RandomWord and Perdu == False:
      if NbrChance > 0:   
         LettreSaisie = input("\nMerci de saisir une lettre :")
         LettreSaisieOK = VerifLettreSaisie(LettreSaisie)
         if LettreSaisieOK in RandomWord:
            for IdLtr,LettreMot in enumerate(RandomWord):
               if LettreMot == LettreSaisieOK:
                  MotTmp[IdLtr] = ord(LettreSaisieOK)
                  print(MotTmp.decode("utf-8"))
         else:
            print("Ce n'est pas la bonne lettre !!")
            NbrChance -= 1
            print("Il vous reste ", NbrChance, "chances!!")
            print(MotTmp.decode("utf-8"))
      else:
         print("Vous avez perdu!!")
         Perdu = True
   if Perdu == False:   
      print("Vous avez Gagné!!")
      Wscore(NomJoueur,NbrChance)
   ContinuerJeux = False

   
   
      