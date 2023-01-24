#Lag en liste med fornavn som input
#det skal spørres om man skal lese inn flere navn
#det skal leses inn nye fornavn så lenge man svarer "ja"
#ved "nei" skal programmet skrive ut lista med fornavn, samt reversert liste (s.402)

navnliste=[]
start=True


while start:
    #print('Navnliste til nå er:',navnliste)
    print()
    navn=input('Skriv inn fornavn: ')
    navnliste+=[navn]
    nytt_navn=input('Vil du skrive inn flere fornavn? Skriv "ja" eller "nei"')
    if nytt_navn=="ja":
        start=True
    if nytt_navn=="nei" or nytt_navn!="ja":
        start=False
        print(navnliste)
        navnliste.reverse()
        print('Lista baklengs er: ',navnliste)
            
    
