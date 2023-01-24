#Program for å sortere talliste ved hjelp av for-løkke
#Denne delen av koden finner KUN det største tallet,
#og viser stegene for hvordan det blir flyttet til rett plass.

usortert=[5,3,2,1,4]

for n in range(0,len(usortert)-1,1):
    #print(n)#Her printer den antall steg i forhold til antall elementer i lista

    if usortert[n]>usortert[n+1]:
        bytte=usortert[n]
        usortert[n]=usortert[n+1]
        usortert[n+1]=bytte
        print('Resultatet etter bytte nr.',n+1,'er:')
        print(usortert)
        


