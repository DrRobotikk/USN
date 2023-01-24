#Delprogram for å slette en eksisterende kunde
def slett_kunde():
    ny_kunde='ja'
    while ny_kunde=='ja':
        import os
        funnet_kunde=False
        funnet_hund=False
        slett=input('Skriv inn tlf på kunden du ønsker å slette: ')
        kundefil=open('kunde.txt','r')#Sjekker om kunden finnes i kunde.txt
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
                
        #har vi funnet kunden i kunde.txt OG ikke funnet hunden i hund.txt 
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
slett_kunde()
