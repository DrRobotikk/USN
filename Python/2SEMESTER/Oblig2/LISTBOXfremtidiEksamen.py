from tkinter import *
from tkinter.ttk import Combobox
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Eksamenssjef',passwd='oblig2022',db='oblig2022')

def sjekk_fremtidig_eksamen(event):
    valgt=lst_emnekode.get(lst_emnekode.curselection())


    sjekk_markor=mindatabase.cursor()

    sjekk_markor.execute('''
                        SELECT *
                        FROM Eksamen
                        ''')

    for row in sjekk_markor:
        if valgt==row[0]:
            dato.set(row[1])
    sjekk_markor.close()
    
markor=mindatabase.cursor()

markor.execute('''
                SELECT *
                FROM Eksamen
                ''')

emneliste=[]
for row in markor:
    emneliste+=[row[0]]
markor.close()

vindu=Tk()
vindu.title('Fremtidige eksamener')

innhold_emnekode=StringVar()
lst_emnekode=Listbox(vindu,width=20,height=10,listvariable=innhold_emnekode)
lst_emnekode.grid(row=0,column=0,padx=10,pady=10,sticky=W)

innhold_emnekode.set(tuple(emneliste))

dato=StringVar()
ent_dato=Entry(vindu,width=20,textvariable=dato)
ent_dato.grid(row=0,column=1,padx=10,pady=10,sticky=E)

lst_emnekode.bind('<<ListboxSelect>>',sjekk_fremtidig_eksamen)

vindu.mainloop()
mindatabase.close()
