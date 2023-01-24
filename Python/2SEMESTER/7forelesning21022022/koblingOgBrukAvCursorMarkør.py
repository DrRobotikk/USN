#PRG1100-2022-kobling og bruk av cursor

import mysql.connector

#1. kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

#2. oppretter corsoren/markøren
markor=mindatabase.cursor()

#3. bruke databasen
markor.execute("SELECT * FROM Vare")

#4. bruke resultatet
for row in markor:
    print(row)

#5. koble ned databasen, corsoren stenges etter bruk, koblingen stenges
#ved programslutt
markor.close()

mindatabase.close()
