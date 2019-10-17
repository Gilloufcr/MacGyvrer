# -*-coding:Utf-8 -*


'''
class Personne:
    

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.age = 35
        self.ville = "Arles"

if __name__ == "__main__":
    Jean = Personne("Dupont", "Bernard")
    print(Jean.nom, Jean.prenom)
    Jean.ville = "Berlin"
    print(Jean.ville)'''

'''class Compteur:

    objets = 0
    def __init__(self):
        Compteur.objets += 1

if __name__ == "__main__":
     a = Compteur()
     print(Compteur.objets)
     b = Compteur()
     print(Compteur.objets)'''

class TableauNoir:
    """ Classe définissant une surface de tableau pour ecrire"""

    def __init__(self):
        TableauNoir.surface = ""
        
    def ecrire(self, message):

        if self.surface != "":
            self.surface += "\n"
        self.surface += message
        
if __name__ == "__main__":
    
     tab = TableauNoir()
     tab.ecrire("Bonjour Allll!!")
     tab.ecrire("Deuxieme ligne")
     print(tab.surface)