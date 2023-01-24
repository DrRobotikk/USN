#Finn minste tallet i en tallrekke bestående av 5 tall
#2 variable for å holde orden på minste tall og tallnr, begge settes til 0

minst=0
tallnr=0

#5 virkårlige tall som inndata
t1=int(input('Oppgi tall 1 '))
t2=int(input('Oppgi tall 2 '))
t3=int(input('Oppgi tall 3 '))
t4=int(input('Oppgi tall 4 '))
t5=int(input('Oppgi tall 5 '))

#Finne minste tallet og tallnummeret
if t1>t2:
    minst=t2
    tallnr=2
else:
    minst=t1
    tallnr=1

if minst>t3:
    minst=t3
    tallnr=3

if minst>t4:
    minst=t4
    tallnr=4

if minst>t5:
    minst=t5
    tallnr=5
    
#Så skriver vi resultatet, minste tall og tallnummer
print('Det minste tallet er',minst,'og er det',tallnr,'i rekka')

#Husk å tegne programkart
