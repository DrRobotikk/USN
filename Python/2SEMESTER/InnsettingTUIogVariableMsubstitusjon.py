#PRG1100-2022-innsetting TUI og variable med substitusjon

#Innsetting av data i database fra python
#Innsetting ved verdiene inn i variable som refereres i cursoren

import mysql.connector

#1. koble mot databasen

mindatabase=mysql.connector.connect(host='localhost',port=3306,
    user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

#2. oppretter cursor/markør
settinn_markor=mindatabase.cursor()
markor=mindatabase.cursor()

#3. bruke databasen
varenr=input('Oppgi varenr: ')
varenavn=input('Oppgi varenavn: ')
pris=float(input('Oppgi pris: '))
katnr=int(input('Oppgi kategorinr: '))
antall=int(input('Oppgi antall: '))
hylle=input('Oppgi hylleplassering: ')

settinn_markor.execute("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES('9999','Testvare',99.99,999,99,'T99')")
mindatabase.commit()
settinn_vare=("INSERT INTO Vare"
              "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
              "VALUES(%s,%s,%s,%s,%s,%s)")
datany_vare=(varenr,varenavn,pris,katnr,antall,hylle)

settinn_markor.execute(settinn_vare,datany_vare)
mindatabase.commit()

markor.execute('SELECT * FROM Vare')

#4. bruke resultatet
for row in markor:
    print(row)

#5. koble ned databasen
settinn_markor.close()
markor.close()

mindatabase.close()

                       
