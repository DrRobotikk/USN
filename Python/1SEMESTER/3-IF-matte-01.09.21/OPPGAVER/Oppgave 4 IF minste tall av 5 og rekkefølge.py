#Lag et programm som tar imot 5 tall som inndata og som
#skriver ut verdien og tallnummeret på det minste tallet

tall1=int(input('Skriv inn første tallet her: '))
tall2=int(input('Skriv inn andre tallet her: '))
tall3=int(input('Skriv inn tredje tallet her: '))
tall4=int(input('Skriv inn fjerde tallet her: '))
tall5=int(input('Skriv inn siste tallet her: '))

if tall1<=tall2:
    minst=tall1
    plass=1
else:
    minst=tall2
    plass=2
if tall3<minst:
    minst=tall3
    plass=3
if tall4<minst:
    minst=tall4
    plass=4
if tall5<minst:
    minst=tall5
    plass=5

print('Det minste tallet er',minst,'og ligger på',plass,'plass.')
