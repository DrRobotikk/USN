from tkinter import*

def rulett():
    tallet=int(tall.get())
    if tallet<0 or tallet>36:
        farge.set('Ugyldig tall')
    else:
        if tallet==0:
            farge.set('Grønn')
        else:
            if tallet<=10:
                if (tallet%2)==0:
                    farge.set('Svart')
                else:
                    farge.set('Rød')
            else:
                if tallet<=18:
                    if (tallet%2)==0:
                        farge.set('Rød')
                    else:
                        farge.set('Svart')
                else:
                    if tallet<=28:
                        if (tallet%2)==0:
                            farge.set('Svart')
                        else:
                            farge.set('Rød')
                    else:
                        if tallet<=36:
                            if (tallet%2)==0:
                                farge.set('Rød')
                            else:
                                farge.set('Svart')


window=Tk()
window.title('Rulett')


lbl_tall=Label(window, text='Oppgi tall: ')
lbl_tall.grid(row=0, column=0, padx=100, pady=15)

tall=StringVar()
ent_tall=Entry(window, width=2, textvariable=tall)
ent_tall.grid(row=0, column=1, padx=100, pady=15)

farge=StringVar()
ent_farge=Entry(window, width=10, state='readonly', textvariable=farge)
ent_farge.grid(row=1, column=1, padx=100, pady=15)

btn_resultat=Button(window, text='Vis farge',command=rulett)
btn_resultat.grid(row=1, column=0, padx=100, pady=15)

btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=3, column=0, columnspan=2, pady=15)

window.mainloop()


















