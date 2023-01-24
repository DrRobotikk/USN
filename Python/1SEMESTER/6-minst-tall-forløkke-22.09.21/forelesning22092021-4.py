#Program for å lese inn 5 tall inn i en liste og finne det minste tallet

talliste=[] #Talliste defineres som en tom liste
minst=1000000 #definerer det minste tallet (dummy)
tallnr=1 #Definerer rekkefølgen på tall i lista (dummy)
print('Lista til nå er:',talliste) #utskrift av listeinnhold før fylling
print() 

#FOR-løkke for å lese 5 tall inni lista talliste
for indeks in range(0,5,1):
    print('Tall nr:',indeks+1)
    listeverdi=int(input('Oppgi tall: '))
    talliste +=[listeverdi] #Innlest listeverdi legges inn i lista
    print('Lista til nå er:',talliste) #Utskrift av listeinnhold underveis/ med fylling
    print()
    if listeverdi<minst: #UTVIDELSE; finner det minste tallet
        minst=listeverdi
        tallnr=indeks+1 #Finner rekkefølge på minste tallet


print('Hele lista er:',talliste) #Utskrift av listeinnhold og listestørrelse etter fylling
liste_lengde=len(talliste)

print('Antall elementer i lista er:',liste_lengde)
print('Det minste tallet er',minst,'og er det',tallnr,'tallet i rekkefølga')

