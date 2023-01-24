#PRG1100-2022-objekt med flere atributter

#Objekter med flere dataattributter

class Student:
    def __init__(self,studentnr,fornavn,etternavn,epost,studium):
        self.__studentnr=studentnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
        self.__studium=studium

    #__str__metoden, holder orden på "an object's state",
    #dvs verdien på atributtene
    def __str__(self):
        return 'Objektets attributter er: '+'\n' + self.__studentnr + '\n' + self.__fornavn + '\n' + self.__etternavn + '\n' + self.__epost + '\n' + self.__studium

studentnr=input('Oppgi studentnr: ')
fornavn=input('Oppgi fornavn: ')
etternavn=input('Oppgi etternavn: ')
epost=input('Oppgi epost: ')
studium=input('Oppgi studium: ')

ny_student=Student(studentnr,fornavn,etternavn,epost,studium)

#Skriver ut verdiene til attributtene til objektet ny_student
#__str__ kalles ved å sende et objekt som argument til print-funksjonen
print()
print(ny_student)
