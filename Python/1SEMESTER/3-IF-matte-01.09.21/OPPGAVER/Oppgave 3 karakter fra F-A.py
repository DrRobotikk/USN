a=92
b=77
c=58
d=46
e=40
kar=int(input('Skriv her '))

if kar<40:
    print('F')
else:
    if kar<=46:
        print('E')
    else:
        if kar<=58:
            print('D')
        else:
            if kar<77:
                print('C')
            else:
                if kar<92:
                    print('B')
                else:
                    print('A')
