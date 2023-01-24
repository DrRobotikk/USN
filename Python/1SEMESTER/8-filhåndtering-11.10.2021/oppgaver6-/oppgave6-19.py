#Program som sletter informsjon i kaffefila

import os
funnet=False

lete=input('Oppgi kaffetype du ønsker å slette: ')

kaffefil=open('kaffe.txt','r')
tempfil=open('temp.txt','w')

kaffetype=kaffefil.readline()
while kaffetype!='':
    mengde=(kaffefil.readline().rstrip('\n'))
    kaffetype=kaffetype.rstrip('\n')

    if kaffetype!=lete:
        tempfil.write(kaffetype+'\n')
        tempfil.write(mengde+'\n')
    else:
        funnet=True

    kaffetype=kaffefil.readline()
kaffefil.close()
tempfil.close()

os.remove('kaffe.txt')

os.rename('temp.txt','kaffe.txt')

if funnet==True:
    print('Kaffefila har blitt oppdatert')
else:
    print('Kaffetype finnes ikke i lista')

