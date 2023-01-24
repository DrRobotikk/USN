#Program for å lese en hel fil på en gang

#Åpner fila student.txt
studentfil=open('student.txt','r') #r=read

#Leser filens innhold
filinnhold=studentfil.read()

#Stenger fila
studentfil.close()

#Skriver ut innholdet i fila som har blitt lest inn i minnet
print(filinnhold)
