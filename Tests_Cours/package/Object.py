
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

def modif_flottant(mon_chiffre):

    num = str(mon_chiffre)[:5]
    print(num)

    good_num = num.replace(".",",")

    print("Votre num est :", good_num)

if __name__ == "__main__":
    modif_flottant("5.1545154515")
