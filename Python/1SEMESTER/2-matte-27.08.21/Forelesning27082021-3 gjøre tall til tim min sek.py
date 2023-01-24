#Program 2-17 s.82, alternativ fremgangsmåte 1
#Bruk av variable som holder orden på gjenværende sekunder etter en konvertering

#Gjøre om fra sekunder til timer, minutter og sekunder
#time=3600 sek, 60 min

#Ber brukeren oppgi antall sekunder
ant_sek=int(input('Oppgi antall sekunder som skal konverteres: ')) #Her må vi bruke "int" for at python skal kunne kalkulere med tallet "sekunder"

#Beregner antall timer
ant_tim=ant_sek//3600 #Eks.3666//3600= 1 time og 66 sek
rest_sek_etter_tim=ant_sek-3600*ant_tim #Eks. 3666-(3600*1time og 66sek)=66 sek

#Beregner antall gjenværende minutter og sekunder
ant_min=rest_sek_etter_tim//60 #eks:66 sek//60= 1 minutt og 6 sek

rest_sek_etter_min=rest_sek_etter_tim-60*ant_min #Eks: 66-(60*1 minutt og 6 sekunder)=6 sekunder

print(ant_sek, 'sekunder gjort om til timer, minutter og sekunder blir:')
print('Timer: ',ant_tim)
print('Minutter: ',ant_min)
print('Sekunder: ',rest_sek_etter_min)

