#program for å returnere verdi fra delprogram

#delprogram som fikser matematisk utregning av 2 aldere

#setter inn variablene i parantes (kan hete noe annet også, som f.eks.verdi 1 og 2)
def summen(alder1,alder2):
    
    resultat=alder1+alder2
    
    #tar vare på resultatet
    return resultat

#delprogram som ber om input og viser resultatet fra def summen
def main():

    ny='ja'
    while ny=='ja':
        
        #oppgi din alder
        alder1=int(input('Oppgi din alder: '))

        #oppgi vennens alder
        alder2=int(input('Oppgi din venns alder: '))

        #kobler sammen verdi1 og 2 til alder 1 og 2
        #totalt=summen(alder1,alder2)

        #skriver ut totalt med verdier fra def summen
        print('Sammen er dere',total,'gamle')
        ny=input('ny? ')

main()
