#dersom det er 10 deltaker er prisen pr. deltaker 380kr
#lag et program som beregner og skriver ut prisen basert på antall deltakere som inndata

leie_av_bane=2500
#deltaker_tillegg=420

antall_deltakere=int(input('Hvor mange deltakere er med? '))

if antall_deltakere<10:
    deltaker_tillegg=420
else:
    deltaker_tillegg=380

total_belop=leie_av_bane+deltaker_tillegg*antall_deltakere
print(deltaker_tillegg)
print('Totalbeløpet er:',total_belop)
