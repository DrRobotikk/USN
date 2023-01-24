#PRG1100-2022-binærlagring av objekter

#Importerer pickle-modulen for å serialisere/ konvertere et objekt
#til en bit-strøm som kan lagres til fil for senere henting/bruk

import pickle

class Student:
    
    def __init__(self,studentnr,fornavn,etternavn,epost,studium):
        self.__studentnr=studentnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
        self.__studium=studium

    def set_studentnr(self,studentnr):
        self.__studentnr=studentnr

    def set_fornavn(self,fornavn):
        self.__fornavn=fornavn

    def set_etternavn(self,etternavn):
        self.__etternavn=etternavn

    def set_epost(self,epost):
        self.__epost=epost

    def set_studium(self,studium):
        self.__studium=studium

    def get_studentnr(self):
        return self.__studentnr

    def get_fornavn(self):
        return self.__fornavn

    def get_etternavn(self):
        return self.__etternavn

    def get_epost(self):
        return self.__epost

    def get_studium(self):
        return self.__studium

    def __str__(self):
        return 'Objektets attributter er: '+'\n' + self.__studentnr + '\n' + self.__fornavn + '\n' + self.__etternavn + '\n' + self.__epost + '\n' + self.__studium


studentnr=input('Oppgi studentnr: ')
fornavn=input('Oppgi fornavn: ')
etternavn=input('Oppgi etternavn: ')
epost=input('Oppgi epost: ')
studium=input('Oppgi studium: ')

ny_student=Student(studentnr,fornavn,etternavn,epost,studium)

#kontrollprint
print(ny_student)

#Skriver ut epost og studium for så å endre de
print()
print(ny_student.get_epost())
print(ny_student.get_studium())
epost=input('Oppgi ny epost: ')
ny_student.set_epost(epost)
studium=input('Oppgi nytt studium: ')
ny_student.set_studium(studium)
print()
print(ny_student)

#Nytt, serialisering og skriving av objektet til fil
#Åpner en fil for binær skriving
#ikke bruk encoding her- binary mode doesn't take an encoding argument
studentfil=open('student.dat','wb')

#pickler av objektet og lagrer på fil
pickle.dump(ny_student,studentfil)

#Lukker fila
studentfil.close()























