#VIKTIG MTP OBLIG 2
#Leser poster fra fil (uten og med 'rstrip')

studentfil=open('studentene.txt','r')

#starter med å lese første linje/ første felt i første post (3 linjer i tekstfil)
studentnr=studentfil.readline()

while studentnr!='':
    studentnr=studentnr.rstrip('\n')
    
    #Leser resten av posten (de to resterende linjene om studenten i posten)
    #Leser inn fornavn og studium og strip i en operasjon
    fornavn=studentfil.readline().rstrip('\n')
    studium=studentfil.readline().rstrip('\n')

    #skriver ut posten
    print(studentnr,fornavn,studium)

    #Leser studentnr til neste student/ neste post
    studentnr=studentfil.readline()

studentfil.close()
