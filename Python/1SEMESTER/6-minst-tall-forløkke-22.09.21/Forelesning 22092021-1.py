#Finne minste tallet i en tallrekke

t1=int(input('Oppgi tallet: '))
t2=int(input('Oppgi tallet: '))
t3=int(input('Oppgi tallet: '))
t4=int(input('Oppgi tallet: '))
t5=int(input('Oppgi tallet: '))


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
    
print('Det minste tallet er',minst,'og er det',tallnr,'i tallrekka')

