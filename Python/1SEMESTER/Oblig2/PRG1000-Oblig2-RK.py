#Delprogram for registrering av nye studenter:
def registrer():
    ny_student='ja'
    while ny_student=='ja':
        funnet=False
        lete=input('Skriv inn studentnummeret til studenten som skal registreres: ')
        studentfil=open('student.txt','r')
        studentnr=studentfil.readline()
        
        while studentnr!='':
            studentnr=studentnr.rstrip('\n')
            fornavn=studentfil.readline().rstrip('\n')
            etternavn=studentfil.readline().rstrip('\n')
            studium=studentfil.readline().rstrip('\n')
            if studentnr==lete:
                print('Studenten ligger i lista fra før.')
                funnet=True
            studentnr=studentfil.readline()
        studentfil.close()
        
        if funnet==False:
            studentfil=open('student.txt','a')
            fornavn=input('Skriv inn studentens fornavn: ')
            etternavn=input('Skriv inn studentens etternavn: ')
            studium=input('Skriv inn studentens studium: ')

            studentfil.write(lete+'\n')
            studentfil.write(fornavn+'\n')
            studentfil.write(etternavn+'\n')
            studentfil.write(studium+'\n')
            print('Studentlista er blitt oppdatert')
        print()  
        ny_student=input('Vil du legge til flere studenter? (ja/nei) ')
    studentfil.close()

    
#Delprogram for sletting av studenter:
def sletting():
    ny_student='ja'
    while ny_student=='ja':
        import os
        funnet=False
        funnet_student=False
        slett=input('Skriv inn studentnummeret på studenten som skal slettes: ')
        eksamensresultatfil=open('eksamensresultat.txt','r')
        emnekode=eksamensresultatfil.readline()

        while emnekode!='':
            emnekode=emnekode.rstrip('\n')
            studentnr=(eksamensresultatfil.readline().rstrip('\n'))
            resultat=(eksamensresultatfil.readline().rstrip('\n'))
            if studentnr==slett:
                funnet=True
            emnekode=eksamensresultatfil.readline()
        eksamensresultatfil.close()
        
        if funnet==False:
            studentfil=open('student.txt','r')
            studnr=studentfil.readline()
            while studnr!='':
                studnr=studnr.rstrip('\n')
                if studnr==slett:
                    funnet_student=True
                studnr=studentfil.readline()
            studentfil.close()

        if funnet==False and funnet_student==True:
            studentfil=open('student.txt','r')
            midlertidigfil=open('midlertidig.txt','w')
            studentnr=studentfil.readline()
            while studentnr!='':
                studentnr=studentnr.rstrip('\n')
                fornavn=(studentfil.readline().rstrip('\n'))
                etternavn=(studentfil.readline().rstrip('\n'))
                studium=(studentfil.readline().rstrip('\n'))
                if studentnr!=slett:
                    midlertidigfil.write(studentnr+'\n')
                    midlertidigfil.write(fornavn+'\n')
                    midlertidigfil.write(etternavn+'\n')
                    midlertidigfil.write(studium+'\n')
                studentnr=studentfil.readline()
             
            studentfil.close()
            midlertidigfil.close()
            os.remove('student.txt')
            os.rename('midlertidig.txt','student.txt')
            print('Studenten er blitt slettet fra lista.')
        elif funnet==False:
            print('Studenten finnes ikke i lista.')
        else:
            print('Studenten kan ikke slettes da han har gyldig eksamenskarakter.')
        print()    
        ny_student=input('Vil du slette flere studenter? (ja/nei) ')


#Delprogram for eksamensresultatutskrift:
def karakter():
    ny_utskrift='ja'
    while ny_utskrift=='ja':
        funnet=False
        utskrift=input('Skriv inn studentnummer til studenten du ønsker å se karakterene til: ')
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
        ny_utskrift=input('Ønsker du en utskrift for ny student? (ja/nei) ')


#Delprogram for hovedmenyen:
def main():
    valg=True
    while valg==True:
        print('Meny:')
        print('1. Legg til ny student')
        print('2. Slette en student')
        print('3. Se eksamensresultater')
        valg=input('Velg et program: ')

        if valg=='1':
            registrer()
            valg=True
        if valg=='2':
            sletting()
            valg=True
        if valg=='3':
            karakter()
            valg=True
main()
