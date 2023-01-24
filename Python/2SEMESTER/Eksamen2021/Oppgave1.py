#Oppgave 1:
#Lag et program som leser all informasjon om kundene
#inn i en to-dimensjonal liste, og som skriver ut 
#mobilnr, fornavn og etternavn ved en gjennomgang av lista.

kundeliste=[]

kundefil=open('kunde.txt','r',encoding='utf-8')

mobilnr=kundefil.readline()

while mobilnr!='':
    mobilnr=mobilnr.rstrip('\n')
    fornavn=kundefil.readline().rstrip('\n')
    etternavn=kundefil.readline().rstrip('\n')
    epost=kundefil.readline().rstrip('\n')

    kundeliste+=[[mobilnr,fornavn,etternavn,epost]]

    mobilnr=kundefil.readline()
kundefil.close()

for n in range(len(kundeliste)):
    print(kundeliste[n][0],kundeliste[n][1],kundeliste[n][2])
