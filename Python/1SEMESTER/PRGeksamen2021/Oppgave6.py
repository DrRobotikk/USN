#Delprogram for utskrift av dekksett for kunde
def dekksett_for_kunde():
    ny_utskrift='ja'
    while ny_utskrift=='ja':
        funnet_kunde=False
        funnet_dekksett=False
        funnet_oppbevaring=False
        
        utskrift=input('Oppgi kundens mobilnummer: ')
        #Åpner kunde.txt og sammenligne input "utskrift" med "tlf"
        kundefil=open('kunde.txt','r')
        tlf=kundefil.readline()
        while tlf!='':
            tlf=tlf.rstrip('\n')
            fornavn=kundefil.readline().rstrip('\n')
            etternavn=kundefil.readline().rstrip('\n')
            mail=kundefil.readline().rstrip('\n')

            if utskrift==tlf:
                print('Kunden med opplysningene:',tlf,etternavn,mail,'har:')
                funnet_kunde=True
                funnet_tlf=tlf #Lager ny variabel for å beholde data i tlf
            tlf=kundefil.readline()
        kundefil.close()
        
        #Hvis vi har funnet kunden i kunde.txt, må vi sjekke om han har
        #registrert dekksett i både dekksett.txt og oppbevaring.txt
        if funnet_kunde==True:
            dekksettfil=open('dekksett.txt','r')
            kundetlf=dekksettfil.readline()
            while kundetlf!='':
                kundetlf=kundetlf.rstrip('\n')
                regnr=dekksettfil.readline().rstrip('\n')
                
                #Hvis det finnes kundetlf i dekksett.txt, må vi åpne oppbevaring.txt for å hente ut resten av data
                if funnet_tlf==kundetlf:
                    funnet_dekksett=True
                    oppbevaringsfil=open('oppbevaring.txt','r')
                    mobil=oppbevaringsfil.readline()
                    while mobil!='':
                        mobil=mobil.rstrip('\n')
                        reginr=oppbevaringsfil.readline().rstrip('\n')
                        innlevert=oppbevaringsfil.readline().rstrip('\n')
                        utlevert=oppbevaringsfil.readline().rstrip('\n')
                        hylle=oppbevaringsfil.readline().rstrip('\n')
                        pris=oppbevaringsfil.readline().rstrip('\n')

                        #Om kundetlf=mobil i oppbevaring.txt, kan vi skrive ut regnummeret
                        if kundetlf==mobil:
                            print(reginr)
                            funnet_oppbevaring=True
                        mobil=oppbevaringsfil.readline()
                    oppbevaringsfil.close()
                kundetlf=dekksettfil.readline()   
            dekksettfil.close()
        #Her kommer printene for om inndata ikke finnes i filene
        if funnet_kunde==False:
            print('Kunden finnes ikke')
        if funnet_dekksett==False or funnet_oppbevaring==False:
            print('Ingen registrerte dekksett')
        ny_utskrift=input('Ønsker du utskrift av flere dekksett? (ja/nei)')
dekksett_for_kunde()
