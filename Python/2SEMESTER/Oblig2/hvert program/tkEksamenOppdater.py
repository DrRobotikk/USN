from tkinter import *

vindu=Tk()
vindu.title('Oppdater eksamen')

lbl_emne=Label(vindu,text='Oppgi emnekode: ')
lbl_emne.grid(row=0,column=0,padx=5,pady=5,sticky=W)

lbl_dato=Label(vindu,text='Oppgi eksamensdato: ')
lbl_dato.grid(row=1,column=0,padx=5,pady=5,sticky=W)

lbl_romnr=Label(vindu,text='Oppgi romnummer: ')
lbl_romnr.grid(row=2,column=0,padx=5,pady=5,sticky=W)

ent_emne=Entry(vindu,width=8)
ent_emne.grid(row=0,column=2,padx=5,pady=5,sticky=W)

ent_dato=Entry(vindu,width=10)
ent_dato.grid(row=1,column=2,padx=5,pady=5,sticky=W)

ent_romnr=Entry(vindu,width=5)
ent_romnr.grid(row=2,column=2,padx=5,pady=5,sticky=W)

btn_oppdater=Button(vindu,text='Oppdater')
btn_oppdater.grid(row=5,column=3,padx=5,pady=5,sticky=SE)

btn_avslutt=Button(vindu,text='Avslutt',command=vindu.destroy)
btn_avslutt.grid(row=6,column=3,padx=5,pady=5,sticky=SE)
