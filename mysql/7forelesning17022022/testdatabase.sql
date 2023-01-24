-- om datatyper, INSERT, AlTER TABLE, fremmednøkler

DROP SCHEMA IF EXISTS testdatabase;
CREATE SCHEMA testdatabase;

USE testdatabase;

CREATE TABLE Datatyper
(
Postnr1 INTEGER,
Postnr2 CHAR(4),
Dato1 DATE,
Dato2 DATE
);

INSERT INTO Datatyper VALUES(0304,'0304','2022-02-17',20220217);

SELECT *
FROM Datatyper;
-- her blir utskriften i første kollonne 304 og ikke 0304 fordi det første taller er 0

CREATE TABLE Telefonliste
(
Mobilnr CHAR(8) PRIMARY KEY,
Fornavn CHAR(15)
);

INSERT INTO Telefonliste VALUES('41285761','Roman');

ALTER TABLE Telefonliste ADD COLUMN Epost CHAR(30);

SELECT *
FROM Telefonliste;
-- her vil kolonne Epost være NULL da den ikke har data enda

UPDATE Telefonliste
SET Epost='romanko7@hotmail.com'
WHERE Mobilnr='41285761';

SELECT *
FROM Telefonliste;
-- nå har også Epost-kolonnen fått data

CREATE TABLE Postkatalog
(
Postnr CHAR(4) PRIMARY KEY,
Poststed CHAR(20) NOT NULL
);

ALTER TABLE Telefonliste ADD COLUMN Postnr CHAR(4);
ALTER TABLE Telefonliste ADD CONSTRAINT TelefonlistePostkatalogFK FOREIGN KEY
(Postnr) REFERENCES Postkatalog(Postnr);

INSERT INTO Postkatalog VALUES ('3470','Slemmestad');
INSERT INTO Postkatalog VALUES ('6400','Molde');

UPDATE Telefonliste
SET Postnr='3470'
WHERE Mobilnr='41285761';

SELECT *
FROM Telefonliste;

-- legger til 99999999 Jens på postnr 6400, ok eller ikke?
INSERT INTO Telefonliste (Mobilnr, Fornavn, Postnr)
VALUES ('99999999','Jens','6400');
-- OK, epost-feltet blir satt til null da eposten til jens ikke er oppgitt
SELECT *
FROM Telefonliste;
-- legger til 44444444 Kari på postnr 7800, ok eller ikke? Se ned!!
INSERT INTO Telefonliste(Mobilnr, Fornavn, Postnr)
VALUES ('444444444','Kari','7800');

SELECT *
FROM Telefonliste;
-- Kari kan ikke legges inn fordi postnr 7800 ikke finnes i tabellen Postkatalog
-- dette fikses her!
INSERT INTO Postkatalog VALUES ('7800','Namsos');
INSERT INTO Telefonliste (Mobilnr, Fornavn, Postnr)
VALUES ('44444444','Kari','7800');

SELECT *
FROM Telefonliste;
-- I og med at postnummeret 7800 Namsos finnes i Postkatalog, er Kari nå blitt lagt i databasen
-- merk at også hun vil få nullmerke på epost, da den ikke ble innserted i Telefonlista

