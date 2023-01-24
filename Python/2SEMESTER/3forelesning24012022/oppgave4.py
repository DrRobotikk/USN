#PRG1100-2022-innstikksortering slightly_faster - pseudo
#Program for å innstikksortere en usortert liste

#Pseudokoden blir da:
#for i = 1 to length(A)
#    x = A[i]
#    j = i - 1
#    while j >= 0 and A[j] > x
#        A[j+1] = A[j]
#        j = j - 1
#    end while
#    A[j+1] = x
# end for

tabell=[5,3,1,2,4]
print(tabell)
print()


for index in range(1,len(tabell),1):
    print('Vi jobber med "kort" nr.',index+1,'i tabellen over')
    print('Det har verdien',tabell[index])
    

    print('"Kortet tas ut"')
    x=tabell[index]
    stopp_merke=index-1

    flytt=0

    while stopp_merke>=0 and (tabell[stopp_merke]>x):
        
        tabell[stopp_merke+1]=tabell[stopp_merke]
        stopp_merke=stopp_merke-1
        flytt=flytt+1
    tabell[stopp_merke+1]=x
    print('Og',flytt,'"kort" forran flyttes til høyre, før "kortet" settes inn')
    print('Resultatet blir da',tabell)
    print()
    
print('Slutt på FOR-løkke og den sorterte tabellen er',tabell)


