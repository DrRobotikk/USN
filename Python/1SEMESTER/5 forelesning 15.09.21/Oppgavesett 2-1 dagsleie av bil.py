#Dagsleie av bil:
#1 fastpris 750,-
#2 fastpris 300,- + 2,- pr km
#3 fastpris 150,- + 4,- pr km
#Program som sammenligner de tre alternativene
#Tabell 0-500km med steg på 50km
#avgjør best alternativ for hver rad

for n in range(0,501,50):
    print()
    print('Km lengde er: ',n,'km')
    pris1=750
    pris2=300+2*n
    pris3=150+4*n
    print('Prisene er:',pris1,pris2,pris3)
    if pris1<pris2 and pris3:
        print('I dette tilfelle er 1. alternativ det beste for deg')
    elif pris2<pris3:
        print('I dette tilfelle er 2. alternativ det beste for deg')
    else:
        print('I dette tilfelle er 3. alternativ det beste for deg')
