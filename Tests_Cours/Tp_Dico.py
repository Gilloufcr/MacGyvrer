# -*-coding:Utf-8 -*


class DicoOrdo():
    """Creation d'un dictionnaire pouvant etre manipulé, ordonné..."""
    
    def __init__(self, copydico={}, **itemsadd):
        """ Si on ne met pas de données dans le constructeur celui-ci cree un dico vide"""
        self.dico = {}
        for item in copydico:
            key = item
            value = copydico[item]
            self.dico[key] = value
        for item in itemsadd:
            key = item
            value = itemsadd[item]
            self.dico[key] = value
        print(self.dico)
        self.sort = sorted(self.dico)
        
    def __setitem__(self, keys, values):
        """Methode permetant d'ajouter des élément dans le Dico"""
        self.dico[keys] = values
        print(self.dico)

    def __len__(self):
        lendico = len(self.dico)
        print(lendico)
        return lendico
        
        
    def __getitem__(self, key):
        for value in self.dico:
            if value == value:
                self.new_keys = self.dico[key]
                print(self.new_keys)
                return self.new_keys 
                
    def __sort__(self):
        self.dico = sorted()
        print(self.dico)
    
 
if __name__ == "__main__":
    dicotest = DicoOrdo()
    dicotest["pomme"] = 50
    dicotest["poire"] = 45
    dicotest["peche"] = 40
    legume = DicoOrdo(tomate = 10)
    dicotest1 = {"toto": 20}
    dicotest2 = DicoOrdo(dicotest1)
    print(dicotest2)
    len(dicotest)
    dicotest['pomme']
