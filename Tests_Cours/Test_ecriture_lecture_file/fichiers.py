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

'''with open('donnee', 'rb') as fichier:
    mon_pickler = pickle.Unpickler(fichier)
    score = mon_pickler.load()
    print(score)
'''

'''def set_var(nouvelle_valeur):
    try:
        print("La valleur de var est {0}".format(var))
    except NameError:
        print("La valeur de var n'est pas connue.....")
    var = nouvelle_valeur
    print("Apres l'affectation var vaut : {0}".format(var))

if __name__ == "__main__":
    set_var(10)
'''


'''def ajouter_liste(ma_liste, values):
    ma_liste.append(values)
    
    print(liste)

if __name__ == "__main__":
    liste = ['a', 'b', 'c']
    ajouter_liste(liste, '10')
'''

