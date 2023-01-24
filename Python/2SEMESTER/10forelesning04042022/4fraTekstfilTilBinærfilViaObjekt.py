#PRG1100-2022-fra tekstfil til binærfil via objekt

#Instansiere objektet med innlesing av data fra fil
#Serialiserer og lagrer objektet

import pickle

class Ansatt:
    def __init__(self,fornavn,etternav,epost):
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost

    def __str__(self):
        return 'Objektets attributter er: ' + self.__fornavn + '\n' + self.__etternavn + '\n' + self.__epost + '\n'

ansatt_txt_fil=open('laerer.txt','r',encoding='utf-8')
ansatt_dat_fil=open('laerer.dat','wb')

fornavn=ansatt_txt_fil.readline()

while fornavn !='':
    fornavn=fornavn.rstrip('\n')
    etternavn=ansatt_txt_fil.readline().rstrip('\n')
    epost=ansatt_txt_fil.readline().rstrip('\n')

    #Legger variablene i attributtene til objektet
    ny_ansatt=Ansatt(fornavn,etternavn,epost)

    print(ny_ansatt)

    #Serialisering og skriving av objektet til fil
    pickle.dump(ny_ansatt,ansatt_dat_fil)

    
    fornavn=ansatt_txt_fil.readline()

ansatt_txt_fil.close()
ansatt_dat_fil.close()
