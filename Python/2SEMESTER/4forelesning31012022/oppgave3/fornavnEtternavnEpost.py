#skriv ut fornavn, etternavn og epost for alle studenter
def studie():
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

    c=0
    for r in range(len(student)):
        
        if student[r][c+6]=='Bach IT og IS':
            print((student[r][c]),(student[r][c+1]),(student[r][c+2]),(student[r][c+3]))

studie()

