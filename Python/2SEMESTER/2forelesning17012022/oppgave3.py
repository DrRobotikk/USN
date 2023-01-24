#Program for å sortere talliste ved hjelp av for-løkke

usortert=[5,3,2,1,4]
for x in range(0,len(usortert),1):
    print('Her starter gjennomgang nr.',x+1)

    for n in range(0,len(usortert)-1,1):
        #print(n)#Her printer den antall steg i forhold til antall elementer i lista

        if usortert[n]>usortert[n+1]:
            bytte=usortert[n]
            usortert[n]=usortert[n+1]
            usortert[n+1]=bytte
            print('Resultatet etter bytte nr.',n+1,'er:')
            print(usortert)
print('Den sorterte lista er:',usortert)


#Basert på oppgave 1 og oppgave 2, med kjøreresultat av de ulike listene,
#hva er utfordringen («gjennomgangsmessig») med denne strategien/algoritmen?

#Utfrodringen er at programmet må gå gjennom den usorterte lista like mange
#ganger som det er elementer i lista, selv om lista allerede er sortert.
#Det er egentlig ikke en utfordring med så få elementer i lista, men den dagen
#lista inneholder flere tusen elementer, så vil programmet bli tregt.
