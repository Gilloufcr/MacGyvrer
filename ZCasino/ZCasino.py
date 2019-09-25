# -*-coding:Utf-8 -*

from math import ceil
from random import randrange

argent = 1000
continuer_partie = True

print("Vous vous installez à la table de roulette avec", argent, "$.")

while continuer_partie == True:
    nummise = -1
    #Choix du numéro
    while nummise < 0 or nummise > 49:
        nummise = input("Merci de Saisir un Numéro entre 0 et 49: ")
        try:
            nummise = int(nummise)
        except ValueError:
            print("Le numéro Saisi n'est pas correct")
            nummise = -1
            continue

    #Choix de la mise
    
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Merci d'indiquer votre mise $ : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Le numéro Saisi n'est pas correct")
            mise = -1
            continue
        if mise > argent:
            print("Vous avez misé plus que votre argent..")

    # La mise est selectionnée et le numéro choisi, on lance la roulette.

    numroul = randrange(50)

    if nummise == numroul:
        gain = int(mise) * 3
        print("Le numéro de la Banque est :", numroul)
        print("Bravo! vous avez gagné ", gain + mise, "$ !!")
        argent = argent + gain + mise
        print("votre argent est de ", argent, "$!")

    elif (nummise != numroul and nummise % 2 == 0 and numroul %2 == 0) or (nummise != numroul and numroul % 2 != 0 and nummise % 2 != 0):
        gain = int(mise) * 0.5
        print("Le numéro de la Banque est :", numroul)
        print("Dommage ce n'est pas le bon numéro :( mais c'est la bonne couleur ! Vous gagnez ", ceil(gain) + mise, "$ !!")
        argent = argent + gain + mise
        print("votre argent est de ", argent, "$!")

    else:
        print("Le numéro de la Banque est :", numroul)
        print("Désolé vous avez Perdu :( :(")
        argent = argent - mise
        print("votre argent est de ", argent, "$!")
    
    if argent <= 0:
        print(" Désolé vous n'avez plus d'argent")
        continuer_partie = False
    else:
        quitter = input("Souhaitez vous quitter le jeux ? o/n :")
        if quitter == "o" or quitter == "O":
            print("Vous avez Gagné ", argent,"$ !!")
            continuer_partie = False

    
