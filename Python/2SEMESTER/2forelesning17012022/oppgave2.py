#Program for å sortere talliste ved hjelp av for-løkke

usortert=[5,3,2,1,4]#oppretter en usortert liste
lengde=len(usortert)#oppretter en liste_lengde_variabel

#Denne for_løkka gjør at den gjentar indre forløkke frem til
#hele lista er sortert i stigende rekkefølge
for x in range(0,lengde,1):
    print()
    print('Dette er gjennomgang nr.',x+1)

    #Denne forløkka finner det største tallet i lista og flytter
    #det tallet til siste plass
    for n in range(0,lengde-1,1):
            #print(n)#Her printer den antall steg i forhold til antall elementer i lista

        #Selve koden for plassbytte av tall i lista
        if usortert[n]>usortert[n+1]:
            bytte=usortert[n]
            usortert[n]=usortert[n+1]
            usortert[n+1]=bytte
            print('Resultatet etter bytte nr.',n+1,'er:',usortert)
            
print()
print('Den sorterte lista er:',usortert)


