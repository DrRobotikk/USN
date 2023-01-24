#OPPGAVE 1:
#Lag et program som leser all informasjon om kundene
#inn i en to-dimensjonal liste, og som skriver ut 
#mobilnr, fornavn og etternavn ved en gjennomgang av lista. 

#oppretter en tom liste
kundeliste=[]

#åpner kundefila og går gjennom alle linjene i hver post
kundefil=open('kunde.txt','r',encoding='utf-8')
tlf=kundefil.readline()
while tlf!='':
    tlf=tlf.rstrip('\n')
    fornavn=kundefil.readline().rstrip('\n')
    etternavn=kundefil.readline().rstrip('\n')
    kortnr=kundefil.readline().rstrip('\n')

    #legger alle linjene i en todimmensjonal liste
    kundeliste+=[[tlf,fornavn,etternavn,kortnr]]
    tlf=kundefil.readline()
kundefil.close()

#oppretter en løkke som går gjennom den todimmensjonale lista
for n in range(0,len(kundeliste),1):
    print(kundeliste[n][0],kundeliste[n][1],kundeliste[n][2])
    #her vil den printe ut tlf, fornavn og etternavn for hver kunde
    


