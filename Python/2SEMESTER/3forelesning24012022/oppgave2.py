#Program for å boblesortere en usortert liste A
#Pseudo for boblesortering med stoppmerke

#bytte=true
#j=1       J KAN DEFINERES SOM STOPPMERKE

#while bytte:
#   bytte=false
#   for i=0 to length[A]-j:      I KAN DEFINERES SOM INDEX, A KAN DEFINERES SOM LISTE/ USORTERT
#       if A[i]>A[i+1]:
#           bytte=true
#           A[i] og A[i+1] bytter plass
#       end if
#   end for
#   j=j+1
#end while



usortert=[5,3,1,2,4,7,6]
print('Tabell før sortering er',usortert)
bytte=True
stoppmerke=1

print()
print('Start på WHILE-løkka.')

while bytte==True:
    print('Gjennomgang starter')
    print('Start på FOR-løkka')
    print()
    bytte=False
    
    for n in range(0,len(usortert)-stoppmerke,1):
        
        if usortert[n]>usortert[n+1]:
            byttet=usortert[n]
            usortert[n]=usortert[n+1]
            usortert[n+1]=byttet
            bytte=True
            print('Lista etter hvert bytte innen en gjennomgang:',usortert)
    stoppmerke=stoppmerke+1
    print()
    print('Slutt på FOR-løkka')
print('Slutt på WHILE-løkka')
print('Sortert tabell:',usortert)
