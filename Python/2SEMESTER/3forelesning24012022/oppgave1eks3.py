#Program for å sortere talliste ved hjelp av for-løkke

usortert=[1,2,3,4,5,6,7]
lengde=len(usortert)
print('Lista før sortering er',usortert)

#Denne for_løkka gjør at den gjentar indre forløkke frem til
#hele lista er sortert i stigende rekkefølge
for x in range(0,lengde,1):
    print()
    print('Gjennomgang nr.',x+1,'starter.')
    print()

    #Denne forløkka finner det største tallet i lista og flytter
    #det tallet til siste plass
    for n in range(0,lengde-1,1):
        print('Sammenligning nr.',n+1,'dvs.',usortert[0+n],usortert[1+n])
        
        #Selve koden for plassbytte av tall i lista
        if usortert[n]>usortert[n+1]:
            print('Det må byttes')
            bytte=usortert[n]
            usortert[n]=usortert[n+1]
            usortert[n+1]=bytte
            print(usortert)
            print()
            bytt=True                        
print()
print('Den sorterte lista er:',usortert)


