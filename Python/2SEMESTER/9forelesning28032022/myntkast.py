#PRG1100-2022-opptelling myntkast pp

#Program for brukerbestemt antall myntkast og opptelling av
#antall Kron og Mynt
#funksjonsorientert/ prosedural tilnærming

import random

antall_kron=0
antall_mynt=0

antall_kast=int(input('Oppgi antall ganger mynten skal kastes: '))
print()

for antall_ganger in range(1,antall_kast+1,1):
    if random.randint(0,1)==0:
        sideopp='Kron'
        antall_kron+=1

    else:
        sideopp='Mynt'
        antall_mynt+=1
    print('Resultatet av kast nr',antall_ganger,'ble',sideopp)
print()
print('Resultatet av forsøksrekka ble',antall_kron,'kron, og',antall_mynt,'mynt.')
