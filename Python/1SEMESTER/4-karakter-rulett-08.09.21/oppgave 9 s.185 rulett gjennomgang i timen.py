#Gjennomgang av rulettoppgave 9 side 185

#program for å avgjøre fargen på rulettallet
#alternativ 1 nøsting av hvis-setninger mtp intervall og farge

#steg 1, avgjøre gyldig tall
#steg 2, finne riktig intervall

#brukeren oppgir verdien på ruletten

tall=int(input('Hva er tallet på ruletten '))

#tester om verdien på tall er riktig og beregner riktig farge for gyldige verdier

if tall>=0 and tall<=36:
    print('Gyldig tall')

    if tall==0:
        print('Tallet er',tall,'og er markert "Grønn" på ruletten')
    else:
        if tall<=10:
            print('Taller er',tall,'og er i intervallet [1,10]')
        else:
            if tall<=18:
                print('Tallet er',tall,'og er i intervallet [11,18]')
            else:
                if tall<=28:
                    print('Tallet er',tall,'og er i intervallet [19,28]')
                else:
                    if tall<=36:
                        print('Tallet er',tall,'og er i intervallet [29,36]')
else:
    print('Ugyldig tall')
