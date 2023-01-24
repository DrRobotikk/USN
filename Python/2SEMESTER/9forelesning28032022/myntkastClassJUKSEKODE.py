#PRG1100-2022-juksekode

#Introduksjon til private/ skjulte attributter
#Vi bør sikre oss at det bare er metodene til objektet som kan endre/ aksessere
#attributtene/ instansevariablene
#Slik det er nå kan kode i main endre verdier på attributter til objektet
#dvs vi kan jukse i spillet
import random

#Mynt-klassen simulerer en mynt og hva en kan gjøre med den
class Mynt:
    #__init__metoden initierer objektet/ forekomsten/ instansen
    #og tilordner sideopp-atributtet (self.sideopp) startverdi via en
    #input i __init__
    #dvs setter en startverdi som ikke skal telles med
    
    def __init__(self):
        #Oppgi "myntside" opp før første kast
        self.sideopp=input('Hvilken side på mynten er opp før første kast: ')

    #Kast metoden simulerer ett kast med mynten
    #og gir sideopp-attributtet ny verdi
    def kast(self):
        if random.randint(0,1)==0:
            self.sideopp='Kron'
        else:
            self.sideopp='Mynt'

    #hent_sideopp metoden returnerer til enhver til
    #verdien/ ("siste verdi") på mynten, dvs sideopp-attributtet
    def hent_sideopp(self):
        return self.sideopp


def main():

    antall_kron=0
    antall_mynt=0

    #Oppretter et mynt-objekt, en forekomst/ instanse
    min_mynt=Mynt()

    print('Før første kast, er denne siden opp: ',min_mynt.hent_sideopp())

    antall_kast=int(input('Hvor mange ganger skal mynten kastes: '))

    for antall_kast in range(1,antall_kast+1,1):
        #Mynten kastes
        min_mynt.kast()

        #Resultatet av kastet skrives ut
        print('Resultatet av kast nr',antall_kast,'ble',min_mynt.hent_sideopp())

        #Her kommer den nye "jukse-koden"
        #Uansett hva som blir resultatet av kast-metoden, overstyrer vi
        #resultatet til å bli f.eks. Kron
        min_mynt.sideopp='Kron'
        print('Resultatet av kast nr',antall_kast,'ble manipulert til',min_mynt.sideopp)
        print()

        #Opptelling av kast
        if min_mynt.hent_sideopp()=='Kron':
            antall_kron+=1
        else:
            antall_mynt+=1
            
    print('Resultatet ble',antall_kron,'antall kron og',antall_mynt,'antall mynt')

main()



















