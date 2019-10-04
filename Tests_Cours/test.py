# -*-coding:Utf-8 -*
import pickle

with open('score', 'ab+') as Fscore:
    try:
        FscoreUnpickler = pickle.Unpickler(Fscore)
        Fcontenu = FscoreUnpickler.load()
    except:
        Fcontenu = {"Le Joueur2": "Son Score"}
        FscorePickler = pickle.Pickler(Fscore)
        FscorePickler.dump(Fcontenu)

with open('score', 'rb') as Fscore:
    FscoreUnpickler = pickle.Unpickler(Fscore)
    Fcontenu = FscoreUnpickler.load()
    print(Fcontenu)