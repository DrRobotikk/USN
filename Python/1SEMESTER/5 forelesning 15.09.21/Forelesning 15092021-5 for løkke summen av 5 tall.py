#Program for å summere 5 tall

summen_er=0

for n in range(1,6,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    summen_er=summen_er+tall

print('Summen av de 5 tallene er:',summen_er)
