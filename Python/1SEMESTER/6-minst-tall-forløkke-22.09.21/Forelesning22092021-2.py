#Oppgavesett 2 oppgave 2; minste tall i tallrekka og rekkefølge vha løkke

minst=1000000
tallnr=0

for n in range(1,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    if tall<=minst:
        minst=tall
        tallnr=n
    print()
print('Minste tall er',minst,'og er det',tallnr,'i rekkefølga')    
