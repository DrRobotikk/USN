def heleLista():
    student=[]
    print('Studentene i lista hittil er:',student)
    print()

    studentfil=open('student.txt','r',encoding='utf-8')

    snummer=studentfil.readline()
    while snummer!='':
        snummer=snummer.rstrip('\n')
        fornavn=studentfil.readline().rstrip('\n')
        etternavn=studentfil.readline().rstrip('\n')
        epost=studentfil.readline().rstrip('\n')
        fdato=studentfil.readline().rstrip('\n')
        kjonn=studentfil.readline().rstrip('\n')
        studium=studentfil.readline().rstrip('\n')

        #Legger linjene fra tekstfila inni lista "ansatte"
        student+=[[snummer,fornavn,etternavn,epost,fdato,kjonn,studium]]

        snummer=studentfil.readline()
    studentfil.close()

    print(student)
