#Oppgavesett 2 oppgave 2; minste tall i tallrekka og rekkefølge vha løkke

#for å unngå å bruke dummy, lar en første tall en tar imot også være minstetall til nå
#det gjør en i tilfelle utenfor for-løkka
#ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

print('Tall nr1: ')
tall=int(input('Oppgi tall: '))
minst=tall
tallnr=1
print()

for n in range(2,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    if tall<minst:
        minst=tall
        tallnr=n
    print()
print('Minste tall er',minst,'og er det',tallnr,'i rekkefølga')    
