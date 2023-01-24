#Oppgave 3 oppgavesett 1 med if-elif-else tester mindre enn og starter med
#laveste karakter

poengsum=int(input('Oppgi poengsummen her '))

if poengsum<40:
    karakter='F'
elif poengsum<46:
    karakter='E'
elif poengsum<58:
    karakter='D'
elif poengsum<77:
    karakter='C'
elif poengsum<92:
    karakter='B'
else:
    karakter='A'






print('Ved poengsum',poengsum,'får du karakteren',karakter)
