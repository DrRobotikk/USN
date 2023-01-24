#Delprogram for å slette dekksett
def slett_dekksett():
    nytt_dekksett='ja'
    while nytt_dekksett=='ja':
        import os
        funnet_dekk_oppbevaring=False
        funnet_dekksett=False
        slettbar=False
        slettet=False
        slett=input('Oppgi mobilnr til kunden: ')
        oppbevaringsfil=open('oppbevaring.txt','r')
        tlf=oppbevaringsfil.readline()
        while tlf!='':
            tlf=tlf.rstrip('\n')
            regnr=oppbevaringsfil.readline().rstrip('\n')
            innlevert=oppbevaringsfil.readline().rstrip('\n')
            utlevert=oppbevaringsfil.readline().rstrip('\n')
            hylle=oppbevaringsfil.readline().rstrip('\n')
            pris=oppbevaringsfil.readline().rstrip('\n')

            if slett==tlf:
                print('Dekksettet finnes i oppbevaring.txt')
                funnet_dekk_oppbevaring=True
            tlf=oppbevaringsfil.readline()
        oppbevaringsfil.close()
        
        #HAr vi funnet dekksettet i oppbevaringsfila, må vi sjekke om den finnes i dekksett.txt
        if funnet_dekk_oppbevaring==True:
            dekksettfil=open('dekksett.txt','r')
            mobil=dekksettfil.readline()
            while mobil!='':
                mobil=mobil.rstrip('\n')
                reginr=dekksettfil.readline().rstrip('\n')

                if slett==mobil:
                    print('Funnet dekksett i dekksett.txt')
                    funnet_dekksett=True
                mobil=dekksettfil.readline()
            dekksettfil.close()

            #HAr vi funnet dekksett i begge filene
            #må vi sjekke om det har utleveringsdato for å slette
            if funnet_dekk_oppbevaring==True and funnet_dekksett==True:
                oppbevaringsfil=open('oppbevaring.txt','r')
                mnr=oppbevaringsfil.readline()
                while mnr!='':
                    mnr=mnr.rstrip('\n')
                    rnr=oppbevaringsfil.readline().rstrip('\n')
                    ainn=oppbevaringsfil.readline().rstrip('\n')
                    aut=oppbevaringsfil.readline().rstrip('\n')
                    hp=oppbevaringsfil.readline().rstrip('\n')
                    pr=oppbevaringsfil.readline().rstrip('\n')
                    if aut!='X' and mnr==slett:
                        print('Dekksettet kan slettes, da det har utleveringsdato')
                        slettbar=True
                    mnr=oppbevaringsfil.readline()
                oppbevaringsfil.close()
                if funnet_dekk_oppbevaring==True and funnet_dekksett==True and slettbar==True:
                    
                    oppbevaringsfil=open('oppbevaring.txt','r')
                    midlertidigfil=open('midlertidig.txt','w')
                    nummer=oppbevaringsfil.readline()
                    while nummer!='':
                        nummer=nummer.rstrip('\n')
                        regnummer=oppbevaringsfil.readline().rstrip('\n')
                        levert_inn=oppbevaringsfil.readline().rstrip('\n')
                        levert_ut=oppbevaringsfil.readline().rstrip('\n')
                        hylleplass=oppbevaringsfil.readline().rstrip('\n')
                        prisen=oppbevaringsfil.readline().rstrip('\n')

                        if levert_ut=='X' and nummer!=slett:
                            midlertidigfil.write(nummer+'\n')
                            midlertidigfil.write(regnummer+'\n')
                            midlertidigfil.write(levert_inn+'\n')
                            midlertidigfil.write(levert_ut+'\n')
                            midlertidigfil.write(hylleplass+'\n')
                            midlertidigfil.write(prisen+'\n')
                            slettet=True
                        
                        nummer=oppbevaringsfil.readline()
                        
                    oppbevaringsfil.close()
                    midlertidigfil.close()
                    os.remove('oppbevaring.txt')
                    os.rename('midlertidig.txt','oppbevaring.txt')

            if slettet==True:
                print('lista oppdatert')
            else:
                print('Lista ikke oppdatert')
                
        
        nytt_dekksett=input('Skal du slette flere dekksett? ')
slett_dekksett()
        
    

        
    
