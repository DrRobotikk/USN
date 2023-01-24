#største tallet i tall_rekke
#summen av alle tallene i tall_rekke

tall_rekke=(3,6,2,18,11,7,28,19)

#finne største tallet og sammenligne med neste tall i tall_rekke
#beholde største tallet hittil, sammenligne med neste tall i tall_rekke
#beholde største tallet hittil, sammenligne med neste tall i tall_rekke
#denne algorytmen gjentas frem til største tallet er på rett plass-
#for så å finne neste tall og kjøre samme repetisjon frem til alle tall er på rett plass.
print(max(tall_rekke))

#sum=0 (startverdi/ før førstetall)
#sum=sum + nytt tall, gjentas for alle tallene
#før første tall: sum=0 (tar med summen fra før + nytt tall)
#etter første tall: sum=0+3=3
#etter andre tall: sum=3+6=9
#etter tredje tall: sum=9+2=11
#etter fjerde tall: sum=11+18=29
#algorytmen fortsetter sånn frem til alle tallene i tall_rekke er summert


print(sum(tall_rekke))

