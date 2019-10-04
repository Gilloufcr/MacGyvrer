# -*-coding:Utf-8 -*

import os
import pickle
from random import choice

#Fonction d'ecriture du fichier Score.
def Wscore(PNomJoueur,Pscore):
    #Verification de l'existence du fichier score sinon on le cree.
    os.chdir("C:/GitGT/MacGyvrer/Pendu/")
    with open('score', 'ab+') as Fscore:
        try:
            FscoreUnpickler = pickle.Unpickler(Fscore)
            Fcontenu = FscoreUnpickler.load()
        except:
            Fcontenu = {"Le Joueur": "Son Score"}
            FscorePickler = pickle.Pickler(Fscore)
            FscorePickler.dump(Fcontenu)

    #Lecture du Fichier avant Ecriture
    with open('score', 'rb') as Fscore:
        FscoreUnpickler = pickle.Unpickler(Fscore)
        Fcontenu = FscoreUnpickler.load()
    
    print("Le Score du Joueur :", PNomJoueur, "est :", Pscore)

    #Ecriture du Score
    with open('score', 'wb') as Fscore:
        FscoreUnpickler = pickle.Unpickler(Fscore)
        Fcontenu.update({PNomJoueur: Pscore})
        FscorePickler = pickle.Pickler(Fscore)
        FscorePickler.dump(Fcontenu)
        
    #Lecture du Fichier Apres Ecriture       
    with open('score', 'rb') as Fscore:
        FscoreUnpickler = pickle.Unpickler(Fscore)
        Fcontenu = FscoreUnpickler.load()
        print(Fcontenu)


#Fonction du choix du mot
def ChoixMot(Pdico):
    RandomWord = choice(list(Pdico.keys()))
    print(RandomWord)
           