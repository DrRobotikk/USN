#Delprogram for å registrere ny hund
def registrer_ny_hund():
    ny_hund='ja'
    while ny_hund=='ja':
        funnet_kunde=False
        funnet_hund=False
        hund=input('Skriv inn hundens ID: ')
        hundfil=open('hund.txt','r')#Sjekker om hunden finnes fra før i hund.txt
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
registrer_ny_hund()
