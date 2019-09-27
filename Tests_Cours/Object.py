# -*-coding:Utf-8 -*
'''machaine = str()

while machaine.lower() != "q":
    print("taper Q pour quitter")
    machaine = input()

print("Merci!")'''

'''prenom = input("Prenom :")
nom = input("nom :")
age = input("age :")

print("Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} ans.".format(prenom, nom, age, nom.upper()))'''

'''machaine = "Bonjour"
i = 0

while i < len(machaine):
    print(machaine[i])
    i += 1'''

'''ma_liste = [1, 2, "WTF", 450]

print(ma_liste[1])
print(ma_liste[2])

ma_liste[2] = "WAZA"

print(ma_liste[2])

ma_liste.append("who'sssss BADDD")

print(ma_liste)

for elt in ma_liste:
    print(elt)'''


'''def decomposer(entier, divise_par):

    p_e = entier // divise_par
    reste = entier % divise_par

    print(p_e, reste)
    return p_e, reste

if __name__ == "__main__":
    decomposer(20,3)
'''
'''ma_chaine = "Hello world !!!"

modif = ma_chaine.split(" ")

modif2 = " ".join(modif)

print(modif)
print(modif2)'''

'''def modif_flottant(mon_chiffre):

    if type(mon_chiffre) is not float:
        raise TypeError(" Le chiffre n'est pas un flottant")

    num = str(mon_chiffre)[:5]
    print(num)

    good_num = num.replace(".",",")
    print("Votre num est :", good_num)

if __name__ == "__main__":
    modif_flottant(5.1545154515)'''

'''def afficher(*parametres, sep=' ', fin='\n'):

    parametres = list(parametres)
    
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    
    chaine = sep.join(parametres)
    chaine += fin

    print(chaine, end='')
if __name__ == "__main__":
    afficher('33', '34', 'tata')
'''
'''qtt_fruit_retirer = 7

fruit_stocke = [15, 3, 2, 21, 18]

mes_fruits = [nb_fruit-qtt_fruit_retirer for nb_fruit in fruit_stocke if nb_fruit>qtt_fruit_retirer]

print(mes_fruits)'''

'''inventaire = [("pommes", 22), ("melons", 4), ("poires", 18), ("fraises", 76), ("prunes", 51)]

inventaire_inverse = [(nbrfruit, fruit) for fruit, nbrfruit in inventaire]

inventaire = [(fruit, nbrfruit) for nbrfruit, fruit in sorted(inventaire_inverse, reverse=True)]
#inventaire.sort(key=lambda tup: (-tup[1], tup[0]))

print(inventaire)
'''
'''
#mon_dico = dict()

def fete():
    print("C'est la fete")

def oiseau():
    print("Fais comme l'oiseau")

mon_dico = {}

mon_dico["piaf"] = oiseau
mon_dico["cotillon"] = fete

#mon_dico['a', '1'] = "Tour Blanche"
#mon_dico['b', '1'] = "Cavalier Blanc"

if __name__ == "__main__":
    mon_dico["piaf"]()
    mon_dico["cotillon"]()
'''

'''
fruit = {"pomme":20, "raisin":30,"ananas":5, "poire":12}

tri_fruit = [(qtt, nomfruit) for nomfruit, qtt in fruit.items()]
inventaire = [(qtt, nomfruit) for qtt, nomfruit in sorted(tri_fruit)] 
print(inventaire)'''
