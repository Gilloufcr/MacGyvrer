# -*-coding:Utf-8 -*
import pickle

'''lecture_fichier = open("fichier.txt", "r")
#contenu = lecture_fichier.write("Premier Test d'ecriture")
contenu = lecture_fichier.read()
lecture_fichier.close()
print(contenu)
'''

'''score = {"toto":10, "titi":9, "tutu": 15}

with open('donnee', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)
'''

with open('donnee', 'rb') as fichier:
    mon_pickler = pickle.Unpickler(fichier)
    print(fichier)
