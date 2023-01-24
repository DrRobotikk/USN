#finn minste tallet i en tallrekke bestående av 5 tall

minste_tall=int(input('Skriv inn tallet her: '))
rekkefolge=1

for n in range(1,5,1):
    tall=int(input('Skriv inn tallet her: '))
    if tall<minste_tall:
        minste_tall=tall
        rekkefolge=n+1
print('Minstetallet i tallrekka du oppga er',minste_tall,'og er det',rekkefolge,'tallet i rekkefølgen.')

