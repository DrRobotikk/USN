#Delprogram for å sjekke om studenten finnes i student.txt
def sjekk_student():
    funnet=False
    studnr=input('Skriv inn studentnummer: ')
    studentfil=open('student.txt','r')
    studentnr=studentfil.readline()
    
    while studentnr!='':
        studentnr=studentnr.rstrip('\n')
        fornavn=studentfil.readline().rstrip('\n')
        etternavn=studentfil.readline().rstrip('\n')
        studium=studentfil.readline().rstrip('\n')
        if studentnr==studnr:
            print('Studenten finnes fra før.')
            print()
            funnet=True #Når vi har funnet studenten får variabelen funnet en TRUE-verdi
        
        studentnr=studentfil.readline()
    studentfil.close()
    #Vi beholder så verdiene funnet=True og studnr som input
    return funnet,studnr
        
#Delprogram for eksamensresultatutskrift:
def skriv_karakterliste(skriv_karakterlisteStudentnr):
    funnet=False
    utskrift=skriv_karakterlisteStudentnr#input('Skriv inn studentnummer til studenten du ønsker å se karakterene til: ')
    print()
    studentfil=open('student.txt','r')
    studentnr=studentfil.readline()

    while studentnr!='':
        studentnr=studentnr.rstrip('\n')
        fornavn=(studentfil.readline().rstrip('\n'))
        etternavn=(studentfil.readline().rstrip('\n'))
        studium=(studentfil.readline().rstrip('\n'))
        if studentnr==utskrift:
            print(studentnr, fornavn, etternavn, studium)
            funnet=True
        
        if funnet==True:
            eksamensresultatfil=open('eksamensresultat.txt','r')
            emnekode=eksamensresultatfil.readline()
            while emnekode!='':
                emnekode=emnekode.rstrip('\n')
                studentnr_eks=(eksamensresultatfil.readline().rstrip('\n'))
                karakter=(eksamensresultatfil.readline().rstrip('\n'))
                
                if studentnr_eks==studentnr:
                    emnefil=open('emne.txt','r')
                    emnekode_eks=emnefil.readline()
                    
                    while emnekode_eks!='':
                        emnekode_eks=emnekode_eks.rstrip('\n')
                        emnenavn=(emnefil.readline().rstrip('\n'))
                        
                        if emnekode_eks==emnekode:
                            print(emnekode,emnenavn,karakter)
                        emnekode_eks=emnefil.readline()
                    funnet=False
                    emnefil.close()
                emnekode=eksamensresultatfil.readline()
        
            eksamensresultatfil.close()
        studentnr=studentfil.readline()  
    studentfil.close()
    print()


#Delprogram for hovedmenyen:
def main():
    ny_utskrift='ja'
    while ny_utskrift=='ja':
        #Her henter vi inn verdiene fra delprogrammet sjekk_student
        status,studentnr=sjekk_student()
        print('Resultat etter sjekk_student():',status,studentnr)

        #Her tester vi verdien på status
        #dersom den er True, kan vi hente inn funksjonen som skriver ut karakterliste
        if status==True:
            print('Karakterliste skrives ut')
            skriv_karakterliste(studentnr)
        else:
            print('Studenten finnes ikke')
        ny_utskrift=input('Flere utskrifter? ')
main()
