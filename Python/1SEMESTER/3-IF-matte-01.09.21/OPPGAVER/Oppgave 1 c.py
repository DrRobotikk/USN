#dersom det er 20 deltaker er prisen pr. deltaker 350kr
#lag et program som beregner og skriver ut prisen basert på antall deltakere som inndata

leie_av_bane=2500
#deltaker_tillegg=420

antall_deltakere=int(input('Hvor mange deltakere er med? '))

if antall_deltakere<10:
    deltaker_tillegg=420
else:
    #deltaker_tillegg=380
    if antall_deltakere<20:
        deltaker_tillegg=380
    else:
        deltaker_tillegg=350

total_belop=leie_av_bane+deltaker_tillegg*antall_deltakere
print(deltaker_tillegg)
print('Totalbeløpet er:',total_belop)
