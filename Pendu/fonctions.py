# -*-coding:Utf-8 -*

import os
import pickle


#Fonction d'ecriture du fichier Score.
def Wscore(PNomJoueur,Pscore):
    #Verification de l'existence du fichier score sinon on le cree.
    os.chdir("C:/GitGT/MacGyvrer/Pendu/")
    with open('score', 'ab+') as Fscore:
        try:
            FscoreUnpickler = pickle.Unpickler(Fscore)
            Fcontenu = FscoreUnpickler.load()
        except:
            Fcontenu = {PNomJoueur: 0}
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


#Fonction Masque du mot
def MasqueMot(PrandomWord, IdLtr=0, Ltr=''):
    for IdLtr,Ltr in enumerate(PrandomWord):
        MotMasque = "*"
        print(MotMasque, end='')