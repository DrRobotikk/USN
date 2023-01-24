#OPPGAVE 5:
#Skriv koden for definisjon av klassen Bil hvor metoden __init__()
#instansierer et objekt med innlesing av dataattributter. 
#Skriv koden for metoden set_posisjon, basert på ny posisjon
#som inndata i variabel fra brukeren. 
#Skriv koden for metoden get_posisjon, hente ut/vise bilens posisjon.

import pickle

class Bil:
    def __init__(self,regnr,merke,modell,startdato,posisjon):
        self.__regnr=regnr
        self.__merke=merke
        self.__modell=modell
        self.__startdato=startdato
        self.__posisjon=posisjon


    def set_posisjon(self,posisjon):
        self.__posisjon=posisjon

    def get_posisjon(self):
        return self.__posisjon

regnr=input('Oppgi regnr: ')
merke=input('Oppgi merke: ')
modell=input('Oppgi modell: ')
startdato=input('Oppgi startdato: ')
posisjon=input('Oppgi posisjon: ')

bil1=Bil(regnr,merke,modell,startdato,posisjon)

print(bil1.get_posisjon())
posisjon=input('Oppgi ny posisjon: ')
bil1.set_posisjon(posisjon)
print(bil1.get_posisjon())
