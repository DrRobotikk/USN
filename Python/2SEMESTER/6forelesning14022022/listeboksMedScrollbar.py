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

#Liste og scrollbar er to uavhengige komponenter som knyttes sammen
#Listeboks med vertikal scrollbar på høyre side
#Scrollbaren må defineres før listeboksen, her: y_scroll
#Listeboksen heter lst_ansatte og får verdi lest fra fil
#yscrollcommand=y_scroll.set må inn i listeboksen
#y_scroll['command']=lst_ansatte.yview må inn i programmet

y_scroll=Scrollbar(window,orient=VERTICAL)
y_scroll.grid(row=0,column=2,rowspan=5,padx=(0,100),pady=5,sticky=E)

innhold_i_lst_ansatte=StringVar()
lst_ansatte=Listbox(window,width=10,height=5,listvariable=innhold_i_lst_ansatte,yscrollcommand=y_scroll.set)
lst_ansatte.grid(row=0,column=1,rowspan=5,padx=(100,0),pady=5,sticky=E)

innhold_i_lst_ansatte.set(tuple(fornavn))
y_scroll['command']=lst_ansatte.yview

epost_til=StringVar()
ent_epost=Entry(window,width=30,state='readonly',textvariable=epost_til)
ent_epost.grid(row=0,column=3,sticky=E)

lst_ansatte.bind('<<ListboxSelect>>',hent_epost)

window.mainloop()

























