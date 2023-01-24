from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Eksamenssjef',passwd='oblig2022',db='oblig2022')
def finn_studentnr():
    studentliste=[]
    stor=0

    let_markor=mindatabase.cursor()

    let_markor.execute("SELECT * FROM Student")

    for row in let_markor:
        studentliste+=[[row[0],row[1],row[2],row[3],row[4]]]

    let_markor.close()
    print(studentliste)#studentliste henter alle stundentnummer

    for row in range(0,len(studentliste),1):
        if int(studentliste[row][0])>stor:
            stor=int(studentliste[row][0])
    print(stor)#finner største studentnummer i DB
    stnr.set(stor+1)

def lagre_student():
    studentliste=[]
    
    studentnr=int(stnr.get())
    fornavn=fnavn.get()
    etternavn=enavn.get()
    epost=eposten.get()
    mobil=tlf.get()

    studentliste+=[studentnr,fornavn,etternavn,epost,mobil]

    print(studentliste) #lista er ok

    settinn_markor=mindatabase.cursor()

    settinn_student=("INSERT INTO Student"
                     "(Studentnr,Fornavn,Etternavn,Epost,Telefon)"
                     "VALUES(%s,%s,%s,%s,%s)")
    settinn_markor.execute(settinn_student,studentliste)
    mindatabase.commit()
    settinn_markor.close()
    

vindu=Tk()
vindu.title('Lagre ny Student')

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
ent_stnr=Entry(vindu,width=8,textvariable=stnr)
ent_stnr.grid(row=0,column=2,padx=5,pady=5,sticky=W)

fnavn=StringVar()
ent_fnavn=Entry(vindu,width=20,textvariable=fnavn)
ent_fnavn.grid(row=1,column=2,padx=5,pady=5,sticky=W)

enavn=StringVar()
ent_enavn=Entry(vindu,width=30,textvariable=enavn)
ent_enavn.grid(row=2,column=2,padx=5,pady=5,sticky=W)

eposten=StringVar()
ent_epost=Entry(vindu,width=30,textvariable=eposten)
ent_epost.grid(row=3,column=2,padx=5,pady=5,sticky=W)

tlf=StringVar()
ent_tlf=Entry(vindu,width=8,textvariable=tlf)
ent_tlf.grid(row=4,column=2,padx=5,pady=5,sticky=W)

btn_lagre=Button(vindu,text='Lagre',command=lagre_student)
btn_lagre.grid(row=5,column=3,padx=5,pady=5,sticky=SE)

btn_tilbake=Button(vindu,text='Tilbake',command=vindu.destroy)
btn_tilbake.grid(row=6,column=3,padx=5,pady=5,sticky=SE)

