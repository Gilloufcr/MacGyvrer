# -*-coding:Utf-8 -*

#Test de Boucle While table de multiplication

tbl = input("Merci de saisir la table que vous souhaitez multiplier :")

i = 0

while i <= 10:
    result = int(tbl) * int(i)
    print(result)
    i += 1