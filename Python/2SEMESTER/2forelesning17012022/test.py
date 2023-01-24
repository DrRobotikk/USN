liste=[5,4,3,2,1]

lengde=len(liste)
for a in range(0,lengde-1,1):
    print()
    print('Dette er gjennomgang nr.',a+1)
    

    for b in range(0,lengde-1,1):

        if liste[b]>liste[b+1]:
            bytte=liste[b]
            liste[b]=liste[b+1]
            liste[b+1]=bytte

            print('Lista etter bytte nr.',b+1,'er',liste)

    
            
            
