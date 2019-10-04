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
            Fcontenu = {"Le Joueur": "Son Score"}
            FscorePickler = pickle.Pickler(Fscore)
            FscorePickler.dump(Fcontenu)

        #Verification si le Joueur Existe
        with open('score', 'rb+') as Fscore:
            FscoreUnpickler = pickle.Unpickler(Fscore)
            Fcontenu = FscoreUnpickler.load()
            print("Contenu du Fichier actuellement :", Fcontenu)
            print(PNomJoueur)
            print(Pscore)
            if not PNomJoueur in Fcontenu:
                print("Bonjour Nouveau Joueur !")
                Fcontenu = {PNomJoueur: Pscore}
                with open('score', 'ab') as Fscore:
                    FscorePickler = pickle.Pickler(Fscore)
                    FscorePickler.dump(Fcontenu)

    #Lecture du Fichier        
    with open('score', 'rb') as Fscore:
        FscoreUnpickler = pickle.Unpickler(Fscore)
        Fcontenu = FscoreUnpickler.load()
        print(Fcontenu)
            