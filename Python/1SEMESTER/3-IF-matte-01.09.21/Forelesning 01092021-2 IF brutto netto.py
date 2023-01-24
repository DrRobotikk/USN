#Beregne bruttolønn, skattetrekk og nettolønn ved hjel av IF
#if betingelse:
#    "så-blokk" (INNRYKK)
#else:
#    "ellers-blokk" (INNRYKK)

#først inndata av brukeren
timelonn=float(input('Hva er din timelønn? '))
antall_timer=float(input('Hvor mange timer har du jobbet? '))

#Beregne bruttolønn (timelonn*antall_timer)

bruttolonn=timelonn*antall_timer

#finne riktig skattesats

if bruttolonn<20000:
    skattesats=28
else:
    skattesats=35
#Beregner skatt og nettolønn
skatt_i_kr=bruttolonn*skattesats/100
nettolonn=bruttolonn-skatt_i_kr

#skrive ut lønnsberegninga
print('Din bruttolønn er:',format(bruttolonn,'.2f'))
print('Din skatteprossent er:',skattesats,'og skattetrekket i kr er',format(skatt_i_kr,'.2f'))
print('Du får utbetalt',format(nettolonn,'.2f'),'kr.')
