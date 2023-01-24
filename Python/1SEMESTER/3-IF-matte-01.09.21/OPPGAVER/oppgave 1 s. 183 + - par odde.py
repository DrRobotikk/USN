#lag et program som sier om tallet er positivt, negativt eller lik null

heltall=int(input('Skriv inn heltallet her: '))

null=0

if heltall<null:
    print('Tallet er negativt')
    if heltall%2==0:
        print('Tallet er partall')
    else:
        print('Tallet er oddetall')
    
if heltall>null:
    print('Tallet er positivt')
    if heltall%2==0:
        print('Tallet er partall')
    else:
        print('Tallet er oddetall')
    
if heltall==null:
    print('Tallet er null')
