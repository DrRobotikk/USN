#PRG1100-2022 vindu ny vare

from tkinter import *
import mysql.connector

def lagre_liste():
    liste=[]
    varenr=int(vnr.get())
    navn=vnavn.get()
    pris=vpris.get()
    kategori=vkatnr.get()
    antall=vantall.get()
    hylle=vhylle.get()

    liste+=[varenr,navn,pris,kategori,antall,hylle]    
    
    mindatabase=mysql.connector.connect(host='localhost',port=3306,
        user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

    inn_markor=mindatabase.cursor()

    inn_vare=("INSERT INTO Vare"
              "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
              "VALUES(%s,%s,%s,%s,%s,%s)")

    inn_markor.execute(inn_vare,liste)
    mindatabase.commit()

    print(liste)

    inn_markor.close()
    mindatabase.close()
    

window=Tk()
window.title("Nye varer")

lbl_varenr=Label(window,text='Oppgi varenr: ')
lbl_varenr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

lbl_varenavn=Label(window,text='Oppgi varenavn: ')
lbl_varenavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)

lbl_pris=Label(window,text='Oppgi pris: ')
lbl_pris.grid(row=2,column=0,padx=5,pady=5,sticky=E)

lbl_katnr=Label(window,text='Oppgi kategorinr: ')
lbl_katnr.grid(row=3,column=0,padx=5,pady=5,sticky=E)

lbl_antall=Label(window,text='Oppgi antall: ')
lbl_antall.grid(row=4,column=0,padx=5,pady=5,sticky=E)

lbl_hylle=Label(window,text='Oppgi hylleplassering: ')
lbl_hylle.grid(row=5,column=0,padx=5,pady=5,sticky=E)

vnr=StringVar()
ent_vnr=Entry(window,width=6,textvariable=vnr)
ent_vnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

vnavn=StringVar()
ent_vnavn=Entry(window,width=20,textvariable=vnavn)
ent_vnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

vpris=StringVar()
ent_vpris=Entry(window,width=5,textvariable=vpris)
ent_vpris.grid(row=2,column=1,padx=5,pady=5,sticky=W)

vkatnr=StringVar()
ent_vkatnr=Entry(window,width=4,textvariable=vkatnr)
ent_vkatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

vantall=StringVar()
ent_vantall=Entry(window,width=4,textvariable=vantall)
ent_vantall.grid(row=4,column=1,padx=5,pady=5,sticky=W)

vhylle=StringVar()
ent_vhylle=Entry(window,width=4,textvariable=vhylle)
ent_vhylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

#lager en knapp for å lagre ny vare
btn_lagre=Button(window,text='Lagre',command=lagre_liste)
btn_lagre.grid(row=6,column=2,padx=5,pady=5,sticky=W)

btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=7,column=2,padx=5,pady=5,sticky=W)

window.mainloop()

