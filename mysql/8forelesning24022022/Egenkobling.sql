-- Egenkobling
-- Du kan lage databasen på følgende måte
-- 1) kopier tabelldefinisjonen Ansatt Fra Hobbyhuset
-- og legg til kolonnen Leder, smallint(6)
-- fjern definisjonen av Fremmednøkkelen på postnr
-- legg til fremmednøkkel Leder som refererer til Ansatt(Ansattnr)
-- men da må du gjøre om på inndatarekkefølgen slik at sjefene er registrert 
-- før de de leder, altså må inndatalinjene omrokkeres slik at ledere må stå
-- øverst
-- 2) Kopier inndatasettningene fra Hobbyhuset
-- legg inn leder for hver ansatt tilsvarende figur 
-- 4.6 s104 ('insert lederNr i starten av hver inndatalinje')

DROP SCHEMA IF EXISTS Egenkobling;
CREATE SCHEMA Egenkobling;

USE Egenkobling;

CREATE TABLE Ansatt
(
  AnsNr       SMALLINT,
  Fornavn     VARCHAR(50) NOT NULL,
  Etternavn   VARCHAR(50) NOT NULL,
  Adresse     VARCHAR(100),
  PostNr      CHAR(4) NOT NULL,
  Fødselsdato DATE,
  Kjønn       CHAR(1),
  Stilling    VARCHAR(50),
  Årslønn     DECIMAL(8,2) NOT NULL,
  Leder       SMALLINT(6),
  CONSTRAINT AnsattPK PRIMARY KEY (AnsNr),
  CONSTRAINT LederAnsattFK FOREIGN KEY (Leder) REFERENCES Ansatt(AnsNr)
);

INSERT INTO Ansatt (Leder,AnsNr, Fornavn, Etternavn, Adresse, PostNr, Fødselsdato, Kjønn, Stilling, Årslønn) VALUES
(NULL,2, 'Gunnlaug', 'Angeltveit', 'Langmyrgrenda 9', '3800', '1969-03-29', 'K', 'Markedssjef', '643200.00'),
(2,7, 'Henriette', 'Brobakken', 'Stubberud Sognsvann 1', '3800', '1971-10-01', 'K', 'Daglig leder', '833800.00'),
(2,8, 'Synøve', 'Bakketun', 'Vassøyveien 7', '3840', '1985-05-15', 'K', 'Kundebehandler', '518100.00'),
(2,1, 'Georg', 'Barth', 'Kringsjågrenda 3F', '3841', '1982-10-20', 'M', 'Lagerleder', '604900.00'),
(7,3, 'Morgan', 'Dalland', 'Jansbergveien 19', '3830', '1974-01-10', 'M', 'Innkjøper', '670500.00'),
(8,6, 'Vilde', 'Aksnes', 'Minister Ditleffs vei 44', '3810', '1977-10-11', 'K', 'Databaseadministrator', '693200.00'),
(7,9, 'Ragnvald', 'Allum', 'Utsikten 4', '3812', '1992-03-07', 'M', 'Kundebehandler', '484700.00'),
(7,11, 'Oliver', 'Abrahamsen', 'Tarjei Vesaas\' vei 3A', '3812', '1989-01-20', 'M', 'Lagermedarbeider', '466900.00'),
(8,13, 'Oda', 'Cappelen', 'Norheimskneiken 12', '3800', '1991-02-28', 'K', 'Produktutvikler', '653100.00'),
(7,16, 'Andrine', 'Ebbesen', 'Kristianias gate 9', '3800', '1988-12-27', 'K', 'Regnskapssekretær', '532300.00');

USE Egenkobling;
SELECT AnsNr, Fornavn, Etternavn, Leder
FROM Ansatt;

SELECT *
FROM Ansatt;
-- alle ansatte med navn på leder
SELECT A.AnsNr, A.Etternavn, A.Fornavn, Leder.Etternavn AS HarSomLeder
FROM Ansatt AS A, Ansatt AS Leder
WHERE A.Leder=Leder.AnsNr
ORDER BY HarSomLeder, A.Etternavn, A.Fornavn;

-- Oppgave:
-- Lag SQL-setning slik at du også får med de ansatte som ikke har leder (s.107)
-- RIGHT OUTER JOIN
SELECT Ansatte.AnsNr, Ansatte.Fornavn, Ansatte.Etternavn, Leder.Etternavn AS HarSomLeder
FROM (Ansatt AS Leder) RIGHT OUTER JOIN (Ansatt AS Ansatte)
	ON Leder.AnsNr=Ansatte.Leder
ORDER BY HarSomLeder;

-- her får vi med lederen også
-- LEFT OUTER JOIN
SELECT Ansatte.AnsNr,Ansatte.Fornavn,Ansatte.Etternavn,Lederen.Etternavn AS
HarSomLeder
FROM (Ansatt AS Ansatte) LEFT OUTER JOIN (Ansatt AS Lederen)
ON Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.Fornavn;

-- View for produksjon av salgsrapporter
-- Oppgave:
-- Bruke view'et sammen med andre tabeller for å lage ulike salgsrapporter
USE Hobbyhuset;

CREATE VIEW Salg AS
(
SELECT OL.*, V.Betegnelse, K.Navn AS Kategori, O.OrdreDato, O.Knr
FROM Ordre AS O, Ordrelinje AS OL, Vare AS V, Kategori AS K
WHERE OL.OrdreNr=O.OrdreNr
	AND OL.VNr=V.VNr
		AND V.KatNr=K.KatNr
);

SELECT *
FROM Salg;

SELECT *
FROM Ordrelinje;

-- Kunder uten bestillinger ved bruk av NOT EXISTS
-- resultatet ble 107 kunder
SELECT *
FROM Kunde
WHERE NOT EXISTS
	(SELECT KNr FROM ordre
    WHERE Kunde.KNr=Ordre.KNr);

-- Kunder med bestillinger ved hjelp av EXISTS
-- resultatet ble 405 kunder
SELECT*
FROM Kunde
WHERE EXISTS
	(SELECT KNr FROM ordre
    WHERE Kunde.KNr=Ordre.KNr);


-- NATURAL JOIN brukes/ Anbefalles IKKE
USE Ansattpersonal2022;

SELECT *
FROM Ansatt NATURAL JOIN Stillingstype;

SELECT *
FROM Ansatt NATURAL JOIN Stillingstype NATURAL JOIN Avdeling;

-- Mer om del-spørringer
-- Varer billigere enn gjennomsnittet
-- resultatet ble 142 rader
USE Hobbyhuset;

SELECT VNr, Betegnelse, Pris
FROM Vare
WHERE Pris<(SELECT AVG (Pris) FROM Vare)
-- ORDER BY Pris
;

-- Vekselvirkende delspørringer
-- billigste vare i hver kategori, Alternativ 1:
-- resultatet blir 20 rader, men det finnes flere varer med samme pris
-- så det vi vet er at det finnes færre enn 20 billigste varer i hver kategori
SELECT Vare1.VNr, Vare1.Betegnelse, Vare1.KatNr, Vare1.Pris
FROM Vare AS Vare1
WHERE Vare1.Pris=
		(SELECT MIN(Vare2.Pris)
		FROM Vare AS Vare2
			WHERE Vare1.KatNr=Vare2.KatNr)
;

-- Oppgaver
-- 1) Løs ved bruk av et View (alternativ 2)
-- VIEW'et blir BilligsteIKategori
drop view if exists BilligsteIKategori;
CREATE VIEW BilligsteIKategori AS
(
SELECT KatNr, MIN(Pris) AS Billigste
FROM Vare
GROUP BY KatNr
);

-- her blir resultatet 17 linjer, selv om det
-- finnes flere varer med samme laveste pris (20)
SELECT *
FROM BilligsteIKategori;

SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM Vare,BilligsteIKategori
WHERE Vare.KatNr=BilligsteIKategori.KatNr
	AND Vare.Pris=BilligsteIKategori.Billigste;

-- lekse fra forelesning 8 alternativ 3:
-- BilligsteIKategori som navngitt spørring og 
-- spørring i FROM-delen
SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM Vare, (SELECT KatNr, MIN(Pris) AS Billigste
			FROM Vare
            GROUP BY KatNr) AS BiK
WHERE Vare.KatNr=BiK.KatNr
	AND Vare.Pris=BiK.Billigste;
