-- Introduksjon DDL, opprette database, opprette tabell, legge inn data

-- Skript for å
-- opprette databasen
-- opprette tabellen
-- legge til data

-- Sletter databasen hvis den finnes
DROP SCHEMA IF EXISTS heltnydatabase;
-- Oppretter databasen
CREATE SCHEMA IF NOT EXISTS heltnydatabase;

USE heltnydatabase;

-- Oppretter tabellen Vare
-- variant av CREATE-setning s 66,
-- forbyr NULL-merker i enkelte kolonner
CREATE TABLE Vare
(
VNr CHAR(5) PRIMARY KEY,
Betegnelse VARCHAR(30) NOT NULL,
Pris DECIMAL(8,2) NOT NULL,
KatNr SMALLINT NOT NULL,
Antall INTEGER NOT NULL,
Hylle CHAR(3)
);

-- legge inn data i tabellen vare, vare nr 1
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('90693','Marsipantang',57.00,4,0,'B17');

-- HER LEGGER DERE INN VARE NR 2 I TABELLEN S 67

INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('44939','Hobbymaling, 6 farger','115.00','2','2','B02');

-- vare nr 3
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('10830','Nisseskjegg, 30 cm',57.50,13,42,NULL);

-- HER LEGGER DERE INN VARE NR 4 TOM. VARE NR 8 ETTER SAMME STRUKTUR
INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('33044','Blandet blomsterfrø','14.50','15','1080','E05');
INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('15217','Kram tørrfluekorker, 5stk','32.00','7','213','B42');
INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('90164','Lakrisekstrakt, 100g','75.50','4','104','B06');
INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('15207','Antron garn, hvit','24.50','7','21','B41');
INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('13001','Glasskuler, 100gr','38.00','13','0','E11');
-- vare nr 9
-- TRENGER IKKE FELTNAVN-LISTA HVIS DET FINNES DATA I ALLE FELT
INSERT INTO Vare VALUES('21032','Furuspon 3 cm',57.50,17,240,'B32');

-- her legger dere inn vare nr 10 tom 15, kortform
-- SIDEN VARE NR. 15 IKKE ER HYLLEPLASSERT, HAR DEN VERDIEN 'NULL' OG MÅ SKRIVES I LANGFORMAT
INSERT INTO Vare VALUES('33045','Blomkarse','17.50','15','1206','E05');
INSERT INTO Vare VALUES('55130','Moro med marsipan','298.50','10','140','C20');
INSERT INTO Vare VALUES('15211','Tubeflue verktøy','209.00','7','39','B42');
INSERT INTO Vare VALUES('42615','Gipsform marihøner','106.00','3','124','B03');
INSERT INTO Vare (VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('64551','Hengebegonia, 10 stk.','118.00','16','206',NULL);

SELECT *
FROM Vare;
