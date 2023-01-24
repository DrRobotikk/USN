import mysql.connector
from tkinter import *

def hent_prisoglager(event):
    valgt=lst_varer.get(lst_varer.curselection())

    prisoglager_markor=mindatabase.cursor()
    prisoglager_markor.execute('SELECT Betegnelse, Pris, Antall FROM Vare')

    #While-løkke ikke ferdig
    while prisoglager_markor!='':
        
        

        if valgt==:
            pris.set()
            lager.set()

  
    prisoglager_markor.close()


#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
    user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

#2. oppretter cursor/markør
vare_markor=mindatabase.cursor()

#3. bruke databasen
vare_markor.execute('SELECT Betegnelse FROM Vare')

#4. bruke resultatet
#Oppretter en liste basert på Betegnelse/Varenavn fra varetabellen
varer=[]
for r in vare_markor:
    varer+=[r[0]]

window=Tk()
window.title('Varer')

y_scroll=Scrollbar(window, orient=VERTICAL)
y_scroll.grid(row=0,column=2, rowspan=10, padx=(0,100),pady=5,sticky=NS)

innhold_i_lst_varer=StringVar()
lst_varer=Listbox(window, width=50,height=10,
        listvariable=innhold_i_lst_varer, yscrollcommand=y_scroll.set)
lst_varer.grid(row=0,column=1, rowspan=10,padx=(100,0),pady=5,sticky=E)
innhold_i_lst_varer.set(tuple(varer))
y_scroll['command']=lst_varer.yview

lbl_pris=Label(window,text='Prisen er:')
lbl_pris.grid(row=0,column=3,padx=5,pady=5,sticky=E)

lbl_lager=Label(window,text='Lagerstatusen er: ')
lbl_lager.grid(row=1,column=3,padx=5,pady=5,sticky=E)

pris=StringVar()
ent_pris=Entry(window, width=10, state="readonly", textvariable=pris)
ent_pris.grid(row=0,column=4,padx=5,pady=5,sticky=W)

lager=StringVar()
ent_lager=Entry(window,width=10,state='readonly',textvariable=lager)
ent_lager.grid(row=1,column=4,padx=5,pady=5,sticky=W)

lst_varer.bind('<<ListboxSelect>>',hent_prisoglager)

window.mainloop()

#5. koble ned databasen
vare_markor.close()
mindatabase.close()
