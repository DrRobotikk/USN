#Rulett har lommer med tall fra 0-36
#lomme 0 er grønn
#lomme 1 til 10; partall er svart; oddetall er rød
#lomme 11 til 18; partall er rød; oddetall er svart
#lomme 19 til 28; partall er svart; oddetall er rød
#lomme 29 til 36; partall er rød; oddetall er svart

#Program med innput mellom 0-36 og programmet skal svare hvilken farge
#tall større enn 36 gir feilmelding

tall_rute=int(input('Skriv inn rulettallet du vil vite fargen på: '))

if tall_rute==0:
    print('grønn')
else:
    if tall_rute>36:
        print('Det finnes kun 36 ruter i rulett')
    else:
        if tall_rute>=29:
            if tall_rute%2==0:
                print('rød fra 29 til 36')
            else:
                print('svart fra 29 til 36')
        else:
            if tall_rute>=19:
                if tall_rute%2==0:
                    print('svart fra 19 til 29')
                else:
                    print('rød fra 19 til 29')
            else:
                if tall_rute>=11:
                    if tall_rute%2==0:
                        print('rød fra 11 til 18')
                    else:
                        print('svart fra 11 til 18')
                else:
                    if tall_rute>=1:
                        if tall_rute%2==0:
                            print('svart fra 1 til 10')
                        else:
                            print('rød fra 1 til 10')

#Det viser seg at koden funker så lenge jeg begynner fra det største tallet.
#satt med denne oppgaven i hele i går og lagde IFer fra 1-36 uten hell
#Men i denne rekkefølgen så fungerer det utmerket
