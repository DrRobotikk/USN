#Laerer.txt med 3 og 3 linjer per post (fornavn, etternavn, epost)
#skriv koden for 2-dimensjonal tabell ed kommentarer for hva som gjør hva

#oppretter en tom liste
ansatte=[]
print('Ansatte i lista hittil er:',ansatte)
print()

ansattfil=open('laerer.txt','r',encoding='utf-8')

fornavn=ansattfil.readline()
while fornavn!='':
    fornavn=fornavn.rstrip('\n')
    etternavn=ansattfil.readline().rstrip('\n')
    epost=ansattfil.readline().rstrip('\n')

    #Legger linjene fra tekstfila inni lista "ansatte"
    ansatte+=[[fornavn,etternavn,epost]]

    fornavn=ansattfil.readline()
ansattfil.close()

#skriver ut lista "ansatte" med linjene fra tesktfila
print('Resultatet ble:',ansatte)
print()

#skriver ut post nummer 5 i lista
print(ansatte[4])
print()

#skriver ut hvor mange poster det finnes i den 2-dimensjonale lista
listelengde=len(ansatte)
print(listelengde)
print()

#her skriver vi ut kun etternavn til alle folka i lista
print('Etternavn:')
#c[0]=første data i posten (fornavn)
#c[1]=andre data i posten  (etternavn)
#c[2]=tredje data i posten (epost)
c=1 #c=colone settes til en( leser kun andre verdi i posten)
for r in range(listelengde):
    print(ansatte[r][c]) #r=row, printer ut row 1,2,3,4,5 osv
                #mens c alltid er 1, altså andre linja i posten
print()

#denne posten skriver ut alle radene (r) og c er fortsatt 1
#[c+1] blir derfor siste dataen i en post, altså eposten
print('Etternavn og epost:')
for r in range(listelengde):
    print(ansatte[r][c],'har epostadresse',ansatte[r][c+1])
print()
