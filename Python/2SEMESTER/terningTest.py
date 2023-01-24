import random

en=0
to=0
tre=0
fire=0
fem=0
seks=0

antall_kast=int(input('Oppgi antall kast: '))

for antall_ganger in range(1,antall_kast+1,1):
    terning_verdi=random.randint(1,6)
    if terning_verdi==1:
        opp=1
        en+=1
    if terning_verdi==2:
        opp=2
        to+=1
    if terning_verdi==3:
        opp=3
        tre+=1
    if terning_verdi==4:
        opp=4
        fire+=1
    if terning_verdi==5:
        opp=5
        fem+=1
    if terning_verdi==6:
        opp=6
        seks+=1
    print('Resultatet av kast nr',antall_ganger,'ble',opp)
#print('Resultatet av antall kast ble:',en,to,tre,fire,fem,seks)

    
