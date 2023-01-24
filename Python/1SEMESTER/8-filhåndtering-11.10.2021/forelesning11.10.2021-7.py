#Program for innføring i funksjoner/ prosedyrer


def drommebolig():
    #Her kommer kode for kalkulator 1(drømmebolig)
    print('Du har valgt kalkulator 1, drømmebolig')
    print()

def lanebevis():
    print('Du har valgt kalkulatoren 2, lånebevis')
    print()

    
def main():
    fortsette=True

    while fortsette:
        valgt_kalkulator=int(input('Hvilken kalkulator vil du bruke? '))
        if valgt_kalkulator==1:
            drommebolig()
        else:
            lanebevis()

        svar=input('Ønsker du å bruke en av kalkulatorene på nytt? ')
        if svar=='nei':
            fortsette=False

#her kommer hovedprogrammet/ kjører main()
main()
