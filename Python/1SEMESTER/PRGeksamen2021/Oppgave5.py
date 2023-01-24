#Delprogram for å slette dekksett
def slett_dekksett():
    nytt_dekksett='ja'
    while nytt_dekksett=='ja':
        import os
        funnet_dekk_oppbevaring=False
        funnet_dekksett=False
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
                print('Dekksettet finnes')
                funnet_dekk_oppbevaring=True
                funnet_tlf=tlf
            tlf=oppbevaringsfil.readline()
        oppbevaringsfil.close()
        
        #HAr vi funnet dekksettet i oppbevaringsfila, må vi sjekke om den finnes i dekksett.txt
        if funnet_dekk_oppbevaring==True:
            dekksettfil=open('dekksett.txt','r')
            mobil=dekksettfil.readline()
            while mobil!='':
                mobil=mobil.rstrip('\n')
                reginr=dekksettfil.readline().rstrip('\n')

                if funnet_tlf==mobil:
                    print('Funnet dekksett i dekkfila')
                    funnet_dekksett=True
                mobil=dekksettfil.readline()
            dekksettfil.close()

            #HAr vi funnet dekksett i begge filene
            #må vi sjekke om det har utleveringsdato for å slette
            if funnet_dekk_oppbevaring==True and funnet_dekksett==True:
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
                    behold_regnr=regnummer

                    if levert_ut=='X':
                        midlertidigfil.write(nummer+'\n')
                        midlertidigfil.write(regnummer+'\n')
                        midlertidigfil.write(levert_inn+'\n')
                        midlertidigfil.write(levert_ut+'\n')
                        midlertidigfil.write(hylleplass+'\n')
                        midlertidigfil.write(prisen+'\n')
                        slettet=True
                    nummer=oppbevaringsfil.readline()

                    #Denne delen av koden som skal slette dekksettet fra dekksett.txt
                    #sletter dessverre hele fila og jeg rekker ikke å gjøre om på den nå
                    #Det jeg skulle ha gjort var å begynne med å slette poster fre fil
                    #dekksett.txt, for da hadde jeg behold reg.nummeret til posten,
                    #for så å fortsette å slette poster fra oppbevaring.txt
                    #Jeg oppdaget det dessverre for sent.
                    if slettet==True:
                        
                        dekksettfil=open('dekksett.txt','r')
                        midlertidig1fil=open('midlertidig1.txt','w')
                        mobnr=dekksettfil.readline()
                        while mobnr!='':
                            
                            mobnr=mobnr.rstrip('\n')
                            rnummer=dekksettfil.readline().rstrip('\n')
                            if behold_regnr==rnummer:
                                
                                midlertidig1fil.write(mobnr+'\n')
                                midlertidig1fil.write(rnummer+'\n')
                            mobnr=dekksettfil.readline()
                        dekksettfil.close()
                        midlertidig1fil.close()
                        os.remove('dekksett.txt')
                        os.rename('midlertidig1.txt','dekksett.txt')
                    
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
        
    
