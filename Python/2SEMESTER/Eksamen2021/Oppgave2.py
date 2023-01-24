#OPPGAVE 2:
#Lag et vindu hvor du har en liste med alle oppbevaringer som
#ikke er avslutta (regnr og innlevert), sortert på innleveringstidspunkt,
#og når en velger i lista får en informasjon om hvem som er kunde for
#dekksettet og hvor det er plassert på dekkhotellet
#(mobilnr, etternavn, epost og hylle). 

import mysql.connector
from tkinter import *

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Dekksjef',passwd='Eksamen2021',db='Dekkhotell')

def hent_kundeinfo(event):
    valgt=lst_opp.get(lst_opp.curselection())
    regnr=valgt[0]
    kundeliste=[]

    sjekk_markor=mindatabase.cursor()

    sjekk=('''
            SELECT Etternavn,Epost,Oppbevaring.Mobilnr,Hylle
            FROM Kunde JOIN Oppbevaring USING(Mobilnr)
            WHERE Oppbevaring.Regnr=%s AND Utlevert IS NULL;
            ''')
    settinn=(regnr,)
    
    sjekk_markor.execute(sjekk,settinn)

    for row in sjekk_markor:
        kundeliste+=[[row[0],row[1],row[2],row[3]]]
        nr.set(row[2])
        etter.set(row[0])
        epost.set(row[1])
        hylle.set(row[3])

    sjekk_markor.close()

oppbevaringsliste=[]

hent_markor=mindatabase.cursor()

hent_markor.execute('''
                    SELECT Regnr,Innlevert
                    FROM Oppbevaring
                    WHERE Utlevert IS NULL
                    ORDER BY Innlevert ASC;
                    ''')
for row in hent_markor:
    oppbevaringsliste+=[[row[0],row[1]]]

hent_markor.close()

vindu=Tk()
vindu.title('Oppbevaringsoversikt')

y_scroll=Scrollbar(vindu,orient=VERTICAL)
y_scroll.grid(row=0,column=1,padx=(0,20),pady=10,sticky=NS)

innhold_opp=StringVar()
lst_opp=Listbox(vindu,width=30,height=5,listvariable=innhold_opp,yscrollcommand=y_scroll.set)
lst_opp.grid(row=0,column=0,padx=(20,0),pady=10,sticky=W)

innhold_opp.set(tuple(oppbevaringsliste))
y_scroll['command']=lst_opp.yview

lst_opp.bind('<<ListboxSelect>>',hent_kundeinfo)

lbl_nr=Label(vindu,text='Mobilnr')
lbl_nr.grid(row=1,column=0,padx=10,pady=10,sticky=W)

lbl_etter=Label(vindu,text='Etternavn')
lbl_etter.grid(row=2,column=0,padx=10,pady=10,sticky=W)

lbl_epost=Label(vindu,text='Epost')
lbl_epost.grid(row=3,column=0,padx=10,pady=10,sticky=W)

lbl_hylle=Label(vindu,text='Hylle')
lbl_hylle.grid(row=4,column=0,padx=10,pady=10,sticky=W)

nr=StringVar()
ent_nr=Entry(vindu,width=11,textvariable=nr)
ent_nr.grid(row=1,column=0,padx=10,pady=10,sticky=E)

etter=StringVar()
ent_etter=Entry(vindu,width=20,textvariable=etter)
ent_etter.grid(row=2,column=0,padx=10,pady=10,sticky=E)

epost=StringVar()
ent_epost=Entry(vindu,width=25,textvariable=epost)
ent_epost.grid(row=3,column=0,padx=10,pady=10,sticky=E)

hylle=StringVar()
ent_hylle=Entry(vindu,width=10,textvariable=hylle)
ent_hylle.grid(row=4,column=0,padx=10,pady=10,sticky=E)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=5,column=1,padx=10,pady=10,sticky=SE)

vindu.mainloop()

mindatabase.close()
