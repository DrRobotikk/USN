#Delprogram for å registrere ny kunde
def registrer_ny_kunde():
    ny_kunde='ja'
    while ny_kunde=='ja':
        funnet=False
        kunde=input('Oppgi nummeret til kunden: ')
        kundefil=open('kunde.txt','r')
        tlf=kundefil.readline()
        
        while tlf!='':
            tlf=tlf.rstrip('\n')
            fornavn=kundefil.readline().rstrip('\n')
            etternavn=kundefil.readline().rstrip('\n')
            mail=kundefil.readline().rstrip('\n')

            #Om kunden finnes fra før, kan den ikke registreres
            if tlf==kunde:
                print('Kunden finnes fra før.')
                funnet=True
            tlf=kundefil.readline()
        kundefil.close()

        #Dersom kunden ikke finnes fra før, fortsetter jeg med registrering av kunde
        if funnet==False:
            kundefil=open('kunde.txt','a')
            fornavn=input('Oppgi kundens fornavn: ')
            etternavn=input('Oppgi kundens etternavn: ')
            mail=input('Oppgi kundens mailadresse: ')

            kundefil.write(kunde+'\n')
            kundefil.write(fornavn+'\n')
            kundefil.write(etternavn+'\n')
            kundefil.write(mail+'\n')
            print('Kunden er registrert og du kan nå registrere dekksett.')
        kundefil.close()

        #Etter at kunden er blitt registrert, registrere jeg også et nytt sett med dekk tilhørende kunden
        if funnet==False:
            dekksettfil=open('dekksett.txt','a')
            regnr=input('Oppgi registrerings nummer på bilen: ')

            dekksettfil.write(kunde+'\n')
            dekksettfil.write(regnr+'\n')
            dekksettfil.close()
        #Dekksettet må også registreres i oppbevaringsfil
        if funnet==False:
            oppbevaringsfil=open('oppbevaring.txt','a')
            innlevert=input('Oppgi innleveringsdato: ')
            utlevert='X'
            hylle=input('Oppgi hyllenummer: ')
            pris=input('Oppgi pris på dekksett: ')

            oppbevaringsfil.write(kunde+'\n')
            oppbevaringsfil.write(regnr+'\n')
            oppbevaringsfil.write(innlevert+'\n')
            oppbevaringsfil.write(utlevert+'\n')
            oppbevaringsfil.write(hylle+'\n')
            oppbevaringsfil.write(pris+'\n')
            print('Dekksettet er blitt registrert.')
            oppbevaringsfil.close()
            
        ny_kunde=input('Flere kunder? ')
registrer_ny_kunde()
