#PRG110-2022-listeboks

from tkinter import *

ansatte=[]
ansattfil=open('ansatt.txt','r',encoding='utf-8')

fornavn=ansattfil.readline()
while fornavn!='':
    fornavn=fornavn.rstrip('\n')
    etternavn=ansattfil.readline().rstrip('\n')
    epost=ansattfil.readline().strip('\n')

    ansatte+=[[fornavn,etternavn,epost]]

    fornavn=ansattfil.readline()
ansattfil.close()


fornavn=[]

#går gjennom hele ansattlista og tar vare på fornavn
for listelengde in range(0,len(ansatte),1):
    fornavn+=[ansatte[listelengde][0]]

window=Tk()
window.title('Ansatte')

#oppretter variabel for ansattliste
innhold_i_lst_ansatte=StringVar()
#oppretter listeboks med bredde, høyde samt hva som skal vises i boksen
#forelesning har height=5 men det finnes 9 ansatte, så jeg satte den til 10
lst_ansatte=Listbox(window,width=10,height=10,listvariable=innhold_i_lst_ansatte)
lst_ansatte.grid(padx=100,pady=5)
#gjør om fornavnlista om til tuple, så verdiene ikke kan endres
innhold_i_lst_ansatte.set(tuple(fornavn))

window.mainloop()
