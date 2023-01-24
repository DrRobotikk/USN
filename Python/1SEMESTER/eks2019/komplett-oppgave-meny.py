def registrer_ny_kunde():
    ny_kunde='ja'
    while ny_kunde=='ja':
        funnet=False
        kunde=input('Skriv inn kundens mobilnummer: ')
        kundefil=open('kunde.txt','r')
        tlf=kundefil.readline()
        while tlf!='':
            tlf=tlf.rstrip('\n')
            fornavn=kundefil.readline().rstrip('\n')
            etternavn=kundefil.readline().rstrip('\n')
            kort=kundefil.readline().rstrip('\n')
            if tlf==kunde:
                print('Kunden finnes fra før')
                funnet=True
            tlf=kundefil.readline()
        kundefil.close()
        
        if funnet==False:
            kundefil=open('kunde.txt','a')
            fornavn=input('Skriv inn fornavn ')
            etternavn=input('Skriv inn etternavn ')
            kort=input('Skriv inn kortnummer ')
            kundefil.write(kunde+'\n')
            kundefil.write(fornavn+'\n')
            kundefil.write(etternavn+'\n')
            kundefil.write(kort+'\n')
            print('Lista oppdatert')
            print()
        ny_kunde=input('flere kunder? ')
        kundefil.close()

def registrer_ny_hund():
    ny_hund='ja'
    while ny_hund=='ja':
        funnet_kunde=False
        funnet_hund=False
        hund=input('Skriv inn hundens ID: ')
        hundfil=open('hund.txt','r')
        hid=hundfil.readline()
        while hid!='':
            hid=hid.rstrip('\n')
            navn=(hundfil.readline().rstrip('\n'))
            rase=(hundfil.readline().rstrip('\n'))
            ktlf=(hundfil.readline().rstrip('\n'))
            dato=(hundfil.readline().rstrip('\n'))
            if hid==hund:
                print('Hunden finnes fra før')
                funnet_hund=True
            hid=hundfil.readline()
        hundfil.close()
        
        #har vi ikke funnet hunden i hund.txt sjekker vi om eieren finnes 
        if funnet_hund==False:
            kunde=input('Skriv inn kundens tlf: ')
            kundefil=open('kunde.txt','r')
            tlf=kundefil.readline()
            while tlf!='':
                tlf=tlf.rstrip('\n')
                fornavn=kundefil.readline().rstrip('\n')
                etternavn=kundefil.readline().rstrip('\n')
                kort=kundefil.readline().rstrip('\n')
                if tlf==kunde:
                    print('Kunden finnes fra før og du kan fortsette med registrering')
                    funnet_kunde=True
                tlf=kundefil.readline()
            kundefil.close()
                
        #har vi IKKE funnet hunden i hund.txt OG funnet kunden i kunde.txt
        if funnet_hund==False and funnet_kunde==True:
            hundfil=open('hund.txt','a')
            hundenavn=input('Skriv inn hundens navn: ')
            hunderase=input('Skriv inn hundens rase: ')
            hundedato=input('Skriv inn ankomstdato: ')
            hundfil.write(hund+'\n')
            hundfil.write(hundenavn+'\n')
            hundfil.write(hunderase+'\n')
            hundfil.write(kunde+'\n')
            hundfil.write(hundedato+'\n')
            print('lista oppdatert')
        if funnet_kunde==False:
            print('Kunden må registreres først')
        ny_hund=input('Vil du legge til flere hunder? (ja/nei) ')

def slett_kunde():
    ny_kunde='ja'
    while ny_kunde=='ja':
        import os
        funnet_kunde=False
        funnet_hund=False
        slett=input('Skriv inn tlf på kunden du ønsker å slette: ')
        kundefil=open('kunde.txt','r')
        tlf=kundefil.readline()
        while tlf!='':
            tlf=tlf.rstrip('\n')
            navn=(kundefil.readline().rstrip('\n'))
            etternavn=(kundefil.readline().rstrip('\n'))
            kort=(kundefil.readline().rstrip('\n'))
            if tlf==slett:
                funnet_kunde=True
            tlf=kundefil.readline()
        kundefil.close()
        
        #har vi funnet kunden, må vi sjekke om han har registrert hunder på seg 
        if funnet_kunde==True:
            hundfil=open('hund.txt','r')
            hundid=hundfil.readline()
            while hundid!='':
                hundid=hundid.rstrip('\n')
                hundnavn=hundfil.readline().rstrip('\n')
                hundrase=hundfil.readline().rstrip('\n')
                ktlf=hundfil.readline().rstrip('\n')
                dato=hundfil.readline().rstrip('\n')
                if ktlf==slett:
                    funnet_hund=True
                hundid=hundfil.readline()
            hundfil.close()
                
        #har vi funnet kunden i kundefil.txt OG ikke funnet hunden i hund.txt 
        if funnet_kunde==True and funnet_hund==False:
            kundefil=open('kunde.txt','r')
            midlertidigfil=open('midlertidig.txt','w')
            tlf=kundefil.readline()
            while tlf!='':
                tlf=tlf.rstrip('\n')
                navn=(kundefil.readline().rstrip('\n'))
                etternavn=(kundefil.readline().rstrip('\n'))
                kort=(kundefil.readline().rstrip('\n'))
                if tlf!=slett:
                    midlertidigfil.write(tlf+'\n')
                    midlertidigfil.write(navn+'\n')
                    midlertidigfil.write(etternavn+'\n')
                    midlertidigfil.write(kort+'\n')
                tlf=kundefil.readline()
            kundefil.close()
            midlertidigfil.close()
            os.remove('kunde.txt')
            os.rename('midlertidig.txt','kunde.txt')
            print('Kunden er blitt slettet fra lista')
        elif funnet_kunde==False:
            print('Kunden finnes ikke i lista') 
        else:
            print('Kunden kan ikke slettes, da han har registrert hund.')
        ny_kunde=input('Vil du slette flere kunder? (ja/nei) ')

def main():
    valg=True
    while valg==True:
        print('Meny:')
        print('1. Legg til ny kunde')
        print('2. Legg til ny hund')
        print('3. Slett en kunde')
        valg=input('Velg et program: ')

        if valg=='1':
            registrer_ny_kunde()
            valg=True
        if valg=='2':
            registrer_ny_hund()
            valg=True
        if valg=='3':
            slett_kunde()
            valg=True
main()
