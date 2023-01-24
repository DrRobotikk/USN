#Program 2-17 s.82, alternativ fremgangsmåte 2
#bruk av variable som holder orden på gjenværende sekunder etter en konvertering

#Gjøre om fra sekunder til timer, minutter og sekunder

#Ber brukeren oppgi antall sekunder

ant_sek=int(input('Oppgi antall sekunder her: '))

#Beregner antall timer
ant_tim=ant_sek//3600
rest_sek_etter_tim=ant_sek%3600

#Beregner antall gjenværende minutter og sekunder

ant_min=rest_sek_etter_tim//60

rest_sek_etter_min=rest_sek_etter_tim%60

#Skriv ut resultatet

print(ant_sek,'sekunder gjort om til timer, minutter og sekunder blir:')
print('Timer:',ant_tim)
print('Minutter:',ant_min)
print('Sekunder:',rest_sek_etter_min)






#hvordan løser programmet i boka problemstillingen?

