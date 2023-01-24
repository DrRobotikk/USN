#Program for å lage GUI til delprogram beregn_porto
from tkinter import*

#Selve koden for beregning av porto, som skal vises i GUI-vinduet
#Den blir koblet sammen med entries, labels og buttons vha. "get" og "set"
def beregn_porto():
    vekt=int(vekta.get())#variabel for get settes før if statement
    #resten av koden skrives akkurat som i oppgaveteksten

    if vekt<=20:
        porto=17
    elif vekt<=50:
        porto=24
    elif vekt<=100:
        porto=27
    elif vekt<=350:
        porto=45
    elif vekt<=100:
        porto=88
    else:
        porto=125
    portoen.set(porto)# Variabel for "set" settes etter if-statement

#Her er koden for GUI-vinduet
window=Tk()
window.title('Portokalkulator')

lbl_vekt=Label(window, text='Forsendelsens vekt (i gram):')
lbl_vekt.grid(row=0,column=0,padx=10,pady=15)

vekta=StringVar()
ent_vekt=Entry(window,width=10, textvariable=vekta)
ent_vekt.grid(row=0, column=1,padx=10,pady=15)

btn_beregn=Button(window, text='Beregn Porto', command=beregn_porto)
btn_beregn.grid(row=0, column=3, padx=10, pady=15)

lbl_porto=Label(window,text='Porto:')
lbl_porto.grid(row=1, column=0, padx=10,pady=15)

portoen=StringVar()
ent_porto=Entry(window,width=5, state='readonly', textvariable=portoen)
ent_porto.grid(row=1, column=1, columnspan=2 ,pady=15)

btn_avslutt=Button(window,text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=2,column=3, padx=10, pady=15)

window.mainloop()
