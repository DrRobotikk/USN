from tkinter import *
import mysql.connector


def lagre_lista_i_database():
    #henter inn inputten fra gui
    nummeret=int(vnummer.get())
    navnet=vnavn.get()
    
    #oppretter en liste
    liste=[]

    #oppretter forbindelse med databasen
    mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='sjefen22',passwd='sjefenpw',db='Arbeidsøkt2022')

    inn_markor=mindatabase.cursor()

    #variabel som sier at databasen skal oppdateres
    inn_vare=("INSERT INTO VARE"
              "(VareNr,Betegnelse)"
              "VALUES(%s,%s)")

    #setter inn verdiene som skal lagres i databasen, inn i vår liste
    liste+=[nummeret,navnet]

    #markøren som utfører lagring av variabelen inn_vare og lista i databasen
    inn_markor.execute(inn_vare,liste)

    #bekrefter lagring i databasen
    mindatabase.commit()

    #kontrollprint
    print(liste)

    inn_markor.close()
    mindatabase.close()


#GUI vindu
window=Tk()
window.title('Varer')


lbl_vnr=Label(window,text='Oppgi varenummer: ')
lbl_vnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

lbl_navn=Label(window,text='Oppgi varenavn: ')
lbl_navn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

vnummer=StringVar()
ent_vnr=Entry(window,width=5,textvariable=vnummer)
ent_vnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

vnavn=StringVar()
ent_navn=Entry(window,width=8,textvariable=vnavn)
ent_navn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

btn_lagre=Button(window,text='Lagre',command=lagre_lista_i_database)
btn_lagre.grid(row=3,column=2,padx=5,pady=5,sticky=W)

window.mainloop()
