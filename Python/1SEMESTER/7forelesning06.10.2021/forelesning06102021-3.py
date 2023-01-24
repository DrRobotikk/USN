#Program for å lese inn 5 tall inn i en liste og finne det minste tallet

talliste=[] #Talliste defineres som en tom liste
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

               #HER STARTER UTVIDELSE AV PROGRAM 22092021-4
#klargjør for å finne minste tall, settes til første tall i lista utenfor løkka

minste_tall=talliste[0]
tallnr=1

for index in range(1,5,1):
    if talliste[index]<minste_tall:
        #da er det et nytt tall som er minste_tall
        minste_tall=talliste[index]
        #tallnr i rekka er index i lista + 1
        tallnr=index+1
print('Det minste tallet er',minste_tall,'og det er tall nr.',tallnr,'i lista')
