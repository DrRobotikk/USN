#Delprogram for å slette en eksisterende hundeeier
def slett_hundeeier():
    ny_eier='ja'
    while ny_eier=='ja':
        import os
        funnet_eier=False
        funnet_eier_i_hund=False
        slett=input('Oppgi ID til eieren som skal slettes: ')
        #Sjekker i hundeeierfila om eieren stemmer overens med input
        hundeeierfil=open('hundeeier.txt','r')
        eierid=hundeeierfil.readline()
        while eierid!='':
            eierid=eierid.rstrip('\n')
            fornavn=hundeeierfil.readline().rstrip('\n')
            etternavn=hundeeierfil.readline().rstrip('\n')

            if slett==eierid:
                #print('Eieren finnes fra før')
                funnet_eier=True
            eierid=hundeeierfil.readline()
        hundeeierfil.close()
        #Har vi funnet eieren, må vi sjekke om han har registrerte hunder på seg
        if funnet_eier==True:
            hundefil=open('hund.txt','r')
            hundeid=hundefil.readline()
            while hundeid!='':
                hundeid=hundeid.rstrip('\n')
                hundeeier=hundefil.readline().rstrip('\n')
                oppdretter=hundefil.readline().rstrip('\n')
                hundenavn=hundefil.readline().rstrip('\n')
                hundekjonn=hundefil.readline().rstrip('\n')
                hundedato=hundefil.readline().rstrip('\n')

                if slett==hundeeier:
                    #print('Eieren kan ikke slettes da han har hund')
                    funnet_eier_i_hund=True
                hundeid=hundefil.readline()
            hundefil.close()
        #Hvis eieren finnes og han har IKKE hunder på seg, kan vi fortsette med
        #å slette han fra fila
        if funnet_eier==True and funnet_eier_i_hund==False:
            hundeeierfil=open('hundeeier.txt','r')
            midlertidigfil=open('midlertidig.txt','w')
            eier_id=hundeeierfil.readline()
            while eier_id!='':
                eier_id=eier_id.rstrip('\n')
                for_navn=hundeeierfil.readline().rstrip('\n')
                etter_navn=hundeeierfil.readline().rstrip('\n')

                if eier_id!=slett:
                    midlertidigfil.write(eier_id+'\n')
                    midlertidigfil.write(for_navn+'\n')
                    midlertidigfil.write(etter_navn+'\n')
                eier_id=hundeeierfil.readline()
            hundeeierfil.close()
            midlertidigfil.close()
            os.remove('hundeeier.txt')
            os.rename('midlertidig.txt','hundeeier.txt')
            print('Eieren er blitt slettet')
        if funnet_eier==False:
            print('Eieren finnes ikke i lista')
        if funnet_eier_i_hund==True:
            print('Eieren kan ikke slettes da han har hund')
        ny_eier=input('Ønsker du å slette en ny eier? ')
slett_hundeeier()
            
            
                    
