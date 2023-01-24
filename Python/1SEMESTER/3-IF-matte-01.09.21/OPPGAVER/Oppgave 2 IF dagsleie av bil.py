#et bilutleiefirma tilbyr følgende alternativer for dagsleie av bil
#1. fastpris 750kr
#2. fastpris 300kr og 2kr pr kjørt km
#3. fastpris 150kr og 4 kr pr kjørt km
#Kunden må velge et av alternativene
#Lag et program som sammenligner de tre alternativene ut ifra antall km som inndata
#og avgjør hvilket alternativ som er best for kunden

km_lengde=int(input('Oppgi antall km du har tenkt å kjøre med leiebilen pr. dag: '))
pris1=750
pris2=300+2*km_lengde
pris3=150+4*km_lengde
print(pris1,pris2,pris3)

#MIN EGEN LØSNING, FUNGERER HELT FINT

#if pris2>pris1:
    #print('Første alternativ passer deg best')
#else:
    #if pris3>pris2:
        #print('Andre alternativ passer deg best')
    #else:
        #print('Tredje alternativ passer deg best')

#LØSNINGEN TIL ERIK, FUNGERER OGSÅ HELT FINT, LITT MER OVERSIKTLIG

if pris1>pris2:
    if pris2>pris3:
        if pris3<pris1:
            print('Tredje prisen passer deg best')
    else:
        print('Andre prisen passer deg best')
else:
    print('Første prisen passer deg best')
