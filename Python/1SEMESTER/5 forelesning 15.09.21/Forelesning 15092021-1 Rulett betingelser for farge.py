#Program for å beregne farge på tall på ruletten

#Alternativ 3, tar utgangspunkt i hvilke farger gjelder for hvilke intervaller og talltype
#! test på farge, dvs sann/usann på if test nr3.
#Kan ikke si om tallet er partall eller oddetall eller hvilket intervall det tilhører

#angi verdien på tallet på ruletten

tall=int(input('Skriv inn tallet på ruletten her '))

#finne gyldig tall først 0-36

if tall>=0 and tall<=36:
    if tall==0:
        print('Tallet er markert "grønn" på ruletten')
    else:
        #Hele if-setningen deles over flere linjer, må da stå i ekstra ()
        if ((tall>=1 and tall<=10 and (tall%2)==0)
        or (tall>=11 and tall<=18 and (tall%2)!=0)
        or (tall>=19 and tall<=28 and (tall%2)==0)
        or (tall>=29 and tall<=36 and (tall%2)!=0)):
            print('Tallet er markert med "svart" på ruletten')
        else:
            print('Tallet er markert "rødt" på ruletten')
else:
    print('Ugyldig verdi')

print('Programmet avsluttes')
