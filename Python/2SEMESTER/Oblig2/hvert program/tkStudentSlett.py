from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Eksamenssjef',passwd='oblig2022',db='oblig2022')

def finn_student():
    studentliste=[]

    lete_markor=mindatabase.cursor()

    lete_markor.execute("SELECT * FROM Student")

    for row in lete_markor:
        studentliste+=[[row[0],row[1],row[2],row[3],row[4]]]
    lete_markor.close()

    studentnr=stnr.get()

    funnet=False
    row=0

    while funnet==False:
        if studentnr==studentliste[row][0]:
            fnavn.set(studentliste[row][1])
            enavn.set(studentliste[row][2])
            eposten.set(studentliste[row][3])
            tlf.set(studentliste[row][4])
            funnet=True
        row+=1


    
def slett_student():
    studentnr=stnr.get()

    slett_markor=mindatabase.cursor()

    slett_setning=("DELETE FROM Student WHERE Studentnr=%s")

    sletting=(studentnr,)

    slett_markor.execute(slett_setning,sletting)

    mindatabase.commit()

    svar.set('Oppdatert')
    slett_markor.close()


vindu4=Tk()
vindu4.title('Slett student')

lbl_stnr=Label(vindu4,text='Oppgi studentnummer: ')
lbl_stnr.grid(row=0,column=0,padx=5,pady=5,sticky=W)

lbl_fnavn=Label(vindu4,text='Oppgi fornavn: ')
lbl_fnavn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

lbl_enavn=Label(vindu4,text='Oppgi etternavn: ')
lbl_enavn.grid(row=2,column=0,padx=5,pady=5,sticky=W)

lbl_epost=Label(vindu4,text='Oppgi epost: ')
lbl_epost.grid(row=3,column=0,padx=5,pady=5,sticky=W)

lbl_tlf=Label(vindu4,text='Oppgi telefon: ')
lbl_tlf.grid(row=4,column=0,padx=5,pady=5,sticky=W)

stnr=StringVar()
ent_stnr=Entry(vindu4,width=8,textvariable=stnr)
ent_stnr.grid(row=0,column=2,padx=5,pady=5,sticky=W)

fnavn=StringVar()
ent_fnavn=Entry(vindu4,width=20,textvariable=fnavn)
ent_fnavn.grid(row=1,column=2,padx=5,pady=5,sticky=W)

enavn=StringVar()
ent_enavn=Entry(vindu4,width=30,textvariable=enavn)
ent_enavn.grid(row=2,column=2,padx=5,pady=5,sticky=W)

eposten=StringVar()
ent_epost=Entry(vindu4,width=30,textvariable=eposten)
ent_epost.grid(row=3,column=2,padx=5,pady=5,sticky=W)

tlf=StringVar()
ent_tlf=Entry(vindu4,width=8,textvariable=tlf)
ent_tlf.grid(row=4,column=2,padx=5,pady=5,sticky=W)

svar=StringVar()
ent_svar=Entry(vindu4,width=9,state='readonly',textvariable=svar)
ent_svar.grid(row=5,column=2,padx=5,pady=5,sticky=E)

btn_sjekk=Button(vindu4,text='Sjekk student',command=finn_student)
btn_sjekk.grid(row=0,column=3,padx=5,pady=5,sticky=E)

btn_slett=Button(vindu4,text='Slett',command=slett_student)
btn_slett.grid(row=5,column=3,padx=5,pady=5,sticky=SE)

btn_avslutt=Button(vindu4,text='Avslutt',command=vindu4.destroy)
btn_avslutt.grid(row=6,column=3,padx=5,pady=5,sticky=SE)
