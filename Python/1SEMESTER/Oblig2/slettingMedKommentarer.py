def sletting():
    ny_student='ja'
    while ny_student=='ja':
        import os
        funnet=False
        funnet_student=False

        slett=input('Skriv inn studentnr på studenten du ønsker å slette: ')
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
        #har vi ikke funnet studenten i eksamensresultat.txt sjekker vi student.txt først 
        if funnet==False:
            studentfil=open('student.txt','r')
            studnr=studentfil.readline()

            while studnr!='':
                studnr=studnr.rstrip('\n')
                if studnr==slett:
                    funnet_student=True
                studnr=studentfil.readline()
            studentfil.close()
                
        #har vi IKKE funnet studenten i eksamensresultat.txt OG funnet studenten i student.txt
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
            print('Studenten er blitt flettet fra lista')
        elif funnet==False:
            print('Studenten finnes ikke i lista')
            
        else:
            print('Studenten kan ikke slettes, da han har gyldig eksamenskarakter.')
        ny_student=input('Vil du slette flere studenter? (ja/nei) ')
sletting()
