#program som viser data i kaffefil

kaffefil=open('kaffe.txt','r')

#Les første informasjon i lista
kaffetype=kaffefil.readline()

while kaffetype!='':
    mengde=(kaffefil.readline().rstrip('\n'))
    #kaffetype=kaffetype.rstrip('/n')
    #mengde=mengde.rstrip('\n')

    print('Kaffetype:',kaffetype.rstrip('\n'))#fjerner linjeskift
    print('Mengde:', mengde)

    kaffetype=kaffefil.readline()
    
kaffefil.close()


