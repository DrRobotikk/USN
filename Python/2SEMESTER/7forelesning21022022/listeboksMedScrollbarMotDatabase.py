import mysql.connector
from tkinter import *

#Selve koden for å hente ut verdier fra databasen
def hent_prisoglager(event):

    #Variabel som kobles mot vår vareliste fra senere i koden
    valgt=lst_varer.get(lst_varer.curselection())

    prisoglager_markor=mindatabase.cursor()
    prisoglager_markor.execute('SELECT Betegnelse, Pris, Antall FROM Vare')

    #Ville vært mer naturlig med WHILE-løkke struktur,
    #nå leser den alle rader hver gang

    for row in prisoglager_markor:
        if valgt==row[0]:
            pris.set(row[1])
            lager.set(row[2])
    prisoglager_markor.close()

mindatabase=mysql.connector.connect(host='localhost',port=3306,
    user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

#2. oppretter cursor/markør
vare_markor=mindatabase.cursor()

#3. bruke databasen; vare_markøren går gjennom alle verdiene
    #i database-tabellen Vare
vare_markor.execute('SELECT * FROM Vare')

#4. bruke resultatet
#Oppretter en liste basert på Betegnelse=Varenavn fra varetabellen
varer=[]
for row in vare_markor:
    varer+=[row[1]]
print(varer) #liste med alle betegnelser

#Oppretter GUI vindu med navn "Varer"
window=Tk()
window.title('Varer')

#Oppretter scrollbar
y_scroll=Scrollbar(window, orient=VERTICAL)
y_scroll.grid(row=0,column=2, rowspan=10, padx=(0,100),pady=5,sticky=NS)

innhold_i_lst_varer=StringVar()
lst_varer=Listbox(window,width=50,height=10,listvariable=innhold_i_lst_varer,yscrollcommand=y_scroll.set)
lst_varer.grid(row=0,column=1, rowspan=10,padx=(100,0),pady=5,sticky=E)

innhold_i_lst_varer.set(tuple(varer))
y_scroll['command']=lst_varer.yview

#Varepris
lbl_pris=Label(window,text='Prisen er:')
lbl_pris.grid(row=0,column=3,padx=5,pady=5,sticky=E)

#Lagerstatus varer
lbl_lager=Label(window,text='Lagerstatusen er: ')
lbl_lager.grid(row=1,column=3,padx=5,pady=5,sticky=E)

#Entry-output av varepris
pris=StringVar()
ent_pris=Entry(window, width=10, state="readonly", textvariable=pris)
ent_pris.grid(row=0,column=4,padx=5,pady=5,sticky=W)

#Entry-output av lagerstatus varer
lager=StringVar()
ent_lager=Entry(window,width=10,state='readonly',textvariable=lager)
ent_lager.grid(row=1,column=4,padx=5,pady=5,sticky=W)

#Parameteroverføring fra vår def "hent_prisoglager"
lst_varer.bind('<<ListboxSelect>>',hent_prisoglager)

btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=3,column=5,padx=5,pady=5)

window.mainloop()

vare_markor.close()
mindatabase.close()
