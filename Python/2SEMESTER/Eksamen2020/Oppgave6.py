#Oppgave 5:

import pickle

class Bil:
    def __init__(self,regnr,merke,modell,startdato,posisjon):
        self.__regnr=regnr
        self.__merke=merke
        self.__modell=modell
        self.__startdato=startdato
        self.__posisjon=posisjon


    def set_posisjon(self,ny_posisjon):
        self.__posisjon=ny_posisjon

    def get_posisjon(self):
        return self.__posisjon




#Oppgave 6:
#Basert på klassediagrammet i oppgave 5, lag et program som leser
#opplysningene om en bil fra den sekvensielle tekstfila Bil,
#inn i et objekt av klasse Bil, serialiserer og skriver/lagrer objektet i en 
#binærfil. Dette skal gjøres for alle bilene i den sekvensielle tekstfila. 


bilfil=open('bil.txt','r',encoding='utf-8')
output_fil=open('bil.dat','wb')

regnr=bilfil.readline()

while regnr!='':
    regnr=regnr.rstrip('\n')
    merke=bilfil.readline().rstrip('\n')
    modell=bilfil.readline().rstrip('\n')
    startdato=bilfil.readline().rstrip('\n')
    posisjon=bilfil.readline().rstrip('\n')

    ny_bil=Bil(regnr,merke,modell,startdato,posisjon)
    pickle.dump(ny_bil,output_fil)
    regnr=bilfil.readline()
output_fil.close()
bilfil.close()

fortsette=True

bilfil=open('bil.dat','rb')

while fortsette==True:
    try:
        bilen=pickle.load(bilfil)

        print('posisjon: ',bilen.get_posisjon())

    except EOFError:
        fortsette=False
bilfil.close()














    

