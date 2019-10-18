# -*-coding:Utf-8 -*



class Personne:
    

    def __init__(self, nom, prenom):
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = nom
        self.prenom = prenom
        self.age = 35
        self._ville = "Arles"
    
    def _get_ville(self):
        """On accede en lecture a la ville"""
        print("ville actuelle")
        return self._ville
    def _set_ville(self, new_ville):
        """On Accede en modification de la ville"""
        self._ville = new_ville
        
    ville = property(_get_ville,_set_ville)

if __name__ == "__main__":
    Jean = Personne("Dupont", "Bernard")
    print(Jean.nom, Jean.prenom)
    print(Jean.ville)
    Jean.ville = "Berlin"
    print(Jean.ville)
    
'''class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets = 0
    
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets += 1
    
    def combien(cls):
        """Methode de classe affichant combien d'objets ont été créés"""
        print("Voici le nombre d'obejet créé : {}.".format(cls.objets))
    combien = classmethod(combien)

if __name__ == "__main__":
     print(Compteur.combien())
     a = Compteur()
     print(Compteur.combien())
     b = Compteur()
     print(Compteur.combien())

'''
'''
class TableauNoir:
    """ Classe définissant une surface de tableau pour ecrire"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        TableauNoir.surface = ""

    def ecrire(self, message):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""
        
        if self.surface != "":
            self.surface += "\n"
        self.surface += message
        
    def lire(self):
        """ Lecture de la surface du tableau"""
        print(self.surface)
    
    def effacer(self):
        """On efface le Tableau"""
        self.surface = ""



if __name__ == "__main__":

    tab = TableauNoir()
    tab.ecrire("Bonjour Allll!!")
    tab.ecrire("Deuxieme ligne")
    tab.lire
    tab.effacer
    tab.lire
    help(TableauNoir)'''


