#Definere tallene i tallrekken

tall1=int(input('Definert det første tallet: '))
tall2=int(input('Definer det andre tallet: '))
tall3=int(input('Definer det tredje tallet: '))
tall4=int(input('Definer det fjerde tallet: '))

storst=0

if tall1 >= storst:
    storst=tall1
else:
    storst=0

if tall2 >= storst:
    storsts=tall2
else:
    storst=tall1

if tall3 >= storst:
    storst=tall3
else:
    storst=tall2

if tall4 >= storst:
    storst=tall4
else:
    storst=tall3
    

print('Det støreste tallet i denne tallrekken er:',storst)

