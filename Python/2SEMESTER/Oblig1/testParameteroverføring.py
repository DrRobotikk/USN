#PRG1100-Oblig1-RK

#Delprogram for å lese inn poster fra tekstfil til todimmensjonal liste.
def usortert_liste():
    usortert=[]

    varefil=open('Varer.txt','r',encoding='utf-8')
    varenr=varefil.readline()

    while varenr!='':
        varenr=varenr.rstrip('\n')
        betegnelse=varefil.readline().rstrip('\n')
        pris=varefil.readline().rstrip('\n')
        kategori=varefil.readline().rstrip('\n')
        hylle=varefil.readline().rstrip('\n')

        usortert+=[[varenr,betegnelse,pris,kategori,hylle]]
        
        varenr=varefil.readline()
    varefil.close()
    liste_lengde=len(usortert)

    #parameteroverføring av 2 variabler
    return usortert, liste_lengde


#Delprogram for å skrive ut alle varer og hylleplass.
#denne måten å hente inn parametrene på gjør at den kun henter inn usortert liste og listelengde uten å kjøre den første defen på nytt
#parameteroverføring ved å navngi parameteren slik:
# ny_usortert,listelengde=usortert_liste()
#gjør at defen kjøres på nytt for hver gang programmet kjøres

def skriv_alle_varer(skriv_alle_varerNy_usortert,skriv_alle_varerListelengde):
    for r in range(skriv_alle_varerListelengde):
        print(skriv_alle_varerNy_usortert[r][1],'ligger i hylle', skriv_alle_varerNy_usortert[r][4])

#Delprogram for å skrive ut varer som ikke er hylleplassert.
def ikke_hylleplassert(ikke_hylleplassertNy_usortert,ikke_hylleplassertListelengde):

    for r in range(ikke_hylleplassertListelengde):
        if ikke_hylleplassertNy_usortert[r][4].upper()=='NULL':
            print(ikke_hylleplassertNy_usortert[r][1],'er ikke hylleplassert')

#Delprogram for å skrive ut varer etter brukeroppgitt initial.
def skriv_initialer(skriv_initialerNy_usortert,skriv_initialerListelengde):
    lete=input('Skriv inn forbokstaven på vare du øsnker utskrift for: ')
    for r in range (skriv_initialerListelengde):
        if skriv_initialerNy_usortert[r][1][0:1].upper()==lete.upper():
            print(skriv_initialerNy_usortert[r][1],'begynner på bokstaven',lete)

#Delprogram for å skrive ut varer i en brukeroppgitt kategori.
def oppgi_kategori(oppgi_kategoriNy_usortert,oppgi_kategoriListelengde):
    lete=input('Oppgi ønsket kategori for vareutskrift: ')
    summen=0
    for r in range(oppgi_kategoriListelengde):
        if oppgi_kategoriNy_usortert[r][3].upper()==lete.upper():
            print(oppgi_kategoriNy_usortert[r][1],'finnes i kategori',lete)
            summen+=1
    print('Summen blir da',summen)

#Delprogram for å skrive ut varer i intervallet [100,200].
def skriv_intervall(skriv_intervallNy_usortert,skriv_intervallListelengde):
    for r in range(skriv_intervallListelengde):
        if int(skriv_intervallNy_usortert[r][2])>=100 and int(skriv_intervallNy_usortert[r][2])<=200:
            print(skriv_intervallNy_usortert[r][1],'koster',skriv_intervallNy_usortert[r][2])

#Delprogram for å sortere den usorterte lista og skrive den så
#inn i tekstfila SortertFil.txt.
def sorter_liste(sorter_listeNy_usortert,sorter_listeListelengde):
    bytte=True
    s=1

    #Selve koden for å sortere den todimensjonale lista.
    while bytte==True:
        bytte=False
        for r in range(sorter_listeListelengde-s):

            if sorter_listeNy_usortert[r][1]>sorter_listeNy_usortert[r+1][1]:
                byttet=sorter_listeNy_usortert[r]
                sorter_listeNy_usortert[r]=sorter_listeNy_usortert[r+1]
                sorter_listeNy_usortert[r+1]=byttet
                bytte=True
    s+=1

    #Her oppretter jeg tekstfila som den todimensjonale lista skal skrives inn i.
    sortertfil=open('SortertVare.txt','w',encoding='utf-8')

    for r in range(sorter_listeListelengde):
        sortertfil.write(sorter_listeNy_usortert [r][0]+'\n')
        sortertfil.write(sorter_listeNy_usortert [r][1]+'\n')
        sortertfil.write(sorter_listeNy_usortert [r][2]+'\n')
        sortertfil.write(sorter_listeNy_usortert [r][3]+'\n')
        sortertfil.write(sorter_listeNy_usortert [r][4]+'\n')

    sortertfil.close()
    print(sorter_listeNy_usortert)

#Delprogram for hovedmenyen.
#Her blir parameteroverføringen hentet inn.
def main():
    les_inn=True

    valg='ja'
    while valg=='ja':

        while les_inn:
            ny_usortert,listelengde=usortert_liste()
            les_inn=False
        
        print()
        print('Meny:')
        print('1. Alle varer og hylleplass(dvs betegnelse/varenavn og hylle)')
        print('2. Alle varer som ikke er hylleplassert, dvs har verdien "NULL" i feltet hylle')
        print('3. Alle varer med varenavn som begynner på en brukeroppgitt forbokstav')
        print('4. Alle varer i en brukeroppgitt kategori, med opptelling av antall varer')
        print('5. Alle varer som har en pris i intervallet [100,200] kr')
        print('6. Sorter den usorterte lista og opprett en ny tekstfil ved navn SortertVare.txt')
        print()
        valg=input('Oppgi tallet på programmet du ønsker å kjøre: ')

        if valg=='1':
            skriv_alle_varer(ny_usortert,listelengde)
            valg='ja'
        if valg=='2':
            ikke_hylleplassert(ny_usortert,listelengde)
            valg='ja'
        if valg=='3':
            skriv_initialer(ny_usortert,listelengde)
            valg='ja'
        if valg=='4':
            oppgi_kategori(ny_usortert,listelengde)
            valg='ja'
        if valg=='5':
            skriv_intervall(ny_usortert,listelengde)
            valg='ja'
        if valg=='6':
            sorter_liste(ny_usortert,listelengde)
            valg='ja'
            les_inn=True
#Feilhåndtering ift. om tekstfila finnes eller ikke
try:
    main()
except IOError:
    print('Fila du prøver å åpne finnes ikke.')
