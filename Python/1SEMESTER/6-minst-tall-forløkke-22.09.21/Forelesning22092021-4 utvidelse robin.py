#Program for å lese inn 5 tall inn i en liste og finne det minste tallet

talliste=[] #defineres som en tom liste
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
    


print('Hele lista er:',talliste) #Utskrift av listeinnhold og listestørrelse etter fylling
liste_lengde=len(talliste)

print('Antall elementer i lista er:',liste_lengde)



