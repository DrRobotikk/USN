#OPPGAVE 4:
#Lag et vindu for å registrere et nytt utleie hvor en velger bil fra en liste
#over biler som er ledige og oppgir mobilnr på kunde som skal leie bilen.
#Det må sjekkes at kunden ikke har noen uavsluttede leieforhold fra før.

from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Bilsjef',passwd='eksamen2020',db='bilDeling')

def lagre_liste(event):
    valgt=lst_regnr.get(lst_regnr.curselection())
    global reg
    reg=valgt[0]


def lagre_utleie():
    mobil=mobnr.get()
    kundeliste=[]
    funnet=False
    rad=0
    
    kunde_markor=mindatabase.cursor()

    kunde_markor.execute('''
            SELECT mobilnr
            FROM utleie
            WHERE innlevert IS NULL
            ''')
    
    for row in kunde_markor:
        kundeliste+=[[row[0]]]
    kunde_markor.close()
    while (funnet==False) and (rad<=len(kundeliste)-1):
        if mobil==kundeliste[rad][0]:
            funnet=True
        else:
            rad+=1

        if funnet==True:
            svar.config(text='Kunden kan ikke leie ny bil')
        if funnet==False:
            svar.config(text='Kunden kan leie bil')
            
    if funnet==False:
        km_markor=mindatabase.cursor()

        hent=('''
                SELECT MAX(kminn)
                FROM utleie
                WHERE regnr=%s
                ''')
        settinn=(reg,)
        km_markor.execute(hent,settinn)

        for row in km_markor:
            kmut=row[0]
        km_markor.close()
        lagre_markor=mindatabase.cursor()

        lagre=('''
                INSERT INTO utleie(regnr,utlevert,kmut,mobilnr,innlevert,kminn,beløp)values
                (%s,CURRENT_TIMESTAMP,%s,%s,NULL,NULL,NULL)
                ''')
        settinn=(reg,kmut,mobil)

        lagre_markor.execute(lagre,settinn)
        mindatabase.commit()
        lagre_markor.close()
        svar2.config(text='Lagret')



billiste=[]
hent_markor=mindatabase.cursor()

hent_markor.execute('''
                    SELECT regnr,merke,modell
                    FROM bil
                    WHERE regnr NOT IN
                        (SELECT regnr FROM utleie WHERE innlevert IS NULL)
                    ''')
for row in hent_markor:
    billiste+=[[row[0],row[1],row[2]]]
#print(billiste) OK
  
hent_markor.close()

vindu=Tk()
vindu.title('Registrer nytt utleie')

y_scroll=Scrollbar(vindu,orient=VERTICAL)
y_scroll.grid(row=0,column=1,padx=(0,100),pady=10,sticky=NS)

innhold_regnr=StringVar()
lst_regnr=Listbox(vindu,width=30,height=5,listvariable=innhold_regnr,yscrollcommand=y_scroll.set)
lst_regnr.grid(row=0,column=0,padx=(100,0),pady=10,sticky=W)

innhold_regnr.set(tuple(billiste))
y_scroll['command']=lst_regnr.yview

lst_regnr.bind('<<ListboxSelect>>',lagre_liste)

lbl_mobnr=Label(vindu,text='Mobilnr')
lbl_mobnr.grid(row=1,column=0,padx=10,pady=10,sticky=W)

mobnr=StringVar()
ent_mobnr=Entry(vindu,width=11,textvariable=mobnr)
ent_mobnr.grid(row=1,column=0,padx=10,pady=10,sticky=E)

btn_lagre=Button(vindu,text='Lagre utleie',command=lagre_utleie)
btn_lagre.grid(row=2,column=3,padx=10,pady=10,sticky=SE)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=3,column=3,padx=10,pady=10,sticky=SE)

svar=Label(vindu,text='')
svar.grid(row=2,column=0,padx=10,pady=10,sticky=E)

svar2=Label(vindu,text='')
svar2.grid(row=3,column=0,padx=10,pady=10,sticky=E)

vindu.mainloop()
mindatabase.close()
