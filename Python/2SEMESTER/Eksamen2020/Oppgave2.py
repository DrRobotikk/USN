#OPPGAVE 2:
#Les all informasjon om bilene inn i en to-dimensjonal dictionary 
#skriv ut merke, modell og startdato for en bestemt bil
#når programmet spør brukeren om å oppgi regnr. 
#Programmet skal kjøres så lenge brukeren ønsker.

fortsette='ja'
while fortsette=='ja':

    bil={}

    bilfil=open('bil.txt','r',encoding='utf-8')

    regnr=bilfil.readline()
    while regnr!='':
        regnr=regnr.rstrip('\n')
        merke=bilfil.readline().rstrip('\n')
        modell=bilfil.readline().rstrip('\n')
        startdato=bilfil.readline().rstrip('\n')
        posisjon=bilfil.readline().rstrip('\n')

        bil[regnr]={'merke':merke,'modell':modell,'startdato':startdato,'posisjon':posisjon}
        regnr=bilfil.readline()
    bilfil.close()

    regNr=input('Oppgi regnr: ')
    reg=regNr.upper()

    print(bil[reg]['merke'],bil[reg]['modell'],bil[reg]['startdato'])
    
    fortsette=input('Ønsker du flere utskrifter? ')
