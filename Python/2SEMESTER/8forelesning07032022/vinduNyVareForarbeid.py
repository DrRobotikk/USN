#PRG1100-2022 vindu ny vare

#Oppretter kobling mot Tk-bibliotek 
from tkinter import *

#Importerer database-kobling
import mysql.connector

def lagre_varer():
    settinn_markor=mindatabase.cursor

    settinn_markor.execute("INSERT INTO Vare"
                           "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                           "VALUES(%s,%s,%s,%s,%s,%s)")
    mindatabase.commit()

    settinn_markor.close()


#Oppretting av GUI og gir vinduet navnet "Nye varer"
window=Tk()
window.title("Nye varer")

#Varenummer
lbl_varenr=Label(window,text='Oppgi varenr: ')
lbl_varenr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

#Varenavn
lbl_varenavn=Label(window,text='Oppgi varenavn: ')
lbl_varenavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)

#Vareris
lbl_pris=Label(window,text='Oppgi pris: ')
lbl_pris.grid(row=2,column=0,padx=5,pady=5,sticky=E)

#Kategorinummer
lbl_katnr=Label(window,text='Oppgi kategorinr: ')
lbl_katnr.grid(row=3,column=0,padx=5,pady=5,sticky=E)

#Antall varer
lbl_antall=Label(window,text='Oppgi antall: ')
lbl_antall.grid(row=4,column=0,padx=5,pady=5,sticky=E)

#Hylleplassering av vare
lbl_hylle=Label(window,text='Oppgi hylleplassering: ')
lbl_hylle.grid(row=5,column=0,padx=5,pady=5,sticky=E)

#Indatafelt for varenummer
vnr=StringVar()
ent_vnr=Entry(window,width=6,textvariable=vnr)
ent_vnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

#Inndatafelt for varenavn
vnavn=StringVar()
ent_vnavn=Entry(window,width=20,textvariable=vnavn)
ent_vnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

#Inndatafelt for varepris
vpris=StringVar()
ent_vpris=Entry(window,width=5,textvariable=vpris)
ent_vpris.grid(row=2,column=1,padx=5,pady=5,sticky=W)

#Inndatafelt for kategorinummer
vkatnr=StringVar()
ent_vkatnr=Entry(window,width=4,textvariable=vkatnr)
ent_vkatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

#Inndatafelt for antall varer
vantall=StringVar()
ent_vantall=Entry(window,width=4,textvariable=vantall)
ent_vantall.grid(row=4,column=1,padx=5,pady=5,sticky=W)

#Inndatafelt for hylleplassering av varer
vhylle=StringVar()
ent_vhylle=Entry(window,width=4,textvariable=vhylle)
ent_vhylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

#Lager en knapp for å lagre ny vare
btn_lagre=Button(window,text='Lagre')
btn_lagre.grid(row=6,column=2,padx=5,pady=5,sticky=W)

#Avslutt-knapp
btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=8,column=2,padx=5,pady=5,sticky=W)

#Fortsetter vinduet så lenge brukeren ønsker
window.mainloop()

#Stenger av databasen etter bruk
mindatabase.close()
