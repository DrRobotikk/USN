#tekstfil fornavn.txt
#leser navnene inn i en 1-dimensjonal tabell, linje for linje
#navnene i lista sorteres fra A til Å
#sortert liste skrives til ny fil, navn for navn fra lista
#Versjon 1: boblesortering
#Versjon 2: innstikksortering

usortert=[]
fornavnfil=open('fornavn.txt','r',encoding='utf-8')
navn=fornavnfil.readline()
while navn!='':
    navn=navn.rstrip('\n')

    usortert+=[navn]
    navn=fornavnfil.readline()
fornavnfil.close()
print('Den usorterte tabellen er',usortert)

bytte=True
s=1

for index in range(1,len(usortert),1):                                                #GÅR GJENNOM USORTERT LISTE, BEGYNNER PÅ 1 OG GÅR MED ETT STEG OM GANGEN
    print('Kort nr.',index+1,'med verdi',usortert[index])                             #PRINTER KORT-NUMMER OG VERDIEN PÅ KORTET, EKS. KORT NR 2 MED VERDI 3
    stopp_merke=index                                                              #DEFINERER STOPPMERKET TIL ER LIK INDEX
    flytt=0                                                                        #VARIABEL FOR Å FÅ RIKTIG PRINT MTP HVOR MANGE GANGER KORTET SKAL FLYTTES

    while stopp_merke>0 and (usortert[stopp_merke-1]>usortert[stopp_merke]):
        bytte=usortert[stopp_merke]
        usortert[stopp_merke]=usortert[stopp_merke-1]
        usortert[stopp_merke-1]=bytte
        stopp_merke=stopp_merke-1
        flytt=flytt+1
        print('flyttes',flytt,'gang(er) til venstre og resultatet blir',usortert)
        #print(liste)


sortert1fil=open('sortert1.txt','w',encoding='utf-8')

for index in range(0,len(usortert),1):
    sortert1fil.write(usortert[index]+'\n')
    

sortert1fil.close()
