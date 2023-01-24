#Program for å skrive tre navn til en ny fil

#FØRSTE TRINN: Definerer og åpner fila student.txt
studentfil=open('student.txt','w') #W=write

#ANDRE TRINN: Skriver 3 navn til fila
#Hver tekstsreng (navn) slutter med: \n
studentfil.write('Torvald\n')
studentfil.write('Kari\n')
studentfil.write('Jens\n')

#TREDJE TRINN: Stenger fila
studentfil.close()
