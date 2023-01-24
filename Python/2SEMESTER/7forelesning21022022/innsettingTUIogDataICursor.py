#PRG1100-2022-innsetting TUI og data i cursor

#Innsettin av data i database fra python
#Innsatteing ved verdiene "rett i cursoren"

import mysql.connector

#1. koble mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

#2. oppretter cursoren/markøren
settinn_markor=mindatabase.cursor()
markor=mindatabase.cursor()

#3. bruke databasen
#her hardkoder vi verdiene og setter de inn i databasen
#EKSEMPEL PÅ Å LAGRE NULLMERKE

settinn_markor.execute("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES('9999','Testvare',99.99,999,99,Null)")
#her bekrefter vi lagring inn i databasen
mindatabase.commit()

settinn_markor.execute("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES('8888','Nytestvare',88.88,888,88,'T88')")
mindatabase.commit()
settinn_markor.close()

markor.execute('SELECT * FROM Vare')

#4. bruke resultatet

for row in markor:
    print(row)

#5. koble ned databasen

#settinn_markor.close()
markor.close()
mindatabase.close()
