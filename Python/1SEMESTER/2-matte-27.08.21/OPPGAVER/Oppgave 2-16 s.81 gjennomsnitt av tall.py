#Målet med oppgaven er å finne gjennomsnittsresultatet for en gruppe studenter

#begynner med input av test_resultateter

test_resultat1=int(input('Tast inn første testresultatet her: '))
test_resultat2=int(input('Tast inn andre testresultatet her: '))
test_resultat3=int(input('Tast inn tredje testresultatet her: '))

#nå må vi først plusse sammen testresultatene og så må sluttsummen deles på antall test_resultater (3)
gjennomsnitt_resultat=(test_resultat1+test_resultat2+test_resultat3)/3

#utskrift av gjennomsnitt_resultat

print('Gjennomsnittsresultatet for deres gruppe er: ',gjennomsnitt_resultat)
