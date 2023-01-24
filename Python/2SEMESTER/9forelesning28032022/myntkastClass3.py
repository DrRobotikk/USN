#PRG1100-2022-instansiering input

import random

class Mynt:
    def __init__(self):
        self.sideopp=input('Hvilken side av mynten er opp før første kast: ')

    def kast(self):
        if random.randint(0,1)==0:
            self.sideopp='Kron'
        else:
            self.sideopp='Mynt'

    def hent_sideopp(self):
        return self.sideopp


def main():

    antall_kron=0
    antall_mynt=0
    
    min_mynt=Mynt()

    print('Før første kast, er denne siden opp: ',min_mynt.hent_sideopp())

    antall_kast=int(input('Hvor mange ganger skal mynten kastes: '))

    for antall_kast in range(1,antall_kast+1,1):
        min_mynt.kast()
        print('Resultatet av kast nr',antall_kast,'ble',min_mynt.hent_sideopp())

        if min_mynt.hent_sideopp()=='Kron':
            antall_kron+=1
        else:
            antall_mynt+=1
            
    print('Resultatet ble',antall_kron,'antall kron og',antall_mynt,'antall mynt')

main()


















