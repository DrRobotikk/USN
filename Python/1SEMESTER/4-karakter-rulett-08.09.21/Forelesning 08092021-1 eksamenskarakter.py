#oppgave 3 oppgavesett 1, med nøsta hvis-setninger, tester< og starter med laveste karakter

#Kandidatens poengsum som inndata fra brukeren

poengsum=int(input('oppgi kandidatens poengsum '))

#Tilordning av karakter ved nøsta hvis

if poengsum<40:
    karakter='F'
else:
    if poengsum<46:
        karakter='E'
    else:
        if poengsum<58:
            karakter='D'
        else:
            if poengsum<77:
                karakter='C'
            else:
                if poengsum<92:
                    karakter='B'
                else:
                    karakter='A'
#skriv ut resultatet

print(karakter)

        
