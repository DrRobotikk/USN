#PRG1100-2022-innstikksortering - pseudo
#Program for å innstikksortere en usortert liste

#Pseudokode på algoritmen fra https://en.wikipedia.org/wiki/Insertion_sort

#for i ← 1 to length(A) DER I ER LIK INDEX OG A ER LIK LISTE
#    j ← i              DER J ER LIK STOPPMERKE
#    while j > 0 and A[j-1] > A[j]
#        swap A[j] and A[j-1]
#        j ← j - 1
#    end while
#end for

liste=[5,3,1,2,4]                                                                  #OPPRETTER EN USORTERT LISTE/ KORT-LISTE
print(liste)                                              #PRINTER UT LISTA FØR SORTERING

for index in range(1,len(liste),1):                                                #GÅR GJENNOM USORTERT LISTE, BEGYNNER PÅ 1 OG GÅR MED ETT STEG OM GANGEN
    print()
    print('Vi tar et "kort"')
    print()
    print('Kort nr.',index+1,'med verdi',liste[index])                             #PRINTER KORT-NUMMER OG VERDIEN PÅ KORTET, EKS. KORT NR 2 MED VERDI 3
    stopp_merke=index                                                              #DEFINERER STOPPMERKET TIL ER LIK INDEX
    flytt=0                                                                        #VARIABEL FOR Å FÅ RIKTIG PRINT MTP HVOR MANGE GANGER KORTET SKAL FLYTTES

    while stopp_merke>0 and (liste[stopp_merke-1]>liste[stopp_merke]):
        bytte=liste[stopp_merke]
        liste[stopp_merke]=liste[stopp_merke-1]
        liste[stopp_merke-1]=bytte
        stopp_merke=stopp_merke-1
        flytt=flytt+1
        print('flyttes',flytt,'gang(er) til venstre og resultatet blir',liste)
        #print(liste)
print()
print('Slutt på FOR-løkka og sortert liste blir',liste)


