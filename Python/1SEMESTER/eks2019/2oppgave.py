#GUI til skatt
from tkinter import*

def beregn_skatt():#Selve koden for beregning av skatt som blir vist i gui-vinduet
    lonnsinntekt=int(lonnsinntekten.get())
    #marginal_skatt=marginalskatt*100

    if lonnsinntekt>=964801:
        marginalskatt=0.464
    else:
        if lonnsinntekt>=617501:
            marginalskatt=0.434
        else:
            if lonnsinntekt>=245651:
                marginalskatt=0.344
            else:
                if lonnsinntekt>=224001:
                    marginalskatt=0.321
                else:
                    if lonnsinntekt>=174501:
                        marginalskatt=222
                    else:
                        if lonnsinntekt>=102819:
                            marginalskatt=0.203
    if lonnsinntekt>=102819:
        marginalskatten.set(format(marginalskatt*100,'.2f'))

#Kode for utseende på gui-vinduet
window=Tk()
window.title('Marginalskattkalkulator')

lbl_lonnsinntekten=Label(window, text='Lønnsinntekt:')
lbl_lonnsinntekten.grid(row=0, column=0, padx=10, pady=15)

lonnsinntekten=StringVar()
ent_lonnsinntekten=Entry(window, width=10, textvariable=lonnsinntekten)
ent_lonnsinntekten.grid(row=0, column=1, padx=10, pady=15)

btn_beregn=Button(window, text='Beregn marginalskattprosen', command=beregn_skatt)
btn_beregn.grid(row=0, column=2, padx=10, pady=15)

lbl_marginalskatten=Label(window, text='Marginalskatt:')
lbl_marginalskatten.grid(row=1, column=0, padx=10, pady=15)

marginalskatten=StringVar()
ent_marginalskatten=Entry(window, width=10, state='readonly',textvariable=marginalskatten)
ent_marginalskatten.grid(row=1, column=1, padx=10, pady=15)

btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=2, column=3, padx=5, pady=15)

window.mainloop()
