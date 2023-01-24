#Roman kjøpte 2000 eth
#1 eth kostet 40.00kr
#Roman betalte Robin 3% komisjon av 2000 eth

eth=float(40.00)
beholdning=2000*eth
robin_komisjon=beholdning/100*3

print('Du har',beholdning,'ETH.')
print('Robins komisjon kom på',robin_komisjon,'kr.')
#Beholdningen til roman er på 80.000kr og komisjonen (3%) er på 2.400kr

#2 uker senere solgte Roman 2000eth igjen
#1 eth kostet da 42.75 kr
#Robin fikk igjen 3% komisjon av salgssummen

eth=float(42.75)
ny_beholdning=2000*eth
ny_robin_komisjon=ny_beholdning/100*3

print('Din nye beholdning er',ny_beholdning,'kr.')
print('Du måtte selvsagt betale Robin på nytt, med hele',ny_robin_komisjon,'kr.')


#Nå må Roman finne ut av om han gikk i pluss eller minus
#etter at han solgte seg ut av eth og betalte komisjon til Robin

gevinst=(ny_beholdning-ny_robin_komisjon)-(beholdning+robin_komisjon)
print('Etter to uker har du tjent hele',gevinst,'kr.')
