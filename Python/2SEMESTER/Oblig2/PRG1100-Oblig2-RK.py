#PRG1100-Oblig2-RK

#Importerer tk-komponenter og mysql-kobling
from tkinter import *
import mysql.connector

#Oppretter kobling mellom Python og MySQL-Databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Eksamenssjef',passwd='oblig2022',db='oblig2022')


#Delprogram for å lagre en ny student i Student-tabellen
def vindu_lagre_student():

    #Delprogram som finner det største studentnummeret i Student-tabellen
    #og plusser på en for å generere et nytt studentnummer
    def lag_nytt_studentnr():
        stor=0
        stor_markor=mindatabase.cursor()

        stor_markor.execute('''
                            SELECT MAX(Studentnr)
                            FROM Student
                            ''')

        for row in stor_markor:
            stor=int(row[0])
        stnr.set(stor+1)

    #Delprogram som utfører lagring av student i Student-tabellen
    def lagre_student():
        studentliste=[]
        studentnr=int(stnr.get())
        fornavn=fnavn.get()
        etternavn=enavn.get()
        epost=eposten.get()
        mobil=tlf.get()
        
        studentliste+=[studentnr,fornavn,etternavn,epost,mobil]
                
        settinn_markor=mindatabase.cursor()
        settinn_student=('''
                        INSERT INTO Student
                        (Studentnr,Fornavn,Etternavn,Epost,Telefon)
                        VALUES(%s,%s,%s,%s,%s)
                        ''')
        
        settinn_markor.execute(settinn_student,studentliste)
        mindatabase.commit()
        
        lbl_svar.config(text='Lagret')
        fnavn.set('')
        enavn.set('')
        eposten.set('')
        tlf.set('')
        settinn_markor.close()
        lag_nytt_studentnr()

    #Oppretter vindu som viser informasjon som studenten lagres med
    vindu2=Toplevel()
    vindu2.title('Lagre ny Student')
    
    lbl_stnr=Label(vindu2,text='Oppgi studentnummer: ')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    
    lbl_fnavn=Label(vindu2,text='Oppgi fornavn: ')
    lbl_fnavn.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    
    lbl_enavn=Label(vindu2,text='Oppgi etternavn: ')
    lbl_enavn.grid(row=2,column=0,padx=10,pady=10,sticky=W)
    
    lbl_epost=Label(vindu2,text='Oppgi epost: ')
    lbl_epost.grid(row=3,column=0,padx=10,pady=10,sticky=W)
    
    lbl_tlf=Label(vindu2,text='Oppgi telefon: ')
    lbl_tlf.grid(row=4,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu2,text='')
    lbl_svar.grid(row=5,column=2,sticky=E)
    
    stnr=StringVar()
    ent_stnr=Entry(vindu2,width=8,state='readonly',textvariable=stnr)
    ent_stnr.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
    fnavn=StringVar()
    ent_fnavn=Entry(vindu2,width=20,textvariable=fnavn)
    ent_fnavn.grid(row=1,column=2,padx=10,pady=10,sticky=W)
    
    enavn=StringVar()
    ent_enavn=Entry(vindu2,width=30,textvariable=enavn)
    ent_enavn.grid(row=2,column=2,padx=10,pady=10,sticky=W)
    
    eposten=StringVar()
    ent_epost=Entry(vindu2,width=30,textvariable=eposten)
    ent_epost.grid(row=3,column=2,padx=10,pady=10,sticky=W)
    
    tlf=StringVar()
    ent_tlf=Entry(vindu2,width=8,textvariable=tlf)
    ent_tlf.grid(row=4,column=2,padx=10,pady=10,sticky=W)
    
    btn_lagre=Button(vindu2,text='Lagre',command=lagre_student)
    btn_lagre.grid(row=5,column=3,padx=10,pady=10,sticky=SE)
    
    btn_tilbake=Button(vindu2,text='Tilbake',command=vindu2.destroy)
    btn_tilbake.grid(row=6,column=3,padx=10,pady=10,sticky=SE)

    lag_nytt_studentnr()


#Delprogram for oppdatering av studentinformasjon i Student-tabellen
def vindu_oppdater_student():

    #Delprogram som finner informasjon om studenten
    def sjekk_student():
        studentliste=[]
        studentnr=str(stnr.get())
        
        sjekk_markor=mindatabase.cursor()
        lete=('''
                SELECT *
                FROM Student
                WHERE Studentnr=%s
                ''')

        sjekk_markor.execute(lete%studentnr)
        
        for row in sjekk_markor:
            studentliste+=[[row[0],row[1],row[2],row[3],row[4]]]
            
            fnavn.set(row[1])
            enavn.set(row[2])
            eposten.set(row[3])
            tlf.set(row[4])
        sjekk_markor.close()

    #Delprogram som utfører oppdatering av informasjon om studenten i Student-tabellen
    def oppdater_student():
        studentnr=stnr.get()
        fornavn=fnavn.get()
        etternavn=enavn.get()
        epost=eposten.get()
        telefon=tlf.get()
        
        oppdater_markor=mindatabase.cursor()
        oppdatering=('''
                    UPDATE Student
                    SET Fornavn=%s,Etternavn=%s,Epost=%s,Telefon=%s
                    WHERE Studentnr=%s
                    ''')
        
        settinn=(fornavn,etternavn,epost,telefon,studentnr)
        oppdater_markor.execute(oppdatering,settinn)
        
        mindatabase.commit()
        lbl_svar.config(text='Oppdatert')

        stnr.set('')
        fnavn.set('')
        enavn.set('')
        eposten.set('')
        tlf.set('')
        oppdater_markor.close()

    #Oppretter vindu som viser studenten det skal oppdateres informasjon om
    vindu3=Toplevel()
    vindu3.title('Oppdater student')
    
    lbl_stnr=Label(vindu3,text='Oppgi studentnummer: ')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    
    lbl_fnavn=Label(vindu3,text='Oppgi fornavn: ')
    lbl_fnavn.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    
    lbl_enavn=Label(vindu3,text='Oppgi etternavn: ')
    lbl_enavn.grid(row=2,column=0,padx=10,pady=10,sticky=W)
    
    lbl_epost=Label(vindu3,text='Oppgi epost: ')
    lbl_epost.grid(row=3,column=0,padx=10,pady=10,sticky=W)
    
    lbl_tlf=Label(vindu3,text='Oppgi telefon: ')
    lbl_tlf.grid(row=4,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu3,text='')
    lbl_svar.grid(row=5,column=2,sticky=E)
    
    stnr=StringVar()
    ent_stnr=Entry(vindu3,width=6,textvariable=stnr)
    ent_stnr.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
    fnavn=StringVar()
    ent_fnavn=Entry(vindu3,width=30,textvariable=fnavn)
    ent_fnavn.grid(row=1,column=2,padx=10,pady=10,sticky=W)
    
    enavn=StringVar()
    ent_enavn=Entry(vindu3,width=20,textvariable=enavn)
    ent_enavn.grid(row=2,column=2,padx=10,pady=10,sticky=W)
    
    eposten=StringVar()
    ent_epost=Entry(vindu3,width=40,textvariable=eposten)
    ent_epost.grid(row=3,column=2,padx=10,pady=10,sticky=W)
    
    tlf=StringVar()
    ent_tlf=Entry(vindu3,width=8,textvariable=tlf)
    ent_tlf.grid(row=4,column=2,padx=10,pady=10,sticky=W)
    
    btn_sjekk=Button(vindu3,text='Hent student',command=sjekk_student)
    btn_sjekk.grid(row=0,column=3,padx=10,pady=10,sticky=E)
    
    btn_oppdater=Button(vindu3,text='Oppdater',command=oppdater_student)
    btn_oppdater.grid(row=5,column=3,padx=10,pady=10,sticky=SE)
    
    btn_avslutt=Button(vindu3,text='Tilbake',command=vindu3.destroy)
    btn_avslutt.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for sletting av en student
def vindu_slett_student():

    #Delprogram som finner informasjon om studenten som skal slettes
    def finn_student():
        studentliste=[]
        studentnr=str(stnr.get())
        
        sjekk_markor=mindatabase.cursor()
        lete=('''
                SELECT *
                FROM Student
                WHERE Studentnr=%s
                ''')

        sjekk_markor.execute(lete%studentnr)
        
        for row in sjekk_markor:
            studentliste+=[[row[0],row[1],row[2],row[3],row[4]]]
            
            fnavn.set(row[1])
            enavn.set(row[2])
            eposten.set(row[3])
            tlf.set(row[4])
        sjekk_markor.close()

    #Delprogram som utfører sletting av en student fra Student-tabellen
    #Om studenten finnes i Eksamensresultat-tabellen, kan han ikke slettes
    #da han allerede har fullført en eller flere eksamener
    def slett_student():
        funnet=False
        sjekk_liste=[]
        studentnr=stnr.get()

        finn_markor=mindatabase.cursor()

        finn_markor.execute('''
                SELECT Studentnr
                FROM Eksamensresultat
                ''')
        
        for row in finn_markor:
            sjekk_liste+=[[row[0]]]
            if studentnr==row[0]:
                lbl_svar.config(text='Studenten kan ikke slettes')
                funnet=True
        if funnet==False:
        
            slett_markor=mindatabase.cursor()
            slett_setning=('''
                            DELETE FROM Student
                            WHERE Studentnr=%s
                            ''')
            
            sletting=(studentnr,)
            slett_markor.execute(slett_setning,sletting)
            
            mindatabase.commit()
            lbl_svar.config(text='Slettet')
            stnr.set('')
            fnavn.set('')
            enavn.set('')
            eposten.set('')
            tlf.set('')
            slett_markor.close()

    #Oppretter vindu som viser hvilken student som blir slettet
    vindu4=Toplevel()
    vindu4.title('Slett student')
    
    lbl_stnr=Label(vindu4,text='Oppgi studentnummer: ')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    
    lbl_fnavn=Label(vindu4,text='Oppgi fornavn: ')
    lbl_fnavn.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    
    lbl_enavn=Label(vindu4,text='Oppgi etternavn: ')
    lbl_enavn.grid(row=2,column=0,padx=10,pady=10,sticky=W)
    
    lbl_epost=Label(vindu4,text='Oppgi epost: ')
    lbl_epost.grid(row=3,column=0,padx=10,pady=10,sticky=W)
    
    lbl_tlf=Label(vindu4,text='Oppgi telefon: ')
    lbl_tlf.grid(row=4,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu4,text='')
    lbl_svar.grid(row=5,column=2,sticky=E)
    
    stnr=StringVar()
    ent_stnr=Entry(vindu4,width=8,textvariable=stnr)
    ent_stnr.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
    fnavn=StringVar()
    ent_fnavn=Entry(vindu4,width=20,state='readonly',textvariable=fnavn)
    ent_fnavn.grid(row=1,column=2,padx=10,pady=10,sticky=W)
    
    enavn=StringVar()
    ent_enavn=Entry(vindu4,width=30,state='readonly',textvariable=enavn)
    ent_enavn.grid(row=2,column=2,padx=10,pady=10,sticky=W)
    
    eposten=StringVar()
    ent_epost=Entry(vindu4,width=30,state='readonly',textvariable=eposten)
    ent_epost.grid(row=3,column=2,padx=10,pady=10,sticky=W)
    
    tlf=StringVar()
    ent_tlf=Entry(vindu4,width=8,state='readonly',textvariable=tlf)
    ent_tlf.grid(row=4,column=2,padx=10,pady=10,sticky=W)
    
    btn_sjekk=Button(vindu4,text='Hent student',command=finn_student)
    btn_sjekk.grid(row=0,column=3,padx=10,pady=10,sticky=E)
    
    btn_slett=Button(vindu4,text='Slett',command=slett_student)
    btn_slett.grid(row=5,column=3,padx=10,pady=10,sticky=SE)
    
    btn_avslutt=Button(vindu4,text='tilbake',command=vindu4.destroy)
    btn_avslutt.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å lagre en eksamen med oppgitt emnekode, dato og ledig rom
def vindu_lagre_eksamen():

    #Delprogram som finner alle ledige rom på oppgitt dato
    def hent_rom():
        
        romliste=[]
        dato=datoen.get()
        emnekode=emnet.get()

        hent_markor=mindatabase.cursor()

        hent=('''
                SELECT *
                FROM Rom
                WHERE Romnr NOT IN(SELECT Romnr FROM Eksamen WHERE Dato=%s AND Rom.Romnr=Eksamen.Romnr)
                ORDER BY Romnr;
                ''')
        settinn=(dato,)
        hent_markor.execute(hent,settinn)
        
        for row in hent_markor:
            romliste+=[[row[0],'-',row[1]]]
        innhold_rom.set(romliste)
        hent_markor.close()

    #Delprogram som setter rom inn i entryen for Romnr
    def velg_rom(event):
        
        valgt=lst_rom.get(lst_rom.curselection())
        liste=[]
        markor=mindatabase.cursor()

        markor.execute('''
                        SELECT *
                        FROM Rom 
                        ''')
        for row in markor:
            if valgt[0]==row[0]:
                rommet.set(row[0])

        markor.close()

    #Delprogram som utfører lagring av eksamen med oppgitt Romnr
    def lagre_eksamen():
        
        settinn_liste=[]

        emnekode=emnet.get()
        dato=datoen.get()
        rom=rommet.get()

        lagre_markor=mindatabase.cursor()

        lagre=('''
                INSERT INTO Eksamen
                (Emnekode,Dato,Romnr)
                VALUES(%s,%s,%s)
                ''')
        
        settinn_liste+=[(emnekode.upper()),dato,(rom.upper())]

        lagre_markor.execute(lagre,settinn_liste)
        
        lagre_markor.close()
        mindatabase.commit()
        lbl_svar.config(text='Lagret')

    markor=mindatabase.cursor()

    #Oppretter vindu som viser hvilken eksamen som lagres med hvilket rom
    vindu2=Toplevel()
    vindu2.title('Lagre ny eksamen')

    lbl_emne=Label(vindu2,text='Oppgi emnekode: ')
    lbl_emne.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_dato=Label(vindu2,text='Oppgi eksamensdato: ')
    lbl_dato.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    lbl_romnr=Label(vindu2,text='Oppgi romnummer: ')
    lbl_romnr.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu2,text='')
    lbl_svar.grid(row=3,column=2,sticky=SE)
    
    y_scroll=Scrollbar(vindu2,orient=VERTICAL)
    y_scroll.grid(row=3,column=1,padx=(0,10),pady=5,sticky=NS)
    
    innhold_rom=StringVar()
    lst_rom=Listbox(vindu2,width=25,height=5,listvariable=innhold_rom,yscrollcommand=y_scroll.set)
    lst_rom.grid(row=3,column=0,padx=(10,0),pady=5,sticky=W)

    y_scroll['command']=lst_rom.yview

    lst_rom.bind('<<ListboxSelect>>',velg_rom)

    emnet=StringVar()
    ent_emne=Entry(vindu2,width=8,textvariable=emnet)
    ent_emne.grid(row=0,column=2,padx=10,pady=10,sticky=W)

    datoen=StringVar()
    ent_dato=Entry(vindu2,width=10,textvariable=datoen)
    ent_dato.grid(row=1,column=2,padx=10,pady=10,sticky=W)

    rommet=StringVar()
    ent_romnr=Entry(vindu2,width=6,textvariable=rommet)
    ent_romnr.grid(row=2,column=2,padx=10,pady=10,sticky=W)

    btn_hent=Button(vindu2,text='Sjekk ledige rom',command=hent_rom)
    btn_hent.grid(row=1,column=3,padx=10,pady=10,sticky=SE)

    btn_lagre=Button(vindu2,text='Lagre',command=lagre_eksamen)
    btn_lagre.grid(row=3,column=3,padx=10,pady=10,sticky=SE)

    btn_tilbake=Button(vindu2,text='Tilbake',command=vindu2.destroy)
    btn_tilbake.grid(row=4,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å oppdatere rom med antall plasser for en eksamen
def vindu_oppdater_eksamen():

    #Delprogram som viser alle ledige rom på oppgitt dato
    def hent_rom():
        
        romliste=[]
        dato=datoen.get()
        emnekode=emnet.get()

        hent_markor=mindatabase.cursor()

        hent=('''
                SELECT *
                FROM Rom
                WHERE Romnr NOT IN(SELECT Romnr FROM Eksamen WHERE Dato=%s AND Rom.Romnr=Eksamen.Romnr)
                ORDER BY Romnr;
                ''')
        settinn=(dato,)
        hent_markor.execute(hent,settinn)
        
        for row in hent_markor:
            romliste+=[[row[0],'-',row[1]]]
        innhold_rom.set(romliste)
        hent_markor.close()

    #Delprogram som setter ledig rom inn i entryen for Romnr
    def velg_rom(event):
        
        valgt=lst_rom.get(lst_rom.curselection())
        liste=[]
        markor=mindatabase.cursor()

        markor.execute('''
                        SELECT *
                        FROM Rom 
                        ''')
        for row in markor:
            if valgt[0]==row[0]:
                rommet.set(row[0])

        markor.close()

    #Delprogrammet som utfører oppdatering av en eksamen
    def oppdater_eksamen():
        
        settinn_liste=[]

        emnekode=emnet.get()
        dato=datoen.get()
        rom=rommet.get()

        oppdater_markor=mindatabase.cursor()

        oppdater=('''
                UPDATE Eksamen
                SET Romnr=%s
                WHERE Emnekode=%s AND Dato=%s
                ''')
        
        settinn_liste+=[(rom.upper()),(emnekode.upper()),dato]

        oppdater_markor.execute(oppdater,settinn_liste)
        
        oppdater_markor.close()
        mindatabase.commit()
        lbl_svar.config(text='Oppdatert')

    markor=mindatabase.cursor()

    #Oppretter vindu som viser hvilken eksamen som oppdateres
    vindu3=Toplevel()
    vindu3.title('Oppdater eksamen')

    lbl_emne=Label(vindu3,text='Oppgi emnekode: ')
    lbl_emne.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_dato=Label(vindu3,text='Oppgi eksamensdato: ')
    lbl_dato.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    lbl_romnr=Label(vindu3,text='Oppgi romnummer: ')
    lbl_romnr.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu3,text='')
    lbl_svar.grid(row=5,column=2,sticky=E)

    y_scroll=Scrollbar(vindu3,orient=VERTICAL)
    y_scroll.grid(row=3,column=1,padx=(0,10),pady=5,sticky=NS)

    innhold_rom=StringVar()
    lst_rom=Listbox(vindu3,width=25,height=5,listvariable=innhold_rom,yscrollcommand=y_scroll.set)
    lst_rom.grid(row=3,column=0,padx=(10,0),pady=5,sticky=W)

    y_scroll['command']=lst_rom.yview
    lst_rom.bind('<<ListboxSelect>>',velg_rom)

    emnet=StringVar()
    ent_emne=Entry(vindu3,width=8,textvariable=emnet)
    ent_emne.grid(row=0,column=2,padx=10,pady=10,sticky=W)

    datoen=StringVar()
    ent_dato=Entry(vindu3,width=10,textvariable=datoen)
    ent_dato.grid(row=1,column=2,padx=10,pady=10,sticky=W)

    rommet=StringVar()
    ent_romnr=Entry(vindu3,width=6,textvariable=rommet)
    ent_romnr.grid(row=2,column=2,padx=10,pady=10,sticky=W)

    btn_hent=Button(vindu3,text='Sjekk ledige rom',command=hent_rom)
    btn_hent.grid(row=1,column=3,padx=10,pady=10,sticky=SE)

    btn_lagre=Button(vindu3,text='Oppdater',command=oppdater_eksamen)
    btn_lagre.grid(row=5,column=3,padx=10,pady=10,sticky=SE)

    btn_tilbake=Button(vindu3,text='Tilbake',command=vindu3.destroy)
    btn_tilbake.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å slette en eksamen
def vindu_slett_eksamen():

    #Delprogram som finner eksamen i Eksamen-tabellen
    def finn_eksamen():
        eks_liste=[]
        emnekode=emnet.get()
        dato=datoen.get()
        
        lete_markor=mindatabase.cursor()
        lete=('''
                SELECT *
                FROM Eksamen
                WHERE Emnekode=%s AND Dato=%s
                ''')

        settinn=(emnekode,dato)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            rommet.set(row[2])

        lete_markor.close()

    #Delprogram som finner eksamen i Eksamensresultat-tabellen
    #Om eksamen finnes i denne tabellen, kan den ikke slettes
    def finn_i_eksamensresultat():

        emnekode=emnet.get()
        dato=datoen.get()
        
        funnet=False
        
        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT DISTINCT Emnekode, Dato 
                FROM Eksamensresultat 
                WHERE Emnekode=%s AND Dato=%s
                ''')
        
        settinn=(emnekode,dato)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            if emnekode==row[0]:
                funnet=True
        lete_markor.close()
            
        return funnet            

    #Delprogram som utfører sletting av eksamen fra Eksamen-tabellen
    def slett_eksamen():
        emnekode=emnet.get()
        dato=datoen.get()

        funnet=finn_i_eksamensresultat()
        
        if funnet==False:
            slett_markor=mindatabase.cursor()

            slett=('''
                    DELETE FROM Eksamen
                    WHERE Emnekode=%s AND Dato=%s
                    ''')

            settinn=(emnekode,dato)

            slett_markor.execute(slett,settinn)

            mindatabase.commit()
            slett_markor.close()
            lbl_svar.config(text='Slettet')
        else:
            lbl_svar.config(text='Kan ikke slettes')

    #Oppretter vindu som viser hvilken eksamen som slettes
    vindu4=Toplevel()
    vindu4.title('Slett eksamen')

    lbl_emne=Label(vindu4,text='Oppgi emnekode: ')
    lbl_emne.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_dato=Label(vindu4,text='Oppgi eksamensdato: ')
    lbl_dato.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    lbl_romnr=Label(vindu4,text='Oppgi romnummer: ')
    lbl_romnr.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu4,text='')
    lbl_svar.grid(row=5,column=2,sticky=E)

    emnet=StringVar()
    ent_emne=Entry(vindu4,width=8,textvariable=emnet)
    ent_emne.grid(row=0,column=2,padx=10,pady=10,sticky=W)

    datoen=StringVar()
    ent_dato=Entry(vindu4,width=10,textvariable=datoen)
    ent_dato.grid(row=1,column=2,padx=10,pady=10,sticky=W)

    rommet=StringVar()
    ent_romnr=Entry(vindu4,width=6,textvariable=rommet)
    ent_romnr.grid(row=2,column=2,padx=10,pady=10,sticky=W)

    btn_sjekk=Button(vindu4,text='Hent eksamensinfo',command=finn_eksamen)
    btn_sjekk.grid(row=1,column=3,padx=10,pady=10,sticky=E)

    btn_slett=Button(vindu4,text='Slett',command=slett_eksamen)
    btn_slett.grid(row=5,column=3,padx=10,pady=10,sticky=SE)

    btn_tilbake=Button(vindu4,text='Tilbake',command=vindu4.destroy)
    btn_tilbake.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å melde opp en student til eksamen i Eksamensresultat-tabellen
def vindu_oppmeld_til_eksamen():

    #Delprogram som lagrer studenten i Eksamensresultat-tabellen med karakter=NULL
    def oppmeld_til_eksamen():
        
        studentnr=stnr.get()
        emne=emnet.get()
        dato=datoen.get()
        lagre_markor=mindatabase.cursor()

        lagre=('''
                INSERT INTO Eksamensresultat
                (Studentnr,Emnekode,Dato)
                VALUES(%s,%s,%s)
                ''')
        
        settinn=((studentnr.upper()),(emne.upper()),dato)

        lagre_markor.execute(lagre,settinn)

        mindatabase.commit()
        lagre_markor.close()

        lbl_svar.config(text='Oppmeldt')

    #Oppretter vindu som viser informasjon om studenten som skal meldes opp til eksamen
    vindu2=Toplevel()
    vindu2.title('Eksamensoppmelding av student')

    lbl_stnr=Label(vindu2,text='Oppgi studentnr')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_emnet=Label(vindu2,text='Oppgi emnekode')
    lbl_emnet.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_datoen=Label(vindu2,text='Oppgi dato')
    lbl_datoen.grid(row=3,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu2,text='')
    lbl_svar.grid(row=4,column=1,sticky=E)

    stnr=StringVar()
    ent_stnr=Entry(vindu2,width=5,textvariable=stnr)
    ent_stnr.grid(row=0,column=1,padx=10,pady=10)

    emnet=StringVar()
    ent_emnet=Entry(vindu2,width=8,textvariable=emnet)
    ent_emnet.grid(row=2,column=1,padx=10,pady=10)

    datoen=StringVar()
    ent_datoen=Entry(vindu2,width=9,textvariable=datoen)
    ent_datoen.grid(row=3,column=1,padx=10,pady=10)

    btn_lagre=Button(vindu2,text='Meld opp student',command=oppmeld_til_eksamen)
    btn_lagre.grid(row=4,column=3,padx=10,pady=10,sticky=SE)

    btn_avslutt=Button(vindu2,text='Tilbake',command=vindu2.destroy)
    btn_avslutt.grid(row=5,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å lagre eksamensresultat for en student
def vindu_lagre_eksamensresultat():

    #Delprogram for å finne studenten det skal lagres eksamensresultat for
    def finn_eksamen():
        funnet=False

        karakterliste=[]
        studentnr=stnr.get()
        emne=emnet.get()
        dato=datoen.get()
        
        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT *
                FROM Eksamensresultat
                WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s
                ''')

        settinn=(studentnr,emne,dato)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            karakterliste+=[row[3]]

            if karakterliste[0]==None:
                funnet=True
            
            return funnet

    #Delprogram som utfører lagring av eksamensresultat for en student i Eksamensresultat-tabellen
    def lagre_eksamensresultat():
        
        funnet=finn_eksamen()
        studentnr=stnr.get()
        emne=emnet.get()
        dato=datoen.get()
        karakter=kar.get()
        if funnet==True:
            lagre_markor=mindatabase.cursor()

            lagre=('''
                    UPDATE Eksamensresultat
                    SET Karakter=%s
                    WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s
                    ''')
            
            settinn=((karakter.upper()),studentnr,emne,dato)

            lagre_markor.execute(lagre,settinn)

            mindatabase.commit()
            lagre_markor.close()
            lbl_svar.config(text='Lagret')
        
        else:
            lbl_svar.config(text='Kan ikke lagres')

    #Oppretter vindu som viser hvilken student det skal lagres eksamensresultat for
    vindu3=Toplevel()
    vindu3.title('Lagre ny eksamensresultat')

    lbl_stnr=Label(vindu3,text='Oppgi studentnr')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_emnet=Label(vindu3,text='Oppgi emnekode')
    lbl_emnet.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_datoen=Label(vindu3,text='Oppgi dato')
    lbl_datoen.grid(row=3,column=0,padx=10,pady=10,sticky=W)

    lbl_kar=Label(vindu3,text='Oppgi karakter')
    lbl_kar.grid(row=4,column=0)

    lbl_svar=Label(vindu3,text='')
    lbl_svar.grid(row=5,column=1,sticky=E)

    stnr=StringVar()
    ent_stnr=Entry(vindu3,width=5,textvariable=stnr)
    ent_stnr.grid(row=0,column=1,padx=10,pady=10)

    emnet=StringVar()
    ent_emnet=Entry(vindu3,width=8,textvariable=emnet)
    ent_emnet.grid(row=2,column=1,padx=10,pady=10)

    datoen=StringVar()
    ent_datoen=Entry(vindu3,width=9,textvariable=datoen)
    ent_datoen.grid(row=3,column=1,padx=10,pady=10)

    kar=StringVar()
    ent_kar=Entry(vindu3,width=2,textvariable=kar)
    ent_kar.grid(row=4,column=1)

    btn_lagre=Button(vindu3,text='Lagre eksamensresultat',command=lagre_eksamensresultat)
    btn_lagre.grid(row=5,column=3,padx=10,pady=10,sticky=SE)

    btn_avslutt=Button(vindu3,text='Tilbake',command=vindu3.destroy)
    btn_avslutt.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å oppdatere eksamensresultat for en student
def vindu_oppdater_eksamensresultat():

    #Delprogram som finner studenten det skal oppdateres eksamensresultat for
    def finn_eksamen():
        funnet=False

        karakterliste=[]
        studentnr=stnr.get()
        emne=emnet.get()
        dato=datoen.get()
        
        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT *
                FROM Eksamensresultat
                WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s
                ''')

        settinn=(studentnr,emne,dato)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            karakterliste+=[row[3]]

            if karakterliste[0]==None:
                funnet=True
            else:
                kar.set(karakterliste)

    #Delprogrammet som oppdaterer eksamensresultat for en student i Eksamensresultat-tabellen
    def oppdater_eksamensresultat():
        
        studentnr=stnr.get()
        emne=emnet.get()
        dato=datoen.get()
        karakter=kar.get()
    
        lagre_markor=mindatabase.cursor()

        lagre=('''
                UPDATE Eksamensresultat
                SET Karakter=%s
                WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s
                ''')
        
        settinn=(karakter,studentnr,emne,dato)

        lagre_markor.execute(lagre,settinn)

        mindatabase.commit()
        lagre_markor.close()
        lbl_svar.config(text='Oppdatert')
        
    #Oppretter vindu som viser hvilken student det skal oppdateres eksamensresultat for
    vindu4=Toplevel()
    vindu4.title('Oppdater eksamensresultat')

    lbl_stnr=Label(vindu4,text='Oppgi studentnr')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_emnet=Label(vindu4,text='Oppgi emnekode')
    lbl_emnet.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_datoen=Label(vindu4,text='Oppgi dato')
    lbl_datoen.grid(row=3,column=0,padx=10,pady=10,sticky=W)

    lbl_kar=Label(vindu4,text='Oppgi karakter')
    lbl_kar.grid(row=4,column=0)

    lbl_svar=Label(vindu4,text='')
    lbl_svar.grid(row=5,column=1,sticky=E)

    stnr=StringVar()
    ent_stnr=Entry(vindu4,width=5,textvariable=stnr)
    ent_stnr.grid(row=0,column=1,padx=10,pady=10)

    emnet=StringVar()
    ent_emnet=Entry(vindu4,width=8,textvariable=emnet)
    ent_emnet.grid(row=2,column=1,padx=10,pady=10)

    datoen=StringVar()
    ent_datoen=Entry(vindu4,width=9,textvariable=datoen)
    ent_datoen.grid(row=3,column=1,padx=10,pady=10)

    kar=StringVar()
    ent_kar=Entry(vindu4,width=2,textvariable=kar)
    ent_kar.grid(row=4,column=1)

    btn_sjekk=Button(vindu4,text='Hent info',command=finn_eksamen)
    btn_sjekk.grid(row=3,column=3,sticky=SE)

    btn_lagre=Button(vindu4,text='Oppdater eksamensresultat',command=oppdater_eksamensresultat)
    btn_lagre.grid(row=5,column=3,padx=10,pady=10,sticky=SE)

    btn_avslutt=Button(vindu4,text='Tilbake',command=vindu4.destroy)
    btn_avslutt.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å slette eksamensresultat
def vindu_slett_eksamensresultat():

    #Delprogram som finner studenten i eksamensresultat-tabellen
    def finn_student_i_eksamensresultat():
        funnet=False
        studentnr=stnr.get()
        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT Studentnr
                FROM Eksamensresultat
                WHERE Studentnr=%s AND Karakter IS NULL
                ''')

        lete_markor.execute(lete%studentnr)

        for row in lete_markor:
            if studentnr==row[0]:
                funnet=True
        lete_markor.close()
        return funnet

    #Delprogram som utfører sletting av student med karakter=NULL i databasen
    def slett_eksamensresultat():

        funnet=finn_student_i_eksamensresultat()
        slett_markor=mindatabase.cursor()
        studentnr=stnr.get()
        emnekode=emnet.get()
        dato=datoen.get()
        
        if funnet==True:
            slett=('''
                    DELETE FROM Eksamensresultat
                    WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s
                    ''')
            settinn=(studentnr,emnekode,dato)
            slett_markor.execute(slett,settinn)

            mindatabase.commit()
            slett_markor.close()
            lbl_svar.config(text='Slettet')

        #studenter som allerede har fått en karakter kan ikke slettes
        else:
            lbl_svar.config(text='Kan ikke slettes')

    #Oppretter vindu som viser informasjon om studenten som skal slettes
    vindu5=Toplevel()
    vindu5.title('Slett eksamensresultat')

    lbl_stnr=Label(vindu5,text='Oppgi studentnr')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_emnet=Label(vindu5,text='Oppgi emnekode')
    lbl_emnet.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_datoen=Label(vindu5,text='Oppgi dato')
    lbl_datoen.grid(row=3,column=0,padx=10,pady=10,sticky=W)

    lbl_svar=Label(vindu5,text='')
    lbl_svar.grid(row=5,column=1,sticky=E)

    stnr=StringVar()
    ent_stnr=Entry(vindu5,width=5,textvariable=stnr)
    ent_stnr.grid(row=0,column=1,padx=10,pady=10)

    emnet=StringVar()
    ent_emnet=Entry(vindu5,width=8,textvariable=emnet)
    ent_emnet.grid(row=2,column=1,padx=10,pady=10)

    datoen=StringVar()
    ent_datoen=Entry(vindu5,width=9,textvariable=datoen)
    ent_datoen.grid(row=3,column=1,padx=10,pady=10)

    btn_lagre=Button(vindu5,text='Slett eksamensresultat',command=slett_eksamensresultat)
    btn_lagre.grid(row=5,column=3,padx=10,pady=10,sticky=SE)

    btn_avslutt=Button(vindu5,text='Tilbake',command=vindu5.destroy)
    btn_avslutt.grid(row=6,column=3,padx=10,pady=10,sticky=SE)


#Delprogram for å vise alle eksamener på en oppgitt dato
def vindu_vis_eksamen_dag():

    #Selve delprogrammet der man oppgir en eksamensdato og programmet henter
    #informasjon om alle eksamener på den oppgitte datoen
    def vis_eksamen_dag():
        txt_utdata.config(state=NORMAL)
        txt_utdata.delete('1.0','end')
        
        eks_liste=[]
        dato=datoen.get()
        
        lete_markor=mindatabase.cursor()
        lete=('''
                SELECT *
                FROM Eksamen
                WHERE Dato=%s
                ''')

        lete_markor.execute(lete%dato)

        for row in lete_markor:
            eks_liste+=[[row[0],row[1],row[2]]]

            txt_utdata.insert('1.0',str(row[0])+' '+'på rom '+str(row[2])+'\n')
        txt_utdata.config(state=DISABLED)
        lete_markor.close()

    #Oppretter vindu som viser resultatet for alle eksamener på en oppgitt dato
    vindu_eksamen_dag=Toplevel()
    vindu_eksamen_dag.title('Alle eksamener på en dag')

    lbl_dato=Label(vindu_eksamen_dag,text='Oppgi eksamensdato: ')
    lbl_dato.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    datoen=StringVar()
    ent_datoen=Entry(vindu_eksamen_dag,width=9,textvariable=datoen)
    ent_datoen.grid(row=0,column=1,padx=10,pady=10,sticky=W)
    
    txt_utdata=Text(vindu_eksamen_dag,width=25,height=5)
    txt_utdata.grid(row=1,column=0,rowspan=5,columnspan=2,padx=10,pady=10,sticky=W)

    btn=Button(vindu_eksamen_dag,text='Hent',command=vis_eksamen_dag)
    btn.grid(row=0,column=2,padx=10,pady=10,sticky=NE)

    btn_avslutt=Button(vindu_eksamen_dag,text='Tilbake til hovedmenyen',command=vindu_eksamen_dag.destroy)
    btn_avslutt.grid(row=11,column=2,padx=10,pady=10,sticky=E)


#Delprogram for å vise alle eksamen i en tidsperiode
def vindu_vis_eksamen_periode():

    #Selve delprogrammet der man oppgir dato fra og til og henter alle eksamener i den perioden
    def vis_eksamen_periode():
        txt_utdata.config(state=NORMAL)
        eks_liste=[]
        fradato=dato_fra.get()
        tildato=dato_til.get()
        
        lete_markor=mindatabase.cursor()
        lete=('''
                SELECT *
                FROM Eksamen
                WHERE Dato BETWEEN %s AND %s
                ''')

        settinn=(fradato,tildato)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            eks_liste+=[[row[0],row[1],row[2]]]

            txt_utdata.insert('1.0',str(row[0])+', den'+' '+str(row[1])+' '+'på rom '+str(row[2])+'\n')
        txt_utdata.config(state=DISABLED)

        lete_markor.close()  

    #Oppretter vindu som viser alle eksamener i en periode
    vindu_eksamen_periode=Toplevel()
    vindu_eksamen_periode.title('Alle eksamener i en periode')

    lbl_fradato=Label(vindu_eksamen_periode,text='Oppgi fra dato: ')
    lbl_fradato.grid(row=0,column=0,padx=5,pady=10,sticky=W)

    lbl_tildato=Label(vindu_eksamen_periode,text='Oppgi til dato: ')
    lbl_tildato.grid(row=1,column=0,padx=5,pady=10,sticky=W)

    dato_fra=StringVar()
    ent_dato_fra=Entry(vindu_eksamen_periode,width=9,textvariable=dato_fra)
    ent_dato_fra.grid(row=0,column=0,padx=5,pady=10)

    dato_til=StringVar()
    ent_dato_til=Entry(vindu_eksamen_periode,width=9,textvariable=dato_til)
    ent_dato_til.grid(row=1,column=0,padx=5,pady=10)

    y_scroll=Scrollbar(vindu_eksamen_periode,orient=VERTICAL)
    y_scroll.grid(row=2,column=1,rowspan=5,padx=(0,10),pady=10,sticky=NS)
    
    txt_utdata=Text(vindu_eksamen_periode,width=36,height=5,yscrollcommand=y_scroll.set)
    txt_utdata.grid(row=2,column=0,rowspan=5,padx=(10,0),pady=10,sticky=W)

    y_scroll['command']=txt_utdata.yview
                  
    btn=Button(vindu_eksamen_periode,text='Hent',command=vis_eksamen_periode)
    btn.grid(row=1,column=2,padx=10,pady=10,sticky=NE)

    btn_avslutt=Button(vindu_eksamen_periode,text='Tilbake til hovedmenyen',command=vindu_eksamen_periode.destroy)
    btn_avslutt.grid(row=11,column=2,padx=10,pady=10,sticky=E)


#Delprogram fro masseregistrering av eksamensresultater
def vindu_lagre_resultat_samlet():

    #Delprogram som finner studenter uten gyldig karakter i Eksamensresultat-tabellen
    def finn_student():

        #Delprogram som utfører registrering av eksamensresultat samlet
        def lagre_resultat_samlet():

            emnekode=emnet.get()
            dato=datoen.get()
            
            for n in range (len(ny_liste)):
                studentnr=(ny_liste[n][0].get())
                karakter=(ny_liste[n][1].get())
            
                lagre_markor=mindatabase.cursor()

                lagre=('''
                        UPDATE Eksamensresultat
                        SET Karakter=%s
                        WHERE Emnekode=%s AND Dato=%s AND Studentnr=%s
                        ''')

                settinn=(karakter.upper(),emnekode.upper(),dato,studentnr)

                lagre_markor.execute(lagre,settinn)

                mindatabase.commit()
                lagre_markor.close()
                lbl_svar.config(text='Lagret')
                
        emnekode=emnet.get()
        dato=datoen.get()
        
        studentliste=[]
        ny_liste=[]
        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT Studentnr,Karakter
                FROM Eksamensresultat
                WHERE Emnekode=%s AND Dato=%s AND Karakter IS NULL
                ''')
        settinn=(emnekode,dato)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            studentliste+=[[row[0],row[1]]]

        lete_markor.close()

        #Oppretter vindu der man oppgir karakterer samlet for alle studenter som har tatt eksamen
        vindu3=Toplevel()
        vindu3.title('Registrer resultater')

        #Oppretter labels og entries i en løkke slik at de genereres for
        #hver ny student det skal lagres eksamen for
        for n in range (len(studentliste)):
            lbl_student=Label(vindu3,text='Studentnummer:')
            lbl_student.grid(row=n,column=0,padx=10,pady=10,sticky=W)

            lbl_kar=Label(vindu3,text='Karakter:')
            lbl_kar.grid(row=n,column=3,padx=10,pady=10,sticky=W)

            stnr=StringVar()
            ent_stnr=Entry(vindu3,width=7,state='readonly',textvariable=stnr)
            ent_stnr.grid(row=n,column=2,padx=10,pady=10,sticky=W)

            kar=StringVar()
            ent_kar=Entry(vindu3,width=2,textvariable=kar)
            ent_kar.grid(row=n,column=4,padx=10,pady=10,sticky=W)

            #liste som tar vare på stringvariablene stnr og kar
            ny_liste+=[[stnr,kar]]

        #flytter lbl_svar og knappene utenfor for-løkka slik at de kun genereres en gang
        lbl_svar=Label(vindu3,text='')
        lbl_svar.grid(row=len(studentliste)+1,column=3,padx=10,pady=10,sticky=E)
            
        btn_lagre=Button(vindu3,text='Lagre',command=lagre_resultat_samlet)
        btn_lagre.grid(row=len(studentliste)+1,column=4,padx=10,pady=10,sticky=SE)

        btn_tilbake=Button(vindu3,text='Tilbake',command=vindu3.destroy)
        btn_tilbake.grid(row=len(studentliste)+2,column=4,padx=10,pady=10,sticky=SE)

        #Går gjennom lengden av ny_liste og setter studentnummerene i entryene
        for m in range (len(ny_liste)):
            ny_liste[m][0].set(studentliste[m][0])
        
    #Oppretter vindu der man oppgir emnekode og eksamensdato, trykk deretter på
    # "hent studenter" for å gå videre til neste vindu der man registrerer karakterer
    vindu2=Toplevel()
    vindu2.title('Lagre eksamensresultater samlet')

    lbl_emnet=Label(vindu2,text='Oppgi emnekode')
    lbl_emnet.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_datoen=Label(vindu2,text='Oppgi dato')
    lbl_datoen.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    emnet=StringVar()
    ent_emnet=Entry(vindu2,width=8,textvariable=emnet)
    ent_emnet.grid(row=0,column=1,padx=10,pady=10)

    datoen=StringVar()
    ent_datoen=Entry(vindu2,width=9,textvariable=datoen)
    ent_datoen.grid(row=1,column=1,padx=10,pady=10)

    btn_sjekk=Button(vindu2,text='Hent studenter',command=finn_student)
    btn_sjekk.grid(row=2,column=1,padx=10,pady=10,sticky=SE)

    btn_avslutt=Button(vindu2,text='Tilbake til hovedmenyen',command=vindu2.destroy)
    btn_avslutt.grid(row=3,column=1,padx=10,pady=10,sticky=SE)


#Delprogram for å vise karakterliste i et emne
def vindu_vis_karakterliste(): 

    #Selve delprogrammet der man oppgir emnekode og eksamensdato
    #og programmet henter inn (vha SQL-spørring) all informasjon man trenger for å vise resultatet
    def vis_karakterliste():
        
        txt_utdata.config(state=NORMAL)
        txt_utdata.delete('1.0',END)
        
        innhold_liste=[]
        emnekode=ekode.get()
        datoen=dato.get()

        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT Eksamensresultat.Studentnr,Fornavn,Etternavn,Dato,Karakter
                FROM Student JOIN Eksamensresultat
                        ON(Student.Studentnr=Eksamensresultat.Studentnr)
                WHERE Emnekode=%s AND Dato=%s AND Karakter IS NOT NULL
                GROUP BY Eksamensresultat.Studentnr,Fornavn,Etternavn,Dato,Karakter
                ORDER BY Studentnr DESC, Dato DESC
                ''')
        settinn=(emnekode.upper(),datoen)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            innhold_liste+=[[row[0],row[1],row[2],row[3],row[4]]]
            txt_utdata.insert('1.0',str(row[0])+' '+str(row[1])+' '+str(row[2])+' '+'-'+' '+str(row[4])+'\n')
        txt_utdata.config(state=DISABLED)
        lete_markor.close()

    #Oppretter vindu som viser karakterliste i et emne
    karakterliste=Toplevel()
    karakterliste.title('Karakterliste i et emne')

    lbl_ekode=Label(karakterliste,text='Oppgi emnekode:')
    lbl_ekode.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_dato=Label(karakterliste,text='Oppgi dato:')
    lbl_dato.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    ekode=StringVar()
    ent_ekode=Entry(karakterliste,width=8,textvariable=ekode)
    ent_ekode.grid(row=0,column=0,padx=10,pady=10)

    dato=StringVar()
    ent_dato=Entry(karakterliste,width=8,textvariable=dato)
    ent_dato.grid(row=1,column=0,padx=10,pady=10)

    y_scroll=Scrollbar(karakterliste,orient=VERTICAL)
    y_scroll.grid(row=2,column=1,rowspan=5,padx=(0,10),pady=10,sticky=NS)
    
    txt_utdata=Text(karakterliste,width=36,height=5,yscrollcommand=y_scroll.set)
    txt_utdata.grid(row=2,column=0,rowspan=5,padx=(10,0),pady=10,sticky=W)

    y_scroll['command']=txt_utdata.yview

    btn_emne=Button(karakterliste,text='Hent',command=vis_karakterliste)
    btn_emne.grid(row=1,column=2,padx=10,pady=10,sticky=NE)

    btn_avslutt=Button(karakterliste,text='Tilbake til hovedmenyen',command=karakterliste.destroy)
    btn_avslutt.grid(row=8,column=2,padx=10,pady=10,sticky=SE)


#Delprogram for visning av karakterstatistikk for en eksamen
def vindu_vis_karakterstatistikk():
    
    #Selve delprogrammet for å finne frem all informasjon for en eksamen i et emne
    def finn_emne():
        
        txt_utdata.config(state=NORMAL)
        txt_utdata.delete('1.0',END)
        emnekode=ekode.get()
        datoen=dato.get()
        liste=[]

        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT Emne.Emnekode,Emne.Emnenavn,Emne.Studiepoeng,Karakter, COUNT(*) AS Karakterstatistikk
                FROM Emne JOIN Eksamensresultat
                    ON(Emne.Emnekode=Eksamensresultat.Emnekode)
                WHERE Eksamensresultat.Emnekode=%s AND Dato=%s AND Karakter IS NOT NULL
                GROUP BY Emne.Emnekode, Emne.Emnenavn,Emne.Studiepoeng,Karakter
                ORDER BY Karakter ASC
                ''')
        settinn=(emnekode.upper(),datoen)

        lete_markor.execute(lete,settinn)

        for row in lete_markor:
            liste+=[[row[0],row[1],str(row[2]),row[3],str(row[4])]]

        for n in liste:
            txt_utdata.insert(END,'Antall student(er): '+n[4]+', med karakter: '+n[3]+'\n')
            
        txt_utdata.insert('1.0','Emnenavn: '+str(row[1])+'\n')
        txt_utdata.insert('2.0','Studiepoeng: '+str(row[2])+'\n')
        
        txt_utdata.config(state=DISABLED)
        lete_markor.close()

    #Oppretter vinduet der man søker på emnekode og eksamensdato
    #og viser karakterstatistikken for oppgitt eksamen
    karstatistikk=Toplevel()
    karstatistikk.title('Karakterstatistikk for et emne')

    lbl_ekode=Label(karstatistikk,text='Oppgi emnekode:')
    lbl_ekode.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_dato=Label(karstatistikk,text='Oppgi eksamensdato:')
    lbl_dato.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    ekode=StringVar()
    ent_ekode=Entry(karstatistikk,width=8,textvariable=ekode)
    ent_ekode.grid(row=0,column=1,padx=10,pady=10)

    dato=StringVar()
    ent_dato=Entry(karstatistikk,width=8,textvariable=dato)
    ent_dato.grid(row=1,column=1,padx=10,pady=10)

    txt_utdata=Text(karstatistikk,width=40,height=9)
    txt_utdata.grid(row=4,column=0,rowspan=6,columnspan=4,padx=10,pady=10,sticky=W)

    btn_emne=Button(karstatistikk,text='Hent',command=finn_emne)
    btn_emne.grid(row=0,column=3,padx=10,pady=10,sticky=E)

    btn_avslutt=Button(karstatistikk,text='Tilbake til hovedmenyen',command=karstatistikk.destroy)
    btn_avslutt.grid(row=11,column=3,padx=10,pady=10,sticky=E)


#Delprogram for alle resultater for en student 
def vindu_vis_alle_resultater_en_student():

    #Selve delprogrammet for å hente alle resultater for en student
    def vis_resultater_student():
        txt_utdata.config(state=NORMAL)
        txt_utdata.delete('1.0','end')
        res_liste=[]
        studentnr=str(stnr.get())

        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT Fornavn,Etternavn,Emne.Emnekode,Studiepoeng,Karakter
                FROM Student JOIN Eksamensresultat JOIN Emne
                        ON (Eksamensresultat.Emnekode=Emne.Emnekode)
                                ON(Student.Studentnr=Eksamensresultat.Studentnr)
                WHERE Student.Studentnr=%s
                ''')
        lete_markor.execute(lete%studentnr)

        for row in lete_markor:
            res_liste+=[[row[0],row[1],row[2],row[3],row[4]]]

            txt_utdata.insert('1.0',str(row[2])+' '+str(row[3])+' '+str(row[4])+'\n')
        lbl_navn.config(text=row[0]+' '+row[1])
        txt_utdata.config(state=DISABLED)

    #Oppretter vinduet som viser alle resultater for en student
    resultater_en_student=Toplevel()
    resultater_en_student.title('Alle resultater for en student')

    lbl_stnr=Label(resultater_en_student,text='Studentnr: ')
    lbl_stnr.grid(row=0,column=0,padx=5,pady=10,sticky=W)

    lbl_navn=Label(resultater_en_student,text='')
    lbl_navn.grid(row=1,column=0,padx=5,pady=10,sticky=W)

    stnr=StringVar()
    ent_stnr=Entry(resultater_en_student,width=6,textvariable=stnr)
    ent_stnr.grid(row=0,column=0,padx=5,pady=10)

    y_scroll=Scrollbar(resultater_en_student,orient=VERTICAL)
    y_scroll.grid(row=2,column=1,rowspan=5,padx=(0,10),pady=10,sticky=NS)
    
    txt_utdata=Text(resultater_en_student,width=20,height=5,yscrollcommand=y_scroll.set)
    txt_utdata.grid(row=2,column=0,rowspan=5,padx=(10,0),pady=10,sticky=W)

    y_scroll['command']=txt_utdata.yview

    btn=Button(resultater_en_student,text='Hent',command=vis_resultater_student)
    btn.grid(row=0,column=2,padx=5,pady=10,sticky=SE)

    btn_avslutt=Button(resultater_en_student,text='Tilbake til hovedmenyen',command=resultater_en_student.destroy)
    btn_avslutt.grid(row=9,column=2,padx=5,pady=10,sticky=SE)


# Delprogram for utskrift av vitnemål
def vindu_vis_vitnemål():

    #Selve delprogrammet for å finne all informasjon vitnemålet skal vise for en student
    def vis_vitnemålet():
        
        txt_utdata.config(state=NORMAL)
        txt_utdata.delete('1.0','end')
        innhold_liste=[]
        poengliste=[]
        studentnr=str(stnr.get())

        lete_markor=mindatabase.cursor()

        lete=('''
                SELECT R1.Emnekode, Emnenavn, Fornavn, Etternavn, R1.Dato, R1.Karakter, Studiepoeng
                FROM Student JOIN (Eksamensresultat AS R1) JOIN Emne
                    ON(R1.Emnekode=Emne.Emnekode)
                        ON(Student.Studentnr=R1.Studentnr)
                WHERE R1.Karakter =(
                    SELECT MIN(R2.Karakter) 
                    FROM Eksamensresultat AS R2 
                    WHERE R1.Emnekode = R2.Emnekode AND R1.Studentnr = R2.Studentnr) AND R1.Studentnr = %s
                ORDER BY RIGHT(R1.Emnekode,4)DESC, (R1.Emnekode) DESC;
                ''')

        lete_markor.execute(lete%studentnr)

        for row in lete_markor:
            innhold_liste+=[[row[0],row[1],row[2],row[3],row[4],row[5],row[6]]]

            txt_utdata.insert('1.0',str(row[0])+' '+row[1]+' '+str(row[4])+' '+row[5]+' '+str(row[6])+'\n')
        lete_markor.close()

        poeng=0
        for n in range(len(innhold_liste)):
            poeng+=innhold_liste[n][6]
        stpoeng.set(poeng)
            
        txt_utdata.config(state=DISABLED)
        lbl_fulltnavn.config(text=(row[2])+' '+(row[3]))
    
    #Oppretter Toplevel-vindu for utskrift av vitnemål
    skriv_vitnemål=Toplevel()
    skriv_vitnemål.title('Alle resultater for en student')

    lbl_stnr=Label(skriv_vitnemål,text='Oppgi studentnr: ')
    lbl_stnr.grid(row=0,column=0,padx=10,pady=10,sticky=W)

    lbl_fulltnavn=Label(skriv_vitnemål,text='')
    lbl_fulltnavn.grid(row=1,column=0,padx=10,pady=10,sticky=W)

    lbl_emnenavn=Label(skriv_vitnemål,text='')
    lbl_emnenavn.grid(row=2,column=0,padx=10,pady=10,sticky=W)

    lbl_studiepoeng=Label(skriv_vitnemål,text='Opptjente studiepoeng')
    lbl_studiepoeng.grid(row=13,column=0,padx=10,pady=10)

    stnr=StringVar()
    ent_stnr=Entry(skriv_vitnemål,width=6,textvariable=stnr)
    ent_stnr.grid(row=0,column=1,padx=10,pady=10,sticky=W)

    stpoeng=StringVar()
    ent_stpoeng=Entry(skriv_vitnemål,width=4,state='readonly',textvariable=stpoeng)
    ent_stpoeng.grid(row=13,column=1,padx=10,pady=10,sticky=W)

    y_scroll=Scrollbar(skriv_vitnemål,orient=VERTICAL)
    y_scroll.grid(row=2,rowspan=5,column=6,padx=(0,10),pady=5,sticky=NS)

    txt_utdata=Text(skriv_vitnemål,width=55,height=10,yscrollcommand=y_scroll.set)
    txt_utdata.grid(row=2,rowspan=5,column=0,columnspan=5,padx=(10,0),pady=10)

    y_scroll['command']=txt_utdata.yview
    
    btn=Button(skriv_vitnemål,text='Hent vitnemål',command=vis_vitnemålet)
    btn.grid(row=0,column=4,padx=10,pady=10,sticky=NE)

    btn_avslutt=Button(skriv_vitnemål,text='Tilbake til hovedmenyen',command=skriv_vitnemål.destroy)
    btn_avslutt.grid(row=13,column=4,padx=10,pady=10,sticky=E)


#Delprogram for Toplevel-vindu som inneholder knapper for ajourhold av student
def ajourhold_av_student():
    
    hovedvinduet=Toplevel()
    hovedvinduet.title('Ajourhold av studenter')
    
    btn_vindu_ny=Button(hovedvinduet,text='Lagre ny student',command=vindu_lagre_student)
    btn_vindu_ny.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    
    btn_vindu_opp=Button(hovedvinduet,text='Oppdater student',command=vindu_oppdater_student)
    btn_vindu_opp.grid(row=0,column=1,padx=10,pady=10,sticky=W)
    
    btn_vindu_sle=Button(hovedvinduet,text='Slett student',command=vindu_slett_student)
    btn_vindu_sle.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
    btn_avslutt=Button(hovedvinduet,text='Tilbake til hovedmenyen',command=hovedvinduet.destroy)
    btn_avslutt.grid(row=2,column=2,padx=10,pady=10,sticky=E)


#Delprogram for Toplevel-vindu som inneholder knapper for ajourhold av eksamen
def ajourhold_av_eksamen():
    
    hovedvinduet=Toplevel()
    hovedvinduet.title('Ajourhold av eksamen')
    
    btn_vindu_ny=Button(hovedvinduet,text='Lagre ny eksamen',command=vindu_lagre_eksamen)
    btn_vindu_ny.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    
    btn_vindu_opp=Button(hovedvinduet,text='Oppdater eksamen',command=vindu_oppdater_eksamen)
    btn_vindu_opp.grid(row=0,column=1,padx=10,pady=10,sticky=W)
    
    btn_vindu_sle=Button(hovedvinduet,text='Slett eksamen',command=vindu_slett_eksamen)
    btn_vindu_sle.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
    btn_avslutt=Button(hovedvinduet,text='Tilbake til hovedmenyen',command=hovedvinduet.destroy)
    btn_avslutt.grid(row=2,column=2,padx=10,pady=10,sticky=E)


#Delprogram for Toplevel-vindu som inneholder knapper for ajourhold av eksamensresultat
def ajourhold_av_eksamensresultat():
    
    hovedvinduet=Toplevel()
    hovedvinduet.title('Ajourhold av eksamensresultat')

    btn_vindu_oppmelding=Button(hovedvinduet,text='Oppmelding til eksamen',command=vindu_oppmeld_til_eksamen)
    btn_vindu_oppmelding.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    
    btn_vindu_ny=Button(hovedvinduet,text='Lagre ny eksamensresultat',command=vindu_lagre_eksamensresultat)
    btn_vindu_ny.grid(row=0,column=1,padx=10,pady=10,sticky=W)
    
    btn_vindu_opp=Button(hovedvinduet,text='Oppdater eksamensresultat',command=vindu_oppdater_eksamensresultat)
    btn_vindu_opp.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
    btn_vindu_sle=Button(hovedvinduet,text='Slett eksamensresultat',command=vindu_slett_eksamensresultat)
    btn_vindu_sle.grid(row=0,column=3,padx=10,pady=10,sticky=W)
    
    btn_avslutt=Button(hovedvinduet,text='Tilbake til hovedmenyen',command=hovedvinduet.destroy)
    btn_avslutt.grid(row=2,column=3,padx=10,pady=10,sticky=E)


#Delprogram for hovedmenyen/ Alle knapper som programmet krever
def main():
    
    hovedvindu=Tk()
    hovedvindu.title('System for håndtering av eksamen ved USN')

    btn_vindu_student=Button(hovedvindu,text='Ajourhold av studenter',command=ajourhold_av_student)
    btn_vindu_student.grid(row=0,column=0,padx=10,pady=10)

    btn_vindu_eksamen=Button(hovedvindu,text='Ajourhold av eksamen',command=ajourhold_av_eksamen)
    btn_vindu_eksamen.grid(row=0,column=1,padx=10,pady=10)

    btn_vindu_resultat=Button(hovedvindu,text='Ajourhold av eksamensresultat',command=ajourhold_av_eksamensresultat)
    btn_vindu_resultat.grid(row=0,column=2,padx=10,pady=10)

    btn_vindu_eksamen_dag=Button(hovedvindu,text='Alle eksamener på en dag',command=vindu_vis_eksamen_dag)
    btn_vindu_eksamen_dag.grid(row=1,column=0,padx=10,pady=10)

    btn_vindu_eks_etter_dato=Button(hovedvindu,text='Utskrift av eksamen i en periode',command=vindu_vis_eksamen_periode)
    btn_vindu_eks_etter_dato.grid(row=1,column=1,padx=10,pady=10)

    btn_vindu_massereg_karakter=Button(hovedvindu,text='Samlet registrering av karakterer',command=vindu_lagre_resultat_samlet)
    btn_vindu_massereg_karakter.grid(row=1,column=2,padx=10,pady=10)

    btn_vindu_karakterliste=Button(hovedvindu,text='Karakterliste i et emne',command=vindu_vis_karakterliste)
    btn_vindu_karakterliste.grid(row=2,column=0,padx=10,pady=10)

    btn_vindu_karakterstatistikk=Button(hovedvindu,text='Karakterstatistikk for en eksamen',command=vindu_vis_karakterstatistikk)
    btn_vindu_karakterstatistikk.grid(row=2,column=1,padx=10,pady=10)

    btn_vindu_alle_eksamensresultater=Button(hovedvindu,text='Alle eksamensresultater',command=vindu_vis_alle_resultater_en_student)
    btn_vindu_alle_eksamensresultater.grid(row=2,column=2,padx=10,pady=10)

    btn_vindu_vitnem=Button(hovedvindu,text='Utskrift av vitnemål',command=vindu_vis_vitnemål)
    btn_vindu_vitnem.grid(row=3,column=0,padx=10,pady=10)

    btn_avslutt=Button(hovedvindu,text='Avslutt',command=hovedvindu.destroy)
    btn_avslutt.grid(row=6,column=3,padx=10,pady=10,sticky=SE)

    hovedvindu.mainloop()

#Kaller main-programmet samt stenger koblingen mot databasen
main()
mindatabase.close()
