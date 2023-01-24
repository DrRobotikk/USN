#Program for å endre på innholdet "mengde" i kaffefila

import os

#def main():
funnet=False
lete=input('Oppgi kaffetype: ')
ny_mengde=input('Oppgi ny mengde kaffe: ')

kaffefil=open('kaffe.txt','r')

tempfil=open('temp.txt','w')

kaffetype=kaffefil.readline()

while kaffetype!='':
    mengde=(kaffefil.readline())

    kaffetype=kaffetype.rstrip('\n')

    if kaffetype==lete:
        tempfil.write(kaffetype+'\n')
        tempfil.write(ny_mengde+'\n')
        funnet=True
    else:
        tempfil.write(kaffetype+'\n')
        tempfil.write(mengde+'\n')

    kaffetype=kaffefil.readline()
kaffefil.close()
tempfil.close()

os.remove('kaffe.txt')

os.rename('temp.txt','kaffe.txt')

if funnet==True:
    print('Kaffefila har blitt oppdatert')
else:
    print('Kaffetypen ble ikke funnet i fila')
#main()
