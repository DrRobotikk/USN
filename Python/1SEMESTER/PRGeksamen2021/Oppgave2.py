#Program for å lage GUI til fartsbotkalkulator

from tkinter import*

#Selve koden for fartsbotkalkulator, som skal vises i GUI-vinduet
def fartsbot():
    fartsgrense=70

    din_fart=int(hastighet.get())
    if din_fart>=(fartsgrense+35):
        forelegg=9950
    else:
        if din_fart>=(fartsgrense+25):
            forelegg=6250
        else:
            if din_fart>=(fartsgrense+15):
                forelegg=3300
            else:
                if din_fart>=(fartsgrense+5):
                    forelegg=750
                else:
                    forelegg='Ingen'
    forelegget.set(forelegg)

#Koden for GUI-vinduet med inndatafelt, utdatafelt og knapper
window=Tk()
window.title('Fartsbotkalkulator')

lbl_hastighet=Label(window, text='Målt hastighet/din fart i km/t:')
lbl_hastighet.grid(row=0,column=0,padx=10,pady=15)

hastighet=StringVar()
ent_hastighet=Entry(window,width=5, textvariable=hastighet)
ent_hastighet.grid(row=0, column=1,padx=10,pady=15)

btn_beregn=Button(window, text='Beregn forelegg', command=fartsbot)
btn_beregn.grid(row=0, column=3, padx=10, pady=15)

lbl_forelegget=Label(window,text='Forelegg:')
lbl_forelegget.grid(row=1, column=0, padx=10,pady=15)

forelegget=StringVar()
ent_forelegget=Entry(window,width=6, state='readonly', textvariable=forelegget)
ent_forelegget.grid(row=1, column=1, columnspan=2 ,pady=15)

btn_avslutt=Button(window,text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=2,column=3, padx=10, pady=15)

window.mainloop()
