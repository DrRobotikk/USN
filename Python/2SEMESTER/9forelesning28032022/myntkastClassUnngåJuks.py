#PRG1100-2022-private attributter

#For å sikre oss at annen kode ikke kan endre/ korrupere verdier på objektets
#data-attributter/ instansevariabler
#gjør vi attributtene private, dvs at det bare er objektets metoder som har
#direkte aksess/ tilgang til data-attributtene
#I Pyhton gjøres det ved å starte attributt-navnet med 2 "underscore", dvs __
import random

class Mynt:
    def __init__(self):
        self.__sideopp=input('Hvilken side på mynten er opp før første kast: ')

    def kast(self):
        if random.randint(0,1)==0:
            self.__sideopp='Kron'
        else:
            self.__sideopp='Mynt'

    def hent_sideopp(self):
        return self.__sideopp


def main():

    antall_kron=0
    antall_mynt=0
    
    min_mynt=Mynt()

    print('Før første kast, er denne siden opp: ',min_mynt.hent_sideopp())

    antall_kast=int(input('Hvor mange ganger skal mynten kastes: '))

    for antall_kast in range(1,antall_kast+1,1):
        min_mynt.kast()
        print('Resultatet av kast nr',antall_kast,'ble',min_mynt.hent_sideopp())

        #Her er juksedelen som prøver å endre verdien til kron uansett
        min_mynt.__sideopp='Kron'
        print('Resultatet av kast nr',antall_kast,'ble forsøkt manipulert men ble endret til',min_mynt.hent_sideopp())
        print()
        
        if min_mynt.hent_sideopp()=='Kron':
            antall_kron+=1
        else:
            antall_mynt+=1
            
    print('Resultatet ble',antall_kron,'antall kron og',antall_mynt,'antall mynt')

main()



















