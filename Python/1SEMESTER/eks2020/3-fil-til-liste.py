fortsette='ja'
while fortsette=='ja':
    
    hundeliste=[]
    hundefil=open('hund.txt','r')
    hundeid=hundefil.readline()

    while hundeid!='':
        hundeid=hundeid.rstrip('\n')
        oppdretterid=hundefil.readline().rstrip('\n')
        eierid=hundefil.readline().rstrip('\n')
        hundenavn=hundefil.readline().rstrip('\n')
        hundekjønn=hundefil.readline().rstrip('\n')
        hundealder=hundefil.readline().rstrip('\n')

        hundeliste+=[hundeid, oppdretterid, eierid, hundenavn, hundekjønn, hundealder]

        hundeid=hundefil.readline()
    hundefil.close()
    #print(hundeliste)
    print()
    
    oppdretter=input('Oppgi id til oppdretter: ')

    for index in range(0,len(hundeliste),1):
        if oppdretter==hundeliste[index]:
            print(hundeliste[index-1],hundeliste[index+2],hundeliste[index+3],hundeliste[index+4])
    fortsette=input('Ønsker du en ny utskrift? ')





