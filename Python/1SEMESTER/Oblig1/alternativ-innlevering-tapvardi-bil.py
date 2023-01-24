#Input nybilspris og alder
#1. 20%
#2. 14% etter 1 år
#3. 13% etter 2 år
#4. 12% etter 3 år
#5. 11% etter 4 år
#6. 10% etter 5 år
#print nybilpris, bilens alder, verditap i kr og bruktverd
igjen='ja'
while igjen=='ja':
    pris=int(input('Oppgi nybilpris: '))
    alder=int(input('Oppgi bilens alder: '))
    

    if alder==1:
        et_år=pris-((pris/100)*20)
        tap1=pris-et_år
        print('Nypris er',pris,'alder er',alder,'verditapet er',tap1,'og bruktverdien er',et_år)
    elif alder==2:
        to_år=et_år-((et_år/100)*13)
        tap2=pris-to_år
        print(to_år)
    elif alder==3:
        tre_år=to_år-((to_år/100)*12)
        print(tre_år)
    elif alder==4:
        fire_år=tre_år-((tre_år/100)*11)
        print(fire_år)
    else:
        fem_år=fire_år-((fire_år/100)*10)
        print(fem_år)
    igjen=input('Igjen? ')
    
    
