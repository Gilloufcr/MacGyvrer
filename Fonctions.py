# -*-coding:Utf-8 -*
"""module multipli contenant la fonction table"""

def table_multi(nb, max):
 
    i = 0
    while i < max:
        result = int(nb) * int(i)
        print(result)
        i += 1

#Test de la fonction

if __name__ == "__main__":
    table_multi(5,10)