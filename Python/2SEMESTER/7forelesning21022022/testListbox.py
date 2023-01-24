import mysql.connector
from tkinter import *

mindatabase=mysql.connector.connect(host='localhost',port=3306,
    user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

def hent_prisoglager(event):

    valgt=lst_varer.get(lst_varer.curselection())

    prisoglager_markor=mindatabase.cursor()
    prisoglager_markor.execute('SELECT Betegnelse, Pris, Antall FROM Vare')

    for row in prisoglager_markor:
        if valgt==row[0]:
            pris.set(row[1])
            lager.set(row[2])
    prisoglager_markor.close()

vare_markor=mindatabase.cursor()

vare_markor.execute('SELECT Betegnelse FROM Vare')

varer=[]
for row in vare_markor:
    varer+=[row[0]]

window=Tk()
window.title('Varer')

y_scroll=Scrollbar(window, orient=VERTICAL)
y_scroll.grid(row=0,column=2, rowspan=10, padx=(0,100),pady=5,sticky=NS)

innhold_i_lst_varer=StringVar()
lst_varer=Listbox(window,width=50,height=10,listvariable=innhold_i_lst_varer,yscrollcommand=y_scroll.set)
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

btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=3,column=5,padx=5,pady=5)

window.mainloop()

vare_markor.close()
mindatabase.close()
