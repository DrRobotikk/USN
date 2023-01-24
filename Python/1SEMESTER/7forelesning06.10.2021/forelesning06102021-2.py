#Oppgavesett 2 oppgave 2; minste tall i tallrekka og rekkefølge vha løkke
#Ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

minst=1000
tallnr=0

for n in range(1,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    if tall<minst:
        minst=tall
        tallnr=n
    else:
        if tallnr==0:
            minst=tall
            tallnr=1 #Kan også bruke tallnr=n
    print()
print('Minste tall er',minst,'og er det',tallnr,'i rekkefølga')    
