from tkinter import *
import mysql.connector

#oppretter forbindelse med databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
        user='sjefen22',passwd='sjefenpw',db='Arbeidsøkt2022')

#delprogram for å sjekke om varen finnes i tabellen i db
def hent_vare():

    #oppretter en tom (2-dim) liste
    vareliste=[]

    #oppretter markør og leser gjennom alle felt i db
    sjekk_markor=mindatabase.cursor()

    sjekk_markor.execute("SELECT * FROM Vare")

    #legger data fra db inn i en 2-dim liste
    for rad in sjekk_markor:
        vareliste+=[[rad[0],rad[1]]]

    #stenger markøren
    sjekk_markor.close()

    #de tre neste linjene er i tilfelle parameteroverføring
    #inn i en ny def()
    #return lista

#def sjekk_vare():
    #vareliste=hent_vare()

    #henter frem inputen for varenummer fra GUI
    #pass på om du skal hente inn varenummer som
    #string eller int...sjekk DB først
    nummeret=int(vnummer.get())

    #lager et flagg samt setter radverdien til 0
    funnet=False
    rad=0

    while funnet==False:
        if nummeret==vareliste[rad][0]:
            vnavn.set(vareliste[rad][1])
            funnet=True
        rad+=1
    
#delprogram for å oppdatare varen i tabellen i db
def oppdater_database():

    #henter frem inputen for varenummer samt ny betegnelse
    varenummer=vnummer.get()
    nyttvarenavn=nyttnavn.get()

    #oppretter markør 
    ny_markor=mindatabase.cursor()

    #variabel som oppdaterer varen i db
    oppdatering=('''UPDATE Vare SET Betegnelse=%s WHERE VareNr=%s''')

    #tupel som kommuniserer med variabelen ovenfor
    settinn=(nyttvarenavn,varenummer)

    #markøren utfører så endringen i databasen
    ny_markor.execute(oppdatering,settinn)

    #bekrefter endring i databasen
    mindatabase.commit()

    #utskriften som bekrefter at db er blitt oppdatert
    svaret.set('Oppdatert')
    #print(svaret.get())

    #stenger så av markøren
    ny_markor.close()

    
    
#GUI vindu
window=Tk()
window.title('Varer')


lbl_vnr=Label(window,text='Oppgi varenummer: ')
lbl_vnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

lbl_navn=Label(window,text='Varenavn: ')
lbl_navn.grid(row=1,column=0,padx=5,pady=5,sticky=E)

lbl_nyttnavn=Label(window,text='Oppgi nytt varenavn: ')
lbl_nyttnavn.grid(row=2,column=0,padx=5,pady=5,sticky=E)

vnummer=StringVar()
ent_vnr=Entry(window,width=5,textvariable=vnummer)
ent_vnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

vnavn=StringVar()
ent_navn=Entry(window,width=8,state='readonly',textvariable=vnavn)
ent_navn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

nyttnavn=StringVar()
ent_nyttnavn=Entry(window,width=8,textvariable=nyttnavn)
ent_nyttnavn.grid(row=2,column=1,padx=5,pady=5,sticky=W)

svaret=StringVar()
ent_svar=Entry(window,state='readonly',textvariable=svaret)
ent_svar.grid(row=4,column=1,padx=5,pady=5,sticky=E)

btn_sjekk=Button(window,text='Sjekk vare',command=hent_vare)
btn_sjekk.grid(row=1,column=2,padx=5,pady=5,sticky=W)

btn_lagre=Button(window,text='Lagre',command=oppdater_database)
btn_lagre.grid(row=2,column=2,padx=5,pady=5,sticky=W)

btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=4,column=2,padx=5,pady=5,sticky=W)

window.mainloop()
mindatabase.close()
