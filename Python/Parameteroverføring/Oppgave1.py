#Delprogrammet som leser inn info om studenten inni i en liste
def lagListe():
    
    studentliste=[]

    fortsett= 'ja'
    while fortsett == 'ja':
        studnr=int(input('Oppgi studentnr: '))
        fnavn=input('Oppgi fornavn: ')
        studium=input('Oppgi studium: ')

        gyldig=False

        while not gyldig:
            if studium=='it' or studium=='økad' or studium=='jus':
                studentliste+=[studnr,fnavn,studium]
                print(studentliste)
                gyldig=True
            else:
                studium=input('Oppgi rett studium: ')

        fortsett=input('Fortsette?')

    return studentliste

#Delprogram som spør om studentnr og skriver ut tabell med info om denne studenten
def studentInfo(studentliste):

    tabell=[]
    funnet=True
    funnetStudent=True

    while funnet:

        nr= int(input('Oppgi studnr på studenten: '))

        for i in range(0,len(studentliste),1):
            if nr==studentliste[i]:
                tabell+=[studentliste[i],studentliste[i+1],studentliste[i+2]]
                funnetStudent=True
            else:
                funnet=False
                
    if funnetStudent==True:
        print(tabell)
    else:
        print('Studenten finnes ikke')
        
    
#Hovedprogrammet som henter inn parametrene fra tidligere delprogrammer
def main():

    #Kjører først funksjonen lagListe!
    listeStudent=lagListe()
    
    #Kaller så funksjonen studentInfo som opererer
    #med parameteren studentliste
    studentInfo(listeStudent)
    

main()

    
