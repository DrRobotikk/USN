#Program for å lese linjer fra tekstfil inn i ei liste
#Lager meg en løkke først for å kunne kjøre programmet så lenge jeg ønsker
fortsette='ja'
while fortsette=='ja':
    #Lager ei tom liste
    #Åpner så tekstfila oppbevaringsfil.txt og leser første linje
    oppbevaring_liste=[]
    oppbevaringsfil=open('oppbevaring.txt','r')
    tlf=oppbevaringsfil.readline()

    while tlf!='':
        #leser resten av linjene i posten med rstrip
        tlf=tlf.rstrip('\n')
        regnr=oppbevaringsfil.readline().rstrip('\n')
        innlevert=oppbevaringsfil.readline().rstrip('\n')
        utlevert=oppbevaringsfil.readline().rstrip('\n')
        hylle=oppbevaringsfil.readline().rstrip('\n')
        pris=oppbevaringsfil.readline().rstrip('\n')
        
        #Legger info fra tekstfila inn i lista
        oppbevaring_liste+=[tlf, regnr, innlevert, utlevert, hylle, pris]
        
        #Leser første linje i neste post i tekstfila og stenger så tekstfila
        tlf=oppbevaringsfil.readline()
    oppbevaringsfil.close()
    print()#Tom print for mellomrom
    
    #Input for å kunne søke på mobilnr i lista
    mobil=input('Oppgi ditt mobilnr: ')
    
    #Lager en forløkke der jeg sammenligner input med data i lista
    #Om dataene stemmer, skriver jeg ut den posten i ei liste
    for index in range(0,len(oppbevaring_liste),1):
        if mobil==oppbevaring_liste[index]:
            print(oppbevaring_liste[index],oppbevaring_liste[index+1],oppbevaring_liste[index+2],oppbevaring_liste[index+3])
    fortsette=input('Ønsker du en ny utskrift? (ja/nei) ')
