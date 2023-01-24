from tkinter import *
def vindu_2():
    vindu2=Toplevel()
    vindu2.title('Applikasjonsvindu - vindu2')

    btn_tilbake2=Button(vindu2,text='Tilbake til hovedvindu',command=vindu2.destroy)
    btn_tilbake2.grid(row=2,column=6,padx=5,pady=25,sticky=E)

def vindu_3():
    vindu3=Toplevel()
    vindu3.title('Applikasjonsvindu - vindu3')

    btn_tilbake3=Button(vindu3,text='Tilbake til hovedvindu',command=vindu3.destroy)
    btn_tilbake3.grid(row=2,column=6,padx=5,pady=25,sticky=E)

def vindu_4():
    vindu4=Toplevel()
    vindu4.title('Applikasjonsvindu - vindu4')

    btn_tilbake4=Button(vindu4,text='Tilbake til hovedvindu',command=vindu4.destroy)
    btn_tilbake4.grid(row=2,column=6,padx=5,pady=25,sticky=E)

def main():
    hovedvindu=Tk()
    hovedvindu.title('Hovedvindu - meny')

    btn_vindu2=Button(hovedvindu,text='Vindu 2',command=vindu_2)
    btn_vindu2.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    btn_vindu3=Button(hovedvindu,text='Vindu 3',command=vindu_3)
    btn_vindu3.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    btn_vindu4=Button(hovedvindu,text='Vindu 4',command=vindu_4)
    btn_vindu4.grid(row=0,column=2,padx=5,pady=5,sticky=W)

    btn_avslutt=Button(hovedvindu,text='Avslutt',command=hovedvindu.destroy)
    btn_avslutt.grid(row=2,column=4,padx=5,pady=5,sticky=E)

    hovedvindu.mainloop()
main()
