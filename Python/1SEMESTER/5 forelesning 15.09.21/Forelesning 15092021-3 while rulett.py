#Inndatatest i begynnelsen av programmet

#Vi trenger en variabelt til bruk til inndatatest, bolsk variabel
nytt_tall=True

#Løkke som sikrer oss gyldig verdi
while nytt_tall:
    #Brukeren oppgir verdi på ruletten
    tall=int(input('Hva er tallet på ruletten? '))

    #Tester om gyldig verdi er oppgitt
    if tall>=0 and tall<=36:
        print('Gyldig verdi')
        nytt_tall=False
    else:
        print('Ugyldig verdi på ruletten. Skriv inn nytt tall')

print('Da har vi fått gyldig tall på ruletten og kan fortsette programmet med å avgjøre riktig farge')
