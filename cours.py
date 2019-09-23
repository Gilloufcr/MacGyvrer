# -*-coding:Utf-8 -*


#Tests de conditions
#mon_age = 5
#if mon_age > 20:
#   print("Tu as bien grandi!")
#elif mon_age >= 16:
#   print("et tu est meme presque majeur")
#   if mon_age == 17:
#       print("Well done!!")
#else:
#   print("Okayyyy")

#Test de predicat
#age = 20
#majeur = False
#if age >= 18:
#   majeur == True

#Test and or not

#age = 19

#if age < 18 or age > 21:
#   print("age ok")
#else:
#    print("not at all")

#Test de is not

#majeur = False
#if majeur is not True:
#    print("pas bon")
#else:
#    print("okkkk")





# Programme année Bissextile

annee = input("Merci de saisir une année : ")
result4 = int(annee) / 4
result100 = int(annee) / 100
result400 = int(annee) / 400
if result4.is_integer() and result100.is_integer() and result400.is_integer():
    print(result4)
    print(result100)
    print(result400)
    print("L\' Annee est bien Bissextile")    
else:
    print(result4)
    print(result100)
    print(result400)
    print("L\' Annee n\'est pas Bissextile")
