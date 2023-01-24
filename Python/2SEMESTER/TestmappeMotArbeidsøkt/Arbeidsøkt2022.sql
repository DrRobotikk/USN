DROP SCHEMA IF EXISTS Arbeidsøkt2022;

CREATE SCHEMA Arbeidsøkt2022;

USE Arbeidsøkt2022;

CREATE TABLE Vare
(
VareNr INT(4),
Betegnelse CHAR(20),
CONSTRAINT VarePK PRIMARY KEY (VareNr)
);

INSERT INTO Vare (VareNr,Betegnelse) VALUES (1111,'Brød');
INSERT INTO Vare (VareNr,Betegnelse) VALUES (2222,'Smør');
INSERT INTO Vare (VareNr,Betegnelse) VALUES (3333,'Pålegg');

DROP USER IF EXISTS 'sjefen22';

CREATE USER IF NOT EXISTS 'sjefen22' IDENTIFIED BY 'sjefenpw';

GRANT SELECT ON Vare TO 'sjefen22';
GRANT INSERT ON Vare TO 'sjefen22';
GRANT UPDATE ON Vare TO 'sjefen22';
GRANT DELETE ON Vare TO 'sjefen22';

SELECT *
FROM Vare;