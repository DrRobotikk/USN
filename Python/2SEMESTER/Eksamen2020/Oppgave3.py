#OPPGAVE 3
#Lag et vindu hvor du har en liste med alle utleier
#som ikke er avslutta (regnr og utlevert), sortert på 
#utleveringstidspunkt, og når en velger i lista får en
#informasjon om hvem som leier bilen (mobilnr,fornavn og etternavn). 

from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Bilsjef',passwd='eksamen2020',db='bilDeling')


def hent_info(event):
    liste=[]

    valgt=lst_regnr.get(lst_regnr.curselection())
    sjekk_markor=mindatabase.cursor()
    reg=valgt[0]

    sjekk=('''
            SELECT mobilnr,fornavn,etternavn
            FROM kunde JOIN utleie USING (mobilnr)
            WHERE utleie.regnr='%s' AND innlevert IS NULL
            ''')
    sjekk_markor.execute(sjekk%reg)
    for row in sjekk_markor:
        liste+=[[row[0],row[1],row[2]]]
        nr.set(row[0])
        forn.set(row[1])
        etter.set(row[2])
    sjekk_markor.close()
        


billiste=[]
hent_markor=mindatabase.cursor()

hent_markor.execute('''
                    SELECT regnr,utlevert
                    from utleie
                    where innlevert is null
                    ''')
for row in hent_markor:
    billiste+=[[row[0],row[1]]]
  
hent_markor.close()

vindu=Tk()
vindu.title('Hent kundeinformasjon')

y_scroll=Scrollbar(vindu,orient=VERTICAL)
y_scroll.grid(row=0,column=1,padx=(0,100),pady=10,sticky=NS)

innhold_regnr=StringVar()
lst_regnr=Listbox(vindu,width=40,height=5,listvariable=innhold_regnr,yscrollcommand=y_scroll.set)
lst_regnr.grid(row=0,column=0,padx=(100,0),pady=10,sticky=W)

innhold_regnr.set(tuple(billiste))
y_scroll['command']=lst_regnr.yview

lst_regnr.bind('<<ListboxSelect>>',hent_info)

lbl_nr=Label(vindu,text='Mobilnr')
lbl_nr.grid(row=1,column=0,padx=10,pady=10,sticky=W)

lbl_for=Label(vindu,text='Fornavn')
lbl_for.grid(row=2,column=0,padx=10,pady=10,sticky=W)

lbl_etter=Label(vindu,text='Etternavn')
lbl_etter.grid(row=3,column=0,padx=10,pady=10,sticky=W)

nr=StringVar()
ent_nr=Entry(vindu,width=8,textvariable=nr)
ent_nr.grid(row=1,column=0,padx=10,pady=10,sticky=E)

forn=StringVar()
ent_for=Entry(vindu,width=20,textvariable=forn)
ent_for.grid(row=2,column=0,padx=10,pady=10,sticky=E)

etter=StringVar()
ent_etter=Entry(vindu,width=20,textvariable=etter)
ent_etter.grid(row=3,column=0,padx=10,pady=10,sticky=E)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=4,column=1,padx=10,pady=10,sticky=SE)

vindu.mainloop()
mindatabase.close()
