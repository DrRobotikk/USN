#Oppgavesett 3-2

#Starter med tom liste
studentliste=[]
print('Studenter til nå er:',studentliste)
print()

ny_student=True

while ny_student:
    studnr=int(input('Oppgi studentnummer: '))
    studentliste+=[studnr]
    fnavn=input('Oppgi fornavn: ')
    studentliste+=[fnavn]
    studiet=input('Oppgi studium: ')
    studentliste+=[studiet]
    print('Studenter til nå er: ',studentliste)
    print()
    #Kan også komme med 3 input med en gang og skrive en felles print med alle tre inputter
    
    #Spør om flere studenter skal registreres
    svar=input('Skal det leses inn flere studenter? ')
    if svar=="nei":
        ny_student=False
        #Kan også lage en løkke for "ja" sette den til true; else=False

#Printer ut lista med studenter
listelengde_student=len(studentliste)
print()
print('Lista med studenter er',studentliste,'og består av',int(listelengde_student/3),'registrerte studenter')
print()

#SØKE ETTER STUDENT PÅ STUDENTNUMMER
studnr=int(input('Oppgi studentnummer på student det skal søkes på '))
funnet=False

for index in range(0,listelengde_student,3):#Siste steppet er lik 3 fordi studnr finnes på hver 3. plass i lista
    if studnr==studentliste[index]:
        funnet=True
        studenten=index

if funnet==True:
    print('Fullstendig informasjon om studenten er: ')
    print('Studentnr:',studentliste[studenten])
    print('Fornavn:',studentliste[studenten+1])
    print('Studium:',studentliste[studenten+2])
else:
    print('Studenten finnes ikke')

    #prøv selv:
    #1) flytte de tre printene inn i for-løkka, alt. løse med while-løkke
    #2) Søke etter studenter på studieprogram












    
