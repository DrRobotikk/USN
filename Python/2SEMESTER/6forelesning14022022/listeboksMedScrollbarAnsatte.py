#PRG1100-2022-listeboks med scrollbar
#To uavhengige komponenter som knyttes sammen;
#I tillegg skal det vises ekstra info når en velger i lista

from tkinter import *

def hent_epost(event):
    valgt=lst_ansatte.get(lst_ansatte.curselection())

    funnet=False
    radnr=0

    while (funnet==False) and (radnr<=len(ansatte)-1):
        if valgt==ansatte[radnr][0]:
            epost_til.set(ansatte[radnr][2])
            funnet=True
        else:
            radnr+=1

ansatte=[]
ansattfil=open('ansatt.txt','r',encoding='utf-8')

fornavn=ansattfil.readline()
while fornavn!='':
    fornavn=fornavn.rstrip('\n')
    etternavn=ansattfil.readline().rstrip('\n')
    epost=ansattfil.readline().rstrip('\n')

    ansatte+=[[fornavn,etternavn,epost]]

    fornavn=ansattfil.readline()
ansattfil.close()

fornavn=[]
for listelengde in range(0,len(ansatte),1):
    fornavn+=[ansatte[listelengde][0]]

window=Tk()
window.title('Ansatte')
