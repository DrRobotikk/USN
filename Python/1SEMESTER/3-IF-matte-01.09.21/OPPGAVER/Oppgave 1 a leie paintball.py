#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata

leie_av_bane=2500
deltaker_tillegg=420

antall_deltakere=int(input('Hvor mange deltakere er med? '))

total_belop=leie_av_bane+deltaker_tillegg*antall_deltakere
print('Totalbeløpet er:',total_belop)
