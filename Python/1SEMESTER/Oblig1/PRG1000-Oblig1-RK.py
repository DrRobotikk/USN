fortsett='ja'

while fortsett=='ja':
    total=int(input('Hva er totalbeløpet på eiendommen? '))
    brutto=int(input('Hvor mye bruttolønn har du i året? '))
    ek=int(input('Hvor mye egenkapital har du? '))

    egenkap=(15/100)*total
    lanbelop=total-ek
    print()

    if lanbelop<=(brutto*5) and egenkap<=ek:
        print('Lånet innvilges.')
    else:
        if (brutto*5)<lanbelop:
            print('Du har for lite bruttolønn.')
        if ek<egenkap:
            print('Du har får lite egenkapital.')
    print()        
    fortsett=input('Skriv "ja" om du vil beregne på nytt, eller "nei" dersom du vil avslutte kalkulatoren: ')

    #if fortsett=="ja":
       # beregn=True
    #if fortsett!="ja" or fortsett=="nei":
       # beregn=False
