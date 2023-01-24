#program som simulerer test av disjunksjonen/ ELLER mellom to logiske utsagn

print('Vi ønsker å vurdere  A>3 eller B<6 for ulike verdier av A og B, jfr forelesning 4, onsdag 08092021')

#I dette eksempelet bryter vi med at variabelnavn bør skrives med små bokstaver

#Verdien på A styres av en FOR-løkke [2,5>
for A in range(2,6,1):
    
    #Verdien på B styres av en FOR-løkke [4,7>
    for B in range(4,8,1):
        
        if A>3 or B<6: #Vi lager oss en test på disjunksjonen
            print('Verdien på A er',A,'og verdien på B er',B,'og disjunksjonen er sann')
        else:
            print('Verdien på A er',A,'og verdien på B er',B,'og disjunksjonen er usann')
    print('Her er det slutt på løkka for å øke B med 1')
    print()
    print('Her øker verdien på A med 1')
print('Da er det slutt på løkka for å øke A med 1, og dermed slutt på programmet')
