from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
    user='Eksamenssjef',passwd='oblig2022',db='oblig2022')


def sjekk_student():
    studentliste=[]

    sjekk_markor=mindatabase.cursor()

    sjekk_markor.execute("SELECT * FROM Student")

    for row in sjekk_markor:
        studentliste+=[[row[0],row[1],row[2],row[3],row[4]]]
    sjekk_markor.close()

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

def oppdater_student():
    studentnr=stnr.get()
    fornavn=fnavn.get()
    etternavn=enavn.get()
    epost=eposten.get()
    telefon=tlf.get()

    oppdater_markor=mindatabase.cursor()

    oppdatering=("UPDATE Student SET Fornavn=%s,Etternavn=%s,"
                 "Epost=%s,Telefon=%s WHERE Studentnr=%s")

    settinn=(fornavn,etternavn,epost,telefon,studentnr)

    oppdater_markor.execute(oppdatering,settinn)

    mindatabase.commit()
    svar.set('Oppdatert')

    oppdater_markor.close()



vindu=Tk()
vindu.title('Oppdater student')

lbl_stnr=Label(vindu,text='Oppgi studentnummer: ')
lbl_stnr.grid(row=0,column=0,padx=5,pady=5,sticky=W)

lbl_fnavn=Label(vindu,text='Oppgi fornavn: ')
lbl_fnavn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

lbl_enavn=Label(vindu,text='Oppgi etternavn: ')
lbl_enavn.grid(row=2,column=0,padx=5,pady=5,sticky=W)

lbl_epost=Label(vindu,text='Oppgi epost: ')
lbl_epost.grid(row=3,column=0,padx=5,pady=5,sticky=W)

lbl_tlf=Label(vindu,text='Oppgi telefon: ')
lbl_tlf.grid(row=4,column=0,padx=5,pady=5,sticky=W)

stnr=StringVar()
ent_stnr=Entry(vindu,width=6,textvariable=stnr)
ent_stnr.grid(row=0,column=2,padx=5,pady=5,sticky=W)

fnavn=StringVar()
ent_fnavn=Entry(vindu,width=30,textvariable=fnavn)
ent_fnavn.grid(row=1,column=2,padx=5,pady=5,sticky=W)

enavn=StringVar()
ent_enavn=Entry(vindu,width=20,textvariable=enavn)
ent_enavn.grid(row=2,column=2,padx=5,pady=5,sticky=W)

eposten=StringVar()
ent_epost=Entry(vindu,width=40,textvariable=eposten)
ent_epost.grid(row=3,column=2,padx=5,pady=5,sticky=W)

tlf=StringVar()
ent_tlf=Entry(vindu,width=8,textvariable=tlf)
ent_tlf.grid(row=4,column=2,padx=5,pady=5,sticky=W)

svar=StringVar()
ent_svar=Entry(vindu,width=9,state='readonly',textvariable=svar)
ent_svar.grid(row=5,column=2,padx=5,pady=5,sticky=E)

btn_sjekk=Button(vindu,text='Hent student',command=sjekk_student)
btn_sjekk.grid(row=0,column=3,padx=5,pady=5,sticky=E)

btn_oppdater=Button(vindu,text='Oppdater',command=oppdater_student)
btn_oppdater.grid(row=5,column=3,padx=5,pady=5,sticky=SE)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=6,column=3,padx=5,pady=5,sticky=SE)
