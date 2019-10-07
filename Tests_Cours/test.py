# -*-coding:Utf-8 -*
'''import pickle

with open('score', 'ab+') as Fscore:
    try:
        FscoreUnpickler = pickle.Unpickler(Fscore)
        Fcontenu = FscoreUnpickler.load()
    except:
        Fcontenu = {"Le Joueur2": "Son Score"}
        FscorePickler = pickle.Pickler(Fscore)
        FscorePickler.dump(Fcontenu)

with open('score', 'rb') as Fscore:
    FscoreUnpickler = pickle.Unpickler(Fscore)
    Fcontenu = FscoreUnpickler.load()
    print(Fcontenu)'''

RandomWord = "SALUT"
LettreSaisieUpp =''
MotTmp = ''


for IdLtr,LettreMot in enumerate(RandomWord):
    print(IdLtr, LettreMot)

'''while MotTmp != RandomWordUpp:
    LettreSaisieUpp += input("Merci de saisir une lettre :")
    MotTmp = ''
    for LettreATrouver in RandomWordUpp:
        if LettreATrouver in LettreSaisieUpp:
            MotTmp += LettreATrouver
        else:
            MotTmp += "*"
        print(MotTmp)'''





'''Mot_tiré = "abcdef"
Mot_caché = ""
m = ""
 
while (Mot_caché != Mot_tiré):
    m += input("lettre:")
 
    Mot_caché = ""
    for char in Mot_tiré:
        if (char in m):
            Mot_caché += char
        else:
            Mot_caché += '-'
 
    print(Mot_caché)'''