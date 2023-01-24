# Global kode som henter verdier fra Varer.txt
# og legger de inn i en 2-dimensjonal usortert liste

#delprogram for å lese inn poster fra tekstfil til todimmensjonal liste
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
    lengde=len(usortert)
    return usortert,lengde


#Delprogram for å skrive ut alle varer og hylleplass
def alle_varer():
    ny_usortert,liste_lengde=usortert_liste()
    for r in range(liste_lengde):
        print(ny_usortert[r][1],'ligger i hylle', ny_usortert[r][4])

def ikke_hylleplassert():
    ny_usortert,liste_lengde=usortert_liste()
    for r in range(liste_lengde):
        if ny_usortert[r][4].upper()=='NULL':
            print(ny_usortert[r][1],'er ikke hylleplassert')

def initialer():
    ny_usortert,liste_lengde=usortert_liste()
    lete=input('Skriv inn forbokstaven på vare du øsnker utskrift for: ')
    for r in range (liste_lengde):
        if ny_usortert[r][1][0:1].upper()==lete.upper():
            print(ny_usortert[r][1],'begynner på bokstaven',lete)

def brukeroppgitt_kategori():
    ny_usortert,liste_lengde=usortert_liste()
    lete=input('Oppgi ønsket kategori for vareutskrift: ')
    summen=0
    for r in range(liste_lengde):
        if ny_usortert[r][3].upper()==lete.upper():
            print(ny_usortert[r][1],'finnes i kategori',lete)
            summen+=1
    print(summen)

def pris_intervall():
    ny_usortert,liste_lengde=usortert_liste()
    for r in range(liste_lengde):
        if int(ny_usortert[r][2])>=100 and int(ny_usortert[r][2])<=200:
            print(ny_usortert[r][1],'koster',ny_usortert[r][2])

def sortert_liste():
    ny_usortert,liste_lengde=usortert_liste()
    bytte=True
    s=1

    while bytte==True:
        bytte=False
        for r in range(liste_lengde-s):

            if ny_usortert[r]>ny_usortert[r+1]:
                byttet=ny_usortert[r]
                ny_usortert[r]=ny_usortert[r+1]
                ny_usortert[r+1]=byttet
                bytte=True
        s+=1
    #print(usortert)

    sortertfil=open('sortertVare.txt','w',encoding='utf-8')

    for r in range(liste_lengde):
        sortertfil.write(ny_usortert [r][0]+'\n')
        sortertfil.write(ny_usortert [r][1]+'\n')
        sortertfil.write(ny_usortert [r][2]+'\n')
        sortertfil.write(ny_usortert [r][3]+'\n')
        sortertfil.write(ny_usortert [r][4]+'\n')

    sortertfil.close()

def main():
    valg=True
    while valg==True:
        print()
        print('Meny:')
        print('1. Alle varer og hylleplass(dvs betegnelse/varenavn og hylle')
        print('2. Alle varer som ikke er hylleplassert, dvs har verdien "NULL" i feltet hylle')
        print('3. Alle varer med varenavn som begynner på en brukeroppgitt forbokstav')
        print('4. Alle varer i en brukeroppgitt kategori, med opptelling av antall varer')
        print('5. Alle varer som har en pris i intervallet [100,200] kr')
        print('6. Sorter den usorterte lista g opprett en ny tekstfil ved navn sortertVare.txt')
        print()
        valg=input('Oppgi tallet på programmet du ønsker å kjøre: ')

        if valg=='1':
            alle_varer()
            valg=True
        if valg=='2':
            ikke_hylleplassert()
            valg=True
        if valg=='3':
            initialer()
            valg=True
        if valg=='4':
            brukeroppgitt_kategori()
            valg=True
        if valg=='5':
            pris_intervall()
            valg=True
        if valg=='6':
            sortert_liste()
            valg=True
try:
    main()
except IOError:
    print('Fila finnes ikke.')
