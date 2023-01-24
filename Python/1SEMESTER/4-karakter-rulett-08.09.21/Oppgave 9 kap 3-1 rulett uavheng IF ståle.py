#Oppgave 9 kap 3, løst ved uavhengige if-tester...
#...med test på intervall og "talltype"
#tegn programkart først

tall=int(input('Skriv inn her '))

if tall>=0 and tall<=36:
    if tall==0:
        print('Tallet er markert grønn på ruletten')
    else:
        if tall>=1 and tall<=10 and (tall%2)==0:
            print('Tallet er partall og markert svart på ruletten')
        if tall>=1 and tall<=10 and (tall%2)!=0:
            print('Tallet er oddetall og markert rødt på ruletten')
        if tall>=11 and tall<=18 and (tall%2)==0:
            print('Tallet er partall og markert "rødt" på ruletten')
        if tall>=11 and tall<=18 and (tall%2)!=0:
            print('Tallet er oddetall og markert "svart" på ruletten')

