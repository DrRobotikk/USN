student=[]
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
    student+=[[snummer,fornavn,etternavn,epost,fdato,kjonn,studium]]

    snummer=studentfil.readline()
studentfil.close()
def heleTabell():

    print(student)

def epost():
    c=1
    for r in range(len(student)):
        print((student[r][c]),(student[r][c+1]),(student[r][c+2]))

def damer():
    c=0
    for r in range(len(student)):
        
        if student[r][c+5]=='Kvinne':
            print(student[r][c+5])

def studie():
    c=0
    for r in range(len(student)):
        
        if student[r][c+6]=='Bach IT og IS':
            print((student[r][c]),(student[r][c+1]),(student[r][c+2]),(student[r][c+3]))
def main():
    valg=True
    while valg==True:
        print('Meny:')
        print('1. skriv ut hele lista')
        print('2. fornavn, etternavn og fødselsdato')
        print('3. fornavn, etternavn og epost for alle kvinner')
        print('4. stnr, fornavn, etternavn og kjønn for alle på IT')
        valg=input('Velg et program: ')

        if valg=='1':
            heleTabell()
            valg=True
        if valg=='2':
            epost()
            valg=True
        if valg=='3':
            damer()
            valg=True
        if valg=='4':
            studie()
            valg=True
            
main()
