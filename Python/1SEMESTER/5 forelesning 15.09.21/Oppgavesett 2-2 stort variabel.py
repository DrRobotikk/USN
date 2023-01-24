#Lag et program som tar imot 5 tall som inndata
#og som skriver ut verdien og tallnr på det minste tallet

storst=1000000000*999999999 #Setter største verdi slik at våre tall er mindre enn storst

rekkefolge=0 #Angir rekkefølgen for tallet i for-løkka

for n in range(1,6,1): #Gir meg muligheten til å komme med 5 tall programmet skal jobbe med
    tall=int(input('Oppgi tall '))
    if tall<storst: #Hvis inputtallet er mindre enn storst-variabel:
        storst=tall #Blir verdien i storst erstattet med ny minsteverdi
        rekkefolge=n #og rekkefølgen i for-løkka blir angitt i forhold til minste tallet

print('Minste tallet er',storst,'og er det',rekkefolge,'tallet i rekkefølgen.')
