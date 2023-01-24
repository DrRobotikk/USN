#første og siste element i en liste skal bytte plass
talliste=[5,3,2,1,4]

print('Lista før bytte/ usortert liste er',talliste)
print()

#bytte er variabelen vi bruker for å ta vare på første verdi
bytte=talliste[3]

#talliste av 0 får verdien til talliste av 4
talliste[3]=talliste[4]

#talliste av 4 får verdien som vi tok vare på i byttevariabelen
talliste[4]=bytte
#Her bytter tall 4 og tall 1 plass i lista [5,3,2,4,1]


#Her vil tall 5 og tall 1 bytte plass, tallista er så[1,3,2,4,5]
bytte1=talliste[0]
talliste[0]=talliste[4]
talliste[4]=bytte1


#siste steget er å bytte plass på tall 3 og 2 [1,2,3,4,5]
bytte2=talliste[1]
talliste[1]=talliste[2]
talliste[2]=bytte2

#lista etter bytte er
print('Den sorterte lista er',talliste)



