# PRG1100-2022-moduler

#Klassen BankKonto lagres i en modul/ egen .py-fil
#bankkonto.py vil da være tilgjengelig for mange programmer via import
#Det er fila som importeres og gjør klassen tilgjengelig for programmet
#Ved oppretting av objekter må en da sette <modulnavn.> forran klassenavnet
import bankkonto

def main():

    saldo=float(input('Hva er saldoen på kontoen til Kari: '))

    karis_konto=bankkonto.BankKonto(saldo)

    saldo=float(input('Hva er saldoen på kontoen til Knut: '))

    knuts_konto=bankkonto.BankKonto(saldo)

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

    
