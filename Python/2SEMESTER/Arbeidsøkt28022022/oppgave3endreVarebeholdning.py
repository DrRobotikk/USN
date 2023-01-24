#PRG1100-2022 endre varebeholdningen i database

from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
    user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

def sjekk_vare():
    vareliste=[]

    sjekk_markor=mindatabase.cursor()

    sjekk_markor.execute("SELECT * FROM Vare")

    for rad in sjekk_markor:
        vareliste+=[[rad[0],rad[1],rad[2],rad[3],rad[4],rad[5]]]

    sjekk_markor.close()
    #print(vareliste)
    
    varenummer=vnr.get()
    funnet=False
    rad=0

    while funnet==False and rad<=len(vareliste)-1:
        if varenummer==vareliste[rad][0]:
            vnavn.set(vareliste[rad][1])
            vpris.set(vareliste[rad][2])
            vkatnr.set(vareliste[rad][3])
            vantall.set(vareliste[rad][4])
            vhylle.set(vareliste[rad][5])
            funnet=True
        rad+=1
    
    
def lagre_vare():
    
    varenummer=vnr.get()
    ny_antall=vantall.get()

    ny_markor=mindatabase.cursor()

    oppdatering=("UPDATE Vare SET Antall=%s WHERE VNr=%s")

    settinn=(ny_antall,varenummer)

    ny_markor.execute(oppdatering,settinn)

    mindatabase.commit()

    svaret.set('Oppdatert')
    ny_markor.close()

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
ent_vnavn=Entry(window,width=20,state='readonly',textvariable=vnavn)
ent_vnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

vpris=StringVar()
ent_vpris=Entry(window,width=5,state='readonly',textvariable=vpris)
ent_vpris.grid(row=2,column=1,padx=5,pady=5,sticky=W)

vkatnr=StringVar()
ent_vkatnr=Entry(window,width=4,state='readonly',textvariable=vkatnr)
ent_vkatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

vantall=StringVar()
ent_vantall=Entry(window,width=4,textvariable=vantall)
ent_vantall.grid(row=4,column=1,padx=5,pady=5,sticky=W)

vhylle=StringVar()
ent_vhylle=Entry(window,width=5,state='readonly',textvariable=vhylle)
ent_vhylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

svaret=StringVar()
ent_svar=Entry(window,state='readonly',textvariable=svaret)
ent_svar.grid(row=6,column=0,padx=5,pady=5,sticky=E)

#knappen som sjekker om varen finnes
btn_sjekk=Button(window,text='Sjekk vare',command=sjekk_vare)
btn_sjekk.grid(row=0,column=2,padx=5,pady=5,sticky=W)

#Knapp for å lagre ny vare
btn_lagre=Button(window,text='Lagre',command=lagre_vare)
btn_lagre.grid(row=6,column=2,padx=5,pady=5,sticky=W)

btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=7,column=2,padx=5,pady=5,sticky=W)

window.mainloop()
mindatabase.close()

