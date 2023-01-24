#Delprogram for registrering av studenter:

def registrer():
    ny_student='ja'

    while ny_student=='ja':

        funnet=False
        lete=input('Skriv inn studentnummer: ')
        studentfil=open('student.txt','r')
        studentnr=studentfil.readline()
        
        while studentnr!='':
            studentnr=studentnr.rstrip('\n')
            fornavn=studentfil.readline().rstrip('\n')
            etternavn=studentfil.readline().rstrip('\n')
            studium=studentfil.readline().rstrip('\n')
            if studentnr==lete:
                print('Studenten finnes fra før.')
                print()
                funnet=True
            
            studentnr=studentfil.readline()
        studentfil.close()
        if funnet==False:
            studentfil=open('student.txt','a')
            fornavn=input('Skriv inn studentens fornavn: ')
            etternavn=input('Skriv inn studentens etternavn: ')
            studium=input('Skriv inn studentens studium: ')

            #Legger opplysninger i fila
            studentfil.write(lete+'\n')
            studentfil.write(fornavn+'\n')
            studentfil.write(etternavn+'\n')
            studentfil.write(studium+'\n')
            print('Lista er blitt oppdatert')
            print()
        #Legg til flere studenter
        ny_student=input('Vil du legge til flere studenter? (ja/nei) ')
        
    studentfil.close()
registrer()