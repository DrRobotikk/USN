#Oppgave 9 kap 3, løst ved uavhengige if-tester...
#...med test på intervall og "talltype"
#tegn programkart først

partall=False

tall=int(input('Skriv inn tallet her '))
if tall%2==0:
    partall=True

if tall<0 or tall>36:
    print('Ugyldig verdi')
if tall==0:
    print('Tallet har verdien',tall,'og er grønn')
if tall>0 and tall<=10:
    print('Tallet har verdien',tall,'og er i intervall [1,10]')
if tall>10 and tall<=18:
    print('tallet har verdien',tall,'og er i intervall [11,18]')
if tall>18 and tall<=28:
    print ('Tallet har verdien',tall,'og er i intervall [19,28]')
if tall>28 and tall<=36:
    print ('Tallet har verdien',tall,'og er i intervall [29,36]')
if partall and (tall>0 and tall<=10):
    print('Tallet er partall')
if partall==False and (tall>0 and tall<=10):
    print('Tallet er oddetall')
if partall and (tall>10 and tall<=18):
    print('Tallet er partall')
if partall==False and (tall>10 and tall<=18):
    print('Tallet er oddetall')
if partall and (tall>18 and tall<=28):
    print('Tallet er partall')
if partall==False and (tall>18 and tall<=28):
    print('Tallet er oddetall')
if partall and (tall>28 and tall<=36):
    print('Tallet er partall')
if partall==False and(tall>28 and tall<=36):
    print('Tallet er oddetall')

