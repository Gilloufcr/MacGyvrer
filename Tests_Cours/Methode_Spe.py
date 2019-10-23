# -*-coding:Utf-8 -*

'''
class Personne:
    
    def __init__(self, nom, prenom):
        """Notre Cobstructeur de Classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        
    def __repr__(self):
        """Qaund on entre notre objet dans l'interpreteur"""
        return "Personne : nom({}), prénom({}), age({})".format(self.nom, self.prenom, self.age)
    
    

if __name__ == "__main__":
    moi = Personne("Jean", "Dupont")
    print(moi)
    repr(moi)
'''    

'''class Personne:

    def __init__(self, nom, prenom):
        """Notre Cobstructeur de Classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33

    def __str__(self):
        """Qaund on entre notre objet dans l'interpreteur"""
        return "{} {}, {} ans".format(self.nom, self.prenom, self.age)

    def __getattr__(self, name):
        return "Pas d'attribu {} ici !".format(name)


if __name__ == "__main__":
    moi = Personne("Jean", "Dupont")
    print(moi)
'''
'''
class ZDict:
    """Classe contenant un dictionnaire, enfin presque..."""
    def __init__(self):
        self._dictionnaire = {}
        
    def __getitem__(self, index):
        """On accede au dictionnaire grace a cette fonction speciale"""
        return self._dictionnaire[index]
    
    def __setitem__(self, index, valeur):
        """ On Modifie la valeur grace a cette methode spéciale"""
        self._dictionnaire[index] = valeur
            
if __name__ =="__main__":
    dico = ZDict()
    dico = {"1": 21}
    dico.__getitem__
'''

class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min  # Nombre de minutes
        self.sec = sec  # Nombre de secondes

    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __iadd__(self, objet_a_ajouter):
        """ Travil directement sur l'objet"""
        self.sec += objet_a_ajouter
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        return self


if __name__ == "__main__":
    d1 = Duree(8,5)
    print(d1)
    d1 += 128
    print(d1)
