#karakter A=92; B=77; C=58; D=46; E=40; F=39...
#Lag et program som på bakgrunn av poengsum som inndata viser karakteren

dine_poeng=int(input('Skriv inn dine karakterpoeng her: '))
a_poeng=92
b_poeng=77
c_poeng=58
d_poeng=46
e_poeng=40

if dine_poeng>=a_poeng:
    print('Gratulerer, du er best og får karakteren A')
else:
    if dine_poeng>=b_poeng:
        print('Du var nesten der, karakteren din ble en B')
    else:
        if dine_poeng>=c_poeng:
            print('Midt på 3 er slettes ikke verst, du fikk karakteren C')
        else:
            if dine_poeng>=d_poeng:
                print('Det kunne vært verre, du fikk karakteren D')
            else:
                if dine_poeng>=e_poeng:
                    print('Det var så vidt, men du klarte å få karakteren E')
                else:
                    print('Beklager, du fikk strykkarakteren F')

#bruker man <= i starten av koden, så skal den brukes gjennom hele koden, og omvendt
