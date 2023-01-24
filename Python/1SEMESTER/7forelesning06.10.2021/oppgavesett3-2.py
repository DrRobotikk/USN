

liste=[]
print('Lista til nå er ',liste)
print()
start=True

while start:
    stnr=int(input('Skriv inn studentnummer her: '))
    stnv=input('Skriv inn navn her: ')
    stsd=input('Skriv inn studie her: ')
    liste+=[stnr,stnv,stsd]
    print(liste)
    fortsett=input('Ønsker du å legge til flere studenter? ')
    if fortsett=="ja":
        start=True
    if fortsett!="ja" or fortsett=="nei":
        start=False
