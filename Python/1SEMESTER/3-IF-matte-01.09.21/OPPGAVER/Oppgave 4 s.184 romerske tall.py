#Skriv et program som gjør om tallene 1-10 om til romerske tall
#Om tallet er større enn 10, skriv en error

tallet=int(input('Skriv inn tallet som skal gjøres om til romersk tall: '))

minst=0

if tallet==0:
    print('Romerne brukte samme symbolet for null, altså "0"')
else:
    if tallet==1:
        print('I')
    else:
        if tallet==2:
            print('II')
        else:
            if tallet==3:
                print('III')
            else:
                if tallet==4:
                    print('IV')
                else:
                    if tallet==5:
                        print('V')
                    else:
                        if tallet==6:
                            print('VI')
                        else:
                            if tallet==7:
                                print('VII')
                            else:
                                if tallet==8:
                                    print('VIII')
                                else:
                                    if tallet==9:
                                        print('IX')
                                    else:
                                        if tallet==10:
                                            print('X')
                                        else:
                                            if tallet>10:
                                                print('Du, jeg er på min tredje uke i IT utdanninga','\n','det finnes begrensninger på hva jeg får til')
