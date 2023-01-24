from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
        user='Eksamenssjef',passwd='oblig2022',db='oblig2022')

def finn_emne(event):
    valgt=lst_eksamen.get(lst_eksamen.curselection())
    hent_markor=mindatabase.cursor()

    hent_markor.execute("SELECT * FROM Eksamen")

    for row in hent_markor:
        if valgt==row[0]:
            dato.set(row[1])
            rom.set(row[2])
    hent_markor.close()

markor=mindatabase.cursor()

markor.execute("SELECT * FROM Eksamen")

liste=[]
for row in markor:
    liste+=[row[0]]

vindu2=Tk()
vindu2.title('test')

#Oppretter scroll
y_scroll=Scrollbar(vindu2,orient=VERTICAL)
y_scroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

#Oppretter listeboks
innhold_i_lst_eksamen=StringVar()
lst_eksamen=Listbox(vindu2,width=30,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)

innhold_i_lst_eksamen.set(tuple(liste))
y_scroll['command']=lst_eksamen.yview


lbl_dato=Label(vindu2,text='Datoen er:')
lbl_dato.grid(row=0,column=3,padx=5,pady=5,sticky=E)

lbl_rom=Label(vindu2,text='Romnummeret er:')
lbl_rom.grid(row=1,column=3,padx=5,pady=5,sticky=E)

dato=StringVar()
ent_dato=Entry(vindu2,width=11,state='readonly',textvariable=dato)
ent_dato.grid(row=0,column=4,padx=5,pady=5,sticky=W)

rom=StringVar()
ent_rom=Entry(vindu2,width=10,state='readonly',textvariable=rom)
ent_rom.grid(row=1,column=4,padx=5,pady=5,sticky=W)

lst_eksamen.bind('<<ListboxSelect>>',finn_emne)

btn_hent=Button(vindu2,text='avslutt',command=vindu2.destroy)
btn_hent.grid(row=4,column=3,padx=5,pady=5,sticky=SE)

vindu2.mainloop()
    

mindatabase.close()


# Listbox:
#for å få emnekode og dato på samme linje i listeboksen, må liste=[[row][0]] (være todimensjonal)
#etter det må du også definere valgt i finn_emne, altså if valgt[0]=...













