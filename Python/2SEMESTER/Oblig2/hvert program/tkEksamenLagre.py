from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Eksamenssjef',passwd='oblig2022',db='oblig2022')

def finn_ledig_rom(event):
    valgt=lst_rom.get(lst_rom.curselection())
    
    lete_markor=mindatabase.cursor()

    lete_markor.execute("SELECT * FROM Rom")

    for row in lete_markor:
        if valgt==row[0]:
            antall.set(row[1])
     
    lete_markor.close()

def finn_emne(event):
    valgt_emne=lst_emne.get(lst_emne.curselection())
    emne_markor=mindatabase.cursor()

    emne_markor.execute("SELECT * FROM Emne")

    for row in emne_markor:
        if valgt_emne==row[0]:
            emnenavn.set(row[1])
            poeng.set(row[2])
    emne_markor.close()            
    

def lagre_eksamen():
    eks_liste=[]


markor=mindatabase.cursor()
markor.execute("SELECT * FROM Rom")

liste=[]
emneliste=[]
for row in markor:
    liste+=[row[0]]

markor2=mindatabase.cursor()
markor2.execute("SELECT * FROM Emne")

for row in markor2:
    emneliste+=[[row[0],row[1],row[2]]]
print(emneliste)

vindu=Tk()
vindu.title('Lagre ny eksamen')

y_scroll=Scrollbar(vindu,orient=VERTICAL)
y_scroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

innhold_i_lst_rom=StringVar()
lst_rom=Listbox(vindu,width=15,height=8,listvariable=innhold_i_lst_rom,yscrollcommand=y_scroll.set)
lst_rom.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)

innhold_i_lst_rom.set(tuple(liste))
y_scroll['command']=lst_rom.yview



y2_scroll=Scrollbar(vindu,orient=VERTICAL)
y2_scroll.grid(row=0,column=4,rowspan=10,padx=(0,100),pady=5,sticky=NS)

innhold_i_lst_emne=StringVar()
lst_emne=Listbox(vindu,width=15,height=8,listvariable=innhold_i_lst_emne,yscrollcommand=y2_scroll.set)
lst_emne.grid(row=0,column=3,rowspan=10,padx=(100,0),pady=5,sticky=E)

innhold_i_lst_emne.set(tuple(emneliste))
y2_scroll['command']=lst_emne.yview

antall=StringVar()
ent_antall=Entry(vindu,width=6,state='readonly',textvariable=antall)
ent_antall.grid(row=2,column=3,padx=5,pady=5,sticky=W)

emnenavn=StringVar()
ent_emnenavn=Entry(vindu,width=30,state='readonly',textvariable=emnenavn)
ent_emnenavn.grid(row=2,column=5,padx=5,pady=5,sticky=W)

poeng=StringVar()
ent_poeng=Entry(vindu,width=6,state='readonly',textvariable=poeng)
ent_poeng.grid(row=3,column=5,padx=5,pady=5,sticky=W)

btn_lagre=Button(vindu,text='Lagre',command=lagre_eksamen)
btn_lagre.grid(row=5,column=6,padx=5,pady=5,sticky=SE)

btn_tilbake=Button(vindu,text='Tilbake',command=vindu.destroy)
btn_tilbake.grid(row=6,column=6,padx=5,pady=5,sticky=SE)

lst_rom.bind('<<ListboxSelect>>',finn_ledig_rom)
lst_emne.bind('<<ListboxSelect>>',finn_emne)

vindu.mainloop()
mindatabase.close()
