#program for å lete etter informasjon som matcher med input i kaffefila


funnet=False
lete=input('Skriv inn kaffetype du ønsker å finne: ')
kaffefil=open('kaffe.txt','r')
kaffetype=kaffefil.readline()

while kaffetype!='':
    mengde=kaffefil.readline()
    kaffetype=kaffetype.rstrip('\n')
    if kaffetype==lete:
        print('Kaffetype:',kaffetype)
        print('Mengde:',mengde)
        print()
        funnet=True

    kaffetype=kaffefil.readline()

kaffefil.close()
if funnet==False:
    print('Kaffetype finnes ikke i databasen')

