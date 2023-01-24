#Oppgave 4:
#Skriv koden for konstruktøren hvor metoden __init__
#(mobilnr,fornavn,etternavn,epost) instansierer 
#et objekt med innlesing av dataattributter i et hovedprogram.

#Skriv koden for metoden set_epost, basert på ny epost som inndata
#i variabel fra brukeren.

#Skriv koden for metoden get_epost, hente ut/vise kundens epost. 

Class Kunde:
    def __init__(self,mobilnr,fornavn,etternavn,epost):
        #initialiserer variablene
        self.__mobilnr=mobilnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost

    def set_epost(self,epost):
        self.__epost=epost

    def get_epost(self):
        return self.__epost

def main():
    kunde1=Kunde('11111111','Roman','Kollar','roman@kollar.no')
    kunde2=Kunde('22222222','Mira','Bergli','mira@bergli.com')

    #Eksempel på å endre en epostadresse:
    kunde1.set_epost('romanko7@hotmail.com')

#Oppgave 5:
#Basert på klassediagrammet i oppgave 5, lag et program som leser
#og de-serialierer objekter fra binærfila Kunde.dat og skriver ut
#mobilnr, etternavn og e-post for alle kundene. Dette skal gjøres for 
#alle kundene i binærfila.
    
import pickle

def les_fil():
    fortsette=True

    kundefil=open('kunde.dat','rb')

    while fortsette==True:
        try:
            kunde=pickle.load(kundefil)

            print('Mobilnr: ',kunde.get_mobilnr())
            print('Etternavn: ',kunde.get_etternavn())
            print('Epost: ',kunde.get_epost())

        except EOFError:#her kan vi droppe EOFError og da vil excepten plukke opp alle feil
            fortsette=False
    kundefil.close()

les_fil()
main()


