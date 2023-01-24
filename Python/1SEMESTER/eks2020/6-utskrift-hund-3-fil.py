def hunder_fra_kennel():
    
    ny_utskrift='ja'
    while ny_utskrift=='ja':
        funnet_kennel=False
        funnet_hund=False
        funnet_eier=False
        
        utskrift=input('Skriv inn kennelnavn: ')
        #Åpner oppdretter.txt og finner frem kennelnavn utifra input "utskrift"
        oppdretterfil=open('oppdretter.txt','r')
        oppdretterid=oppdretterfil.readline()
        while oppdretterid!='':
            oppdretterid=oppdretterid.rstrip('\n')
            kennelnavn=oppdretterfil.readline().rstrip('\n')
            oppfornavn=oppdretterfil.readline().rstrip('\n')
            oppetternavn=oppdretterfil.readline().rstrip('\n')

            if utskrift==kennelnavn:
                print('I kennelen', utskrift,'finnes det:')
                funnet_kennel=True
                funnet_oppdretterid=oppdretterid #Lager ny variabel for å beholde oppdretterid. Den får nemlig ny verdi i linja rett under
            oppdretterid=oppdretterfil.readline()
        oppdretterfil.close()
        
        #Hvis vi har funnet riktig kennel, må vi sjekke om det finnes hunder i kennelen
        if funnet_kennel==True:
            hundefil=open('hund.txt','r')
            hundeid=hundefil.readline()
            while hundeid!='':
                hundeid=hundeid.rstrip('\n')
                eierid=hundefil.readline().rstrip('\n')
                oppid=hundefil.readline().rstrip('\n')
                hundenavn=hundefil.readline().rstrip('\n')
                hundekjonn=hundefil.readline().rstrip('\n')
                alder=hundefil.readline().rstrip('\n')
                
                #Hvis det finnes hunder i kennelen, må vi åpne eierfila for å hente ut navn på eiere
                if funnet_oppdretterid==oppid:
                    funnet_hund=True
                    hundeeierfil=open('hundeeier.txt','r')
                    hundeeierid=hundeeierfil.readline()
                    while hundeeierid!='':
                        hundeeierid=hundeeierid.rstrip('\n')
                        hundeeiernavn=hundeeierfil.readline().rstrip('\n')
                        hundeeieretternavn=hundeeierfil.readline().rstrip('\n')

                        #Her ser vi at hvis eierid i hundefil og eierfil stemmer overens,
                        #så skriver vi ut info om hund samt fornavn og etternavn på eieren
                        if hundeeierid==eierid:
                            print(hundenavn, hundekjonn, alder, hundeeiernavn, hundeeieretternavn)
                            funnet_eier=True
                        hundeeierid=hundeeierfil.readline()
                    hundeeierfil.close()
                hundeid=hundefil.readline()   
            hundefil.close()
        ny_utskrift=input('Ønsker du flere utskrifter? ')
    
hunder_fra_kennel()     

                
