#Oppgave 3:
#Lag et vindu for å registrere en ny kunde med dekksett og oppbevaring.
#Det må sjekkes at kunden ikke finnes fra før. 

import mysql.connector
from tkinter import *

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Dekksjef',passwd='Eksamen2021',db='Dekkhotell')

def sjekk_kunde():
    sjekk_markor=mindatabase.cursor()
    kundeliste=[]
    mobil=nr.get()
    funnet=False
    rad=0

    sjekk_markor.execute('''
                        SELECT Mobilnr
                        FROM Kunde
                        ''')
    for row in sjekk_markor:
        kundeliste+=[[row[0]]]
    sjekk_markor.close()

    while (funnet==False) and (rad<=len(kundeliste)-1):
        if mobil==kundeliste[rad][0]:
            funnet=True
        else:
            rad+=1

        if funnet==True:
            lbl_svar.config(text='Kunden finnes fra før')
        if funnet==False:
            lbl_svar.config(text='Kunden finnes ikke')

def lagre_kunde():
    lagre_markor=mindatabase.cursor()

    mobil=nr.get()
    fornavn=forn.get()
    etternavn=etter.get()
    eposten=epost.get()

    lagre=('''
            INSERT INTO Kunde VALUES
            (%s,%s,%s,%s)
            ''')
    settinn=(mobil,fornavn,etternavn,eposten)
    lagre_markor.execute(lagre,settinn)
    mindatabase.commit()

    lagre_markor.close()

    lagre_markor=mindatabase.cursor()
    reg=regnr.get()

    lagre=('''
            INSERT INTO Dekksett VALUES
            (%s,%s)
            ''')
    settinn=(mobil,reg)
    lagre_markor.execute(lagre,settinn)
    mindatabase.commit()
    lagre_markor.close()

    lagre_markor=mindatabase.cursor()

    hylla=hylle.get()

    lagre=('''
            INSERT INTO Oppbevaring(Mobilnr,Regnr,Innlevert,Utlevert,Hylle,Pris) VALUES
            (%s,%s,CURRENT_TIMESTAMP(),NULL,%s,NULL)
            ''')
    settinn=(mobil,reg,hylla)
    lagre_markor.execute(lagre,settinn)
    mindatabase.commit()
    lagre_markor.close()

    
vindu=Tk()
vindu.title('Oppbevaringsoversikt')

lbl_nr=Label(vindu,text='Mobilnr')
lbl_nr.grid(row=0,column=0,padx=10,pady=10,sticky=W)

lbl_fornavn=Label(vindu,text='Fornavn')
lbl_fornavn.grid(row=1,column=0,padx=10,pady=10,sticky=W)

lbl_etter=Label(vindu,text='Etternavn')
lbl_etter.grid(row=2,column=0,padx=10,pady=10,sticky=W)

lbl_epost=Label(vindu,text='Epost')
lbl_epost.grid(row=3,column=0,padx=10,pady=10,sticky=W)

lbl_regnr=Label(vindu,text='Regnr')
lbl_regnr.grid(row=4,column=0,padx=10,pady=10,sticky=W)

lbl_hylle=Label(vindu,text='Hylle')
lbl_hylle.grid(row=5,column=0,padx=10,pady=10,sticky=W)

lbl_svar=Label(vindu,text='')
lbl_svar.grid(row=1,column=2)

nr=StringVar()
ent_nr=Entry(vindu,width=11,textvariable=nr)
ent_nr.grid(row=0,column=1,padx=10,pady=10,sticky=W)

forn=StringVar()
ent_fornavn=Entry(vindu,width=11,textvariable=forn)
ent_fornavn.grid(row=1,column=1,padx=10,pady=10,sticky=W)

etter=StringVar()
ent_etter=Entry(vindu,width=20,textvariable=etter)
ent_etter.grid(row=2,column=1,padx=10,pady=10,sticky=W)

epost=StringVar()
ent_epost=Entry(vindu,width=25,textvariable=epost)
ent_epost.grid(row=3,column=1,padx=10,pady=10,sticky=W)

regnr=StringVar()
ent_regnr=Entry(vindu,width=8,textvariable=regnr)
ent_regnr.grid(row=4,column=1,padx=10,pady=10,sticky=W)

hylle=StringVar()
ent_hylle=Entry(vindu,width=6,textvariable=hylle)
ent_hylle.grid(row=5,column=1,padx=10,pady=10,sticky=W)

btn_sjekk=Button(vindu,text='Sjekk kunde',command=sjekk_kunde)
btn_sjekk.grid(row=0,column=2,padx=10,pady=10,sticky=E)

btn_lagre=Button(vindu,text='Lagre',command=lagre_kunde)
btn_lagre.grid(row=5,column=1,padx=10,pady=10,sticky=SE)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=6,column=1,padx=10,pady=10,sticky=SE)

vindu.mainloop()

mindatabase.close()
