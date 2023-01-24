from tkinter import *

vindu=Tk()
vindu.title('Lagre eksamensresultat')

lbl_stnr=Label(vindu,text='Oppgi studentnummer: ')
lbl_stnr.grid(row=0,column=0,padx=5,pady=5,sticky=W)

lbl_emne=Label(vindu,text='Oppgi emnekode: ')
lbl_emne.grid(row=1,column=0,padx=5,pady=5,sticky=W)

lbl_dato=Label(vindu,text='Oppgi eksamensdato: ')
lbl_dato.grid(row=2,column=0,padx=5,pady=5,sticky=W)

lbl_karakter=Label(vindu,text='Oppgi eksamenskarakter: ')
lbl_karakter.grid(row=3,column=0,padx=5,pady=5,sticky=W)

ent_stnr=Entry(vindu,width=8)
ent_stnr.grid(row=0,column=2,padx=5,pady=5,sticky=W)

ent_emne=Entry(vindu,width=8)
ent_emne.grid(row=1,column=2,padx=5,pady=5,sticky=W)

ent_dato=Entry(vindu,width=10)
ent_dato.grid(row=2,column=2,padx=5,pady=5,sticky=W)

ent_karakter=Entry(vindu,width=2)
ent_karakter.grid(row=3,column=2,padx=5,pady=5,sticky=W)

btn_lagre=Button(vindu,text='Lagre')
btn_lagre.grid(row=5,column=3,padx=5,pady=5,sticky=SE)

btn_tilbake=Button(vindu,text='Tilbake',command=vindu.destroy)
btn_tilbake.grid(row=6,column=3,padx=5,pady=5,sticky=SE)

