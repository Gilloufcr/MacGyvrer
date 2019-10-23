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

'''class Duree:
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
'''


'''class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
            self.prenom, self.age, self.moyenne)
    
        
        
if __name__ == "__main__":
    
    etudiants = [
        Etudiant("Clément", 14, 16),
        Etudiant("Charles", 12, 15),
        Etudiant("Oriane", 14, 16),
        Etudiant("Thomas", 11, 12),
        Etudiant("Damien", 12, 15),
    ]

print(sorted(etudiants, key=lambda etudiants:etudiants.moyenne, reverse=True))
'''

'''class Personne:
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.age = 56
    def __str__(self):
        return "{0} {1}".format(self.nom, self.prenom)
    
class AgentSpecial(Personne):
    def __init__(self, nom, matricule, prenom):
        Personne.__init__(self, nom, prenom)
        self.matricule = matricule
    def __str__(self):
        return "Agent {0}, prenom {1} matricule {2}, age {3}".format(self.nom, self.prenom, self.matricule, self.age)
    
if __name__ == "__main__":
    agent = AgentSpecial("Bond", 1235879, "James")
    print(agent)
'''

'''class Revstr(str):
    
    def __init__(self, chaine):
        self.chaine = chaine
        
    def __iter__(self):
        ItRevstr = iter(chaine, reverse=True)
        
        
if __name__ == "__main__":
    Revstr("Hello")
    print(Revstr)
'''