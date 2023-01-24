#Program for å lese navn for navn og skrive ut de navnene som passer med "søkekriterie"
#Generell fremgangsmåte jfr. figur 6-17 og program 6-9

#Åpner fila student.txt
studentfil=open('student.txt','r')

#Leser første linje i fila ved bruk av readline-metoden
student=studentfil.readline()

#I Python, readline returnerer en tom streng ('') når den leser end-of-file(eof) merket,
#da tester vi på det


while student!='':
    if student[0]=='O':
        print(student.rstrip('\n'))#Tar bort linjeskift, altså ingen mellomrom i utskrift
    #leser neste linje i fila
    student=studentfil.readline()

#stenger fila
studentfil.close()

#Prøv selv: Ta bort linjeskift; Det kalles for rstrip
