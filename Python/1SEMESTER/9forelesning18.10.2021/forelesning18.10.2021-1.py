#Legge poster til fil (variabel + '\n')

nystudent='j'

studentfil=open('studentene.txt','a')

while nystudent=='j':
    #Tar imot opplysninger om studenten
    studentnr=input('Oppgi studentnummer: ')
    fornavn=input('Oppgi fornavn på studenten: ')
    studium=input('Oppgi studium: ')

    #Skriver studentopplysninger til fil
    studentfil.write(studentnr+'\n')
    studentfil.write(fornavn+'\n')
    studentfil.write(studium+'\n')

    #Legge til ny student
    nystudent=input('Vil du legge til flere studenter? (j/n) ')

studentfil.close()
