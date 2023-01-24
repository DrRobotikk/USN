


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
        funnet=False
        studentNr=input('Skriv inn studentnummer: ')
        studentfil=open('student.txt','r')
        studentnr=studentfil.readline()
        
        while studentnr!='':
            studentnr=studentnr.rstrip('\n')
            fornavn=studentfil.readline().rstrip('\n')
            etternavn=studentfil.readline().rstrip('\n')
            studium=studentfil.readline().rstrip('\n')
            if studentnr==studentNr:
                print('Studenten finnes fra før.')
                print()
                funnet=True
            
            studentnr=studentfil.readline()
        studentfil.close()
        if funnet==False:
            print('Student finnes ikke')

        if funnet==True:
            skriv_karakterliste(studentNr)
        ny_utskrift=input('Ny utskrift? ')
main()
