#Beregning av bruttolønn

#Først trenger vi input/inndata fra brukeren

timelonn=int(input('Hva er din timelønn? '))
antall_timer=int(input('hvor mange timer har du arbeidet? '))

#Variabelnavn notasjon eller konvensjon, enten antall_timer eller
#antalTimer ("lowerCamelCase") jfr. s. 66

#Beregner bruttolønn/ beregning
bruttolonn=timelonn*antall_timer

#Skriver ut lønnsberegningen/ output, utdata

print('Din bruttolønn er da',bruttolonn)


#Variebelen timelonn og bruttolonn må behandles som tall
#timelonn=int(input('hva er din timelønn')); int=tall
