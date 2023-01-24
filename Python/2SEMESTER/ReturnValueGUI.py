from tkinter import *

#Delprogram som tar seg av selve regnestykket
#setter inn variablene i parantes (kan hete noe annet også, som f.eks.verdi 1 og 2)
def summen(alder1,alder2):
    
    resultat=alder1+alder2
    
    #tar vare på resultatet
    return resultat


#delprogram som ber om input og viser resultatet fra def summen
def main():

    alder1=int(ent1.get())
    alder2=int(ent2.get())

    #returnerer resultat fra forrige def
    total=summen(alder1,alder2)

    #utskrift    
    lbl.config(text='Sammen er dere '+str(total)+' år gamle.')

#tk vindu
vindu=Tk()
vindu.title('Vindu')

lbl_1=Label(vindu,text='Oppgi alder 1')
lbl_1.grid(row=0,column=0,padx=5,pady=5,sticky=W)

ent1=StringVar()
ent_1=Entry(vindu,width=3,textvariable=ent1)
ent_1.grid(row=0,column=1,padx=5,pady=5)

lbl_2=Label(vindu,text='Oppgi alder 2')
lbl_2.grid(row=1,column=0,padx=5,pady=5,sticky=W)

ent2=StringVar()
ent_2=Entry(vindu,width=3,textvariable=ent2)
ent_2.grid(row=1,column=1,padx=5,pady=5)

lbl=Label(vindu,text='')
lbl.grid(row=2,column=0,padx=5,pady=5)

btn=Button(vindu,text='Beregn',command=main)
btn.grid(row=2,column=1,padx=5,pady=5,sticky=SE)

vindu.mainloop()
