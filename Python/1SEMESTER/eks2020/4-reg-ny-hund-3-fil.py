def registrer_ny_hund():
    ny_hund='ja'
    while ny_hund=='ja':
        #her lager jeg utsagn for å holde kontroll
        funnet_hund=False 
        funnet_eier=False
        funnet_oppdretter=False

        hund=input('Oppgi hundens id: ')
        hundefil=open('hund.txt','r')
        hundeid=hundefil.readline()
        
        while hundeid!='':
            hundeid=hundeid.rstrip('\n')
            oppdretterid=hundefil.readline().rstrip('\n')
            hundeeierid=hundefil.readline().rstrip('\n')
            navn=hundefil.readline().rstrip('\n')
            kjonn=hundefil.readline().rstrip('\n')
            fodt=hundefil.readline().rstrip('\n')

            if hundeid==hund:
                print('Hunden finnes fra før')
                funnet_hund=True
            hundeid=hundefil.readline()
        hundefil.close()
        #Om hunden ikke finnes, kan den registreres. Først må jeg sjekke om eieren finnes   
        if funnet_hund==False:
            eier=input('Oppgi eierens id: ')
            hundeeierfil=open('hundeeier.txt','r')
            eierid=hundeeierfil.readline()
            while eierid!='':
                eierid=eierid.rstrip('\n')
                eier_fornavn=hundeeierfil.readline().rstrip('\n')
                eier_etternavn=hundeeierfil.readline().rstrip('\n')

                if eier==eierid:
                    print('Eieren finnes fra før')
                    funnet_eier=True
                eierid=hundeeierfil.readline()
            hundeeierfil.close()
        #Hvis hunden ikke finnes og eieren finnes, må jeg sjekke om oppdretteren finnes før hunden kan registreres
        if funnet_hund==False and funnet_eier==True:
            oppdretter=input('Oppgi oppdretterens id: ')
            oppdretterfil=open('oppdretter.txt','r')
            oppdretterid=oppdretterfil.readline()
            while oppdretterid!='':
                oppdretterid=oppdretterid.rstrip('\n')
                kennel=oppdretterfil.readline().rstrip('\n')
                fornavn=oppdretterfil.readline().rstrip('\n')
                etternavn=oppdretterfil.readline().rstrip('\n')

                if oppdretterid==oppdretter:
                    print('Oppdretteren finnes fra før')
                    funnet_oppdretter=True
                oppdretterid=oppdretterfil.readline()
            oppdretterfil.close()
        #Om hunden ikke finnes men både eieren og oppdretteren finnes, kan jeg fortsette med å lagre info om hunden
        if funnet_hund==False and (funnet_eier==True) and (funnet_oppdretter==True):
            hundefil=open('hund.txt','a')
            hund_navn=input('Oppgi hundens navn: ')
            hund_kjonn=input('Oppgi hundens kjønn: ')
            hund_alder=input('Oppgi hundens fødselsdato: ')

            hundefil.write(hund+'\n')
            hundefil.write(eier+'\n')
            hundefil.write(oppdretter+'\n')
            hundefil.write(hund_navn+'\n')
            hundefil.write(hund_kjonn+'\n')
            hundefil.write(hund_alder+'\n')

            print('Lista oppdatert')
        if funnet_eier==False:
            print('Eieren er ikke registrert')
        hundefil.close()
        ny_hund=input('Ønsker du å legge til flere hunder? (ja/nei) ')

registrer_ny_hund()
