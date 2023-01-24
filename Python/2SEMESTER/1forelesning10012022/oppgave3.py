#Program for å kjøre koden videre etter ValueError og I/O-error
fortsette='ja'
while fortsette=='ja':
    summen=0
    filnavn=input('Oppgi filnavn: ')
    #side 366 handler om try
    try:
        
        #stallfil=open('tall.txt','r')#Denne hører til ValueError-delen
        tallfil=open(filnavn,'r')
        tallet=tallfil.readline()
        while tallet!='':
            tallet=tallet.rstrip('\n')
            summen+=int(tallet)
            tallet=tallfil.readline()
        tallfil.close()
        print(summen)

    except ValueError:
        print(summen)
    except IOError:
        print('Fant ikke fila')
    fortsette=input('Flere utskrift? ')

