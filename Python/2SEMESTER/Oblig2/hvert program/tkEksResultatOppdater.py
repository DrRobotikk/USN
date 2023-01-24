from tkinter import *

vindu=Tk()
vindu.title('Oppdater eksamensresultat')

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

ent_stnr=Entry(vindu,width=8)
ent_stnr.grid(row=0,column=2,padx=5,pady=5,sticky=W)

ent_fnavn=Entry(vindu,width=20)
ent_fnavn.grid(row=1,column=2,padx=5,pady=5,sticky=W)

ent_enavn=Entry(vindu,width=30)
ent_enavn.grid(row=2,column=2,padx=5,pady=5,sticky=W)

ent_epost=Entry(vindu,width=30)
ent_epost.grid(row=3,column=2,padx=5,pady=5,sticky=W)

ent_tlf=Entry(vindu,width=8)
ent_tlf.grid(row=4,column=2,padx=5,pady=5,sticky=W)

btn_oppdater=Button(vindu,text='Oppdater')
btn_oppdater.grid(row=5,column=3,padx=5,pady=5,sticky=SE)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=6,column=3,padx=5,pady=5,sticky=SE)
