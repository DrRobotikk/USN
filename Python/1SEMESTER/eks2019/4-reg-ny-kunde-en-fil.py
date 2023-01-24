#Delprogram for registrering av ny kunde
def registrer_ny_kunde():

    ny_kunde='ja'
    while ny_kunde=='ja':
        
        funnet=False
        kunde=input('Skriv inn kundens mobilnummer: ')
        kundefil=open('kunde.txt','r')#Sjekker i kunde.txt om kunden finnes
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
        #Dersom kunden ikke finnes fra før, kan vi fortsette med registrering
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
registrer_ny_kunde()
