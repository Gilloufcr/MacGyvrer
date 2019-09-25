import math
import random

mise = 0
nummise = 0
numroul = 0
gain = 0

nummise = input ("Merci de Saisir un Numéro entre 0 et 49: ")
mise = input("Merci d'indiquer votre mise $ : ")
numroul = random.randrange(0,49)

#while numroul < 0:

nummise = int(nummise)
mise = int(mise)

if nummise == numroul:
    gain = int(mise) * 3
    print("Le numéro de la Banque est :", numroul)
    print("Bravo! vous avez gagné ", gain + mise, "$ !!")
elif (nummise != numroul and nummise % 2 == 0 and numroul %2 == 0) or (nummise != numroul and numroul % 2 != 0 and nummise % 2 != 0):
    gain = int(mise) * 0.5
    print("Le numéro de la Banque est :", numroul)
    print("Dommage ce n'est pas le bon numéro :( mais c'est la bonne couleur ! Vous gagnez ", math.ceil(gain) + mise, "$ !!")
elif nummise != numroul and int(numroul) % 2 != 0:
    print("Le numéro de la Banque est :", numroul)
    print("Désolé vous avez Perdu :( :(")
