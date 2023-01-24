#PRG1100-2022-flere instanser

#Flere objekter/ instanser av samme klasse, her: kontoene til flere personer
#Kari og Knut

class BankKonto:
    def __init__(self,saldo):
        self.__saldo=saldo

    def innskudd(self,belop):
        self.__saldo=self.__saldo+belop

    def uttak(self,belop):
        if self.__saldo>=belop:
            self.__saldo=self.__saldo-belop

        else:
            print('Feil: ikke nok på konto')

    def hent_saldo(self):
        return self.__saldo

def main():
    saldo=float(input('Hva er saldoen på kontoen til Kari: '))

    karis_konto=BankKonto(saldo)

    saldo=float(input('Hva er saldoen på kontoen til Knut: '))

    knuts_konto=BankKonto(saldo)

    belop=float(input('Hvor mye skal Kari sette inn på konto? '))
    karis_konto.innskudd(belop)

    print('Saldoen på Karis konto er: ',karis_konto.hent_saldo())

    belop=float(input('Hvor mye skal Knut sette inn på konto? '))
    knuts_konto.innskudd(belop)

    print('Saldoen på Knuts konto er: ',knuts_konto.hent_saldo())

    belop=float(input('Hvor mye skal Kari ta ut? '))
    karis_konto.uttak(belop)

    print('Saldoen på Karis konto etter uttak er: ',karis_konto.hent_saldo())

    belop=float(input('Hvor mye skal Knut ta ut? '))
    knuts_konto.uttak(belop)

    print('Saldoen på Knut konto etter uttak er: ',knuts_konto.hent_saldo())

main()

    
