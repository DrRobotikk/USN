# Bankkonto.py

class BankKonto:
    def __init__(self,saldo):
        self.__saldo=saldo

    def innskudd(self,belop):
        self.__saldo=self.__saldo+belop

    def uttak(self,belop):
        if self.__saldo>=belop:
            self.__saldo=self.__saldo-belop

        else:
            print('Feil: ikke nok på konto.')

    def hent_saldo(self):
        return self.__saldo
