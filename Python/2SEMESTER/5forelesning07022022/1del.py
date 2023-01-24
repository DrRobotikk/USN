try:
    student={}
    #print('Studentene i lista hittil er:',student)
    #print()

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
        student[snummer]=[fornavn,etternavn,epost,fdato,kjonn,studium]

        snummer=studentfil.readline()
    studentfil.close()
    print(student)
except IOError:
    print('Fila finnes ikke')

def antall_kvinner():
    antall=0
    for key in student:
        
        #Her må man huske på at første verdien i lista er key og er dermed ikke med i tellinga
        #så selv om info om kjønn ligger på sjette plass i lista, så søker vi etter verdien på
        #5 plass altså student[key][4]
        if student[key][4].upper()=='KVINNE':
            print(key,student[key][0])
            antall+=1
    print(antall)
            
antall_kvinner()

def antall_studenter_på_studie():
    antall_it=0
    antall_ok=0
    for key in student:
        #Brakketene med verdi[5:7] vil si at koden kun leser
        #fom det 5 tegnet til det 7 tegnet i posten studium i tekstfila
        if (student[key][5][5:7].upper())=='IT':
            print(student[key][1])
            antall_it+=1

        else:
            print(student[key][1])
            antall_ok=antall_ok+1
    print('Antall it-studenter er:',antall_it)
    print('Antall øk-studenter er:',antall_ok)
antall_studenter_på_studie()





