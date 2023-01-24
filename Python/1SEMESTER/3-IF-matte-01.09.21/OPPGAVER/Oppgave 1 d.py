#gammelt system:
#baneleie=2500
#deltakere<10=420
#deltakere>=10=380
#deltakere>=20=350
#Nytt system:
#deltakere<10=3500 bane og 350 deltaker
#deltakere<20=2000 bane og 400 deltaker
#deltakere<30=1000 bane og 450 deltaker
#Maks antall deltakere=30 (alt over 30 blir en egen tekst, og ikke en del av utregningen)
deltakere=int(input('Hvor mange deltakere er med? '))

if deltakere>30:
    print('Maks antall deltakere per bane er 30 personer.')
else:
    if deltakere<=10:
        deltaker_pris=420
        belop_gammel=2500+deltaker_pris*deltakere
    else:
        deltaker_pris=380
        belop_gammel=2500+deltaker_pris*deltakere
        if deltakere>=20:
            deltaker_pris=350
            belop_gammel=2500+deltaker_pris*deltakere
    print('Totalbeløpet beregnet etter det gamle systemet er:',belop_gammel)

#nytt system
    if deltakere<10:
        baneleie=3500
        deltaker_pris=350
        belop_nytt=baneleie+deltaker_pris*deltakere
    else:
        baneleie=2000
        deltaker_pris=400
        belop_nytt=baneleie+deltaker_pris*deltakere
        if deltakere>=20:
            baneleie=1000
            deltaker_pris=450
            belop_nytt=baneleie+deltaker_pris*deltakere
    print('Totalbeløpet beregnet etter det nye systemet er:',belop_nytt)

    #hvilket system er mest lønnsomt for bedriften?
    if belop_nytt>belop_gammel:
        print('I dette tilfellet er det det nye systemet er mest lønnsomt for bedriften')
    else:
        print('I dette tilfellet er det det gamle systemet er mest lønnsomt for bedriften')
   
