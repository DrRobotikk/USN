USE ansattpersonal2022;

-- lager et view/ egendefinert liste ved navn Ansattliste
DROP VIEW IF EXISTS Ansattliste;

CREATE VIEW Ansattliste (Etternavn, fornavn, Stillingstype, Avdeling) AS 
(SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr);

-- kan så kjøre spørringer mot VIEW'et
SELECT *
FROM Ansattliste
ORDER BY Etternavn;

-- kryssprodukt (den printer all info fra begge tabellene flere ganger-
-- altså om det finnes 5 poster i hver tabell så vil kryssproduktet bli
-- 25 linjer totalt, men kun 5 av de vil inneholde den riktige informasjonen
SELECT *
FROM Ansatt INNER JOIN Postkatalog;

SELECT *
FROM Ansatt JOIN Postkatalog;

-- likekobling
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;

SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt JOIN Postkatalog
	USING(Postnr);
    
-- NB!!!! Her begynner det å bli komplisert
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Stillingstype JOIN
	(Ansatt JOIN Avdeling
		USING(Avdelingsnr))
	USING(Stillingskode);

-- ytre kobling
SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;

SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	USING(Stillingskode);

-- algoritme-forklaringer
USE Hobbyhuset;

-- første SELECT s.102
SELECT Ordre.*, Fornavn, Etternavn, Poststed
FROM Ordre, Kunde, Poststed
WHERE Ordre.KNr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr;

-- Siste SELECT'n s.103
SELECT Kunde.KNr, Etternavn, COUNT(*) AS AntallOrdre
FROM Kunde, Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr, Etternavn
-- neste linje viser kun de kundene som har 10 eller flere ordre
HAVING AntallOrdre>=10;

-- kortnavn/ alias
SELECT K.KNr, Etternavn, COUNT(*) AS AntallOrdre
FROM Kunde AS K, Ordre AS O
WHERE K.KNr=O.KNr
GROUP BY K.KNr, Etternavn
HAVING AntallOrdre>=10;

-- introduksjon til del-spørringer, del-spørringer i betingelser
USE Hobbyhuset;

-- antall bestillinger i ordretabellen
SELECT KNr
FROM Ordre;
-- svaret ble 2192

SELECT *
FROM Kunde;
-- det finnes 512 kunder i Kunde-tabellen

-- hvem har "bestilt varer"?
SELECT *
FROM Kunde
WHERE KNr IN (SELECT KNr FROM Ordre);
-- av 512 kunder er det 405 kunder med bestillinger

-- kunder som aldri har bestilt
SELECT *
FROM Kunde
WHERE KNr NOT IN (SELECT KNr FROM Ordre);
-- svaret er 107 kunder

-- forelesning 24022022 (Kunder uten bestillinger ved bruk av NOT EXISTS)
-- NOT EXISTS kan ha verdier TRUE/ FALSE
SELECT *
FROM Kunde
WHERE NOT EXISTS
	(SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);

-- forelesning 24022022 (Kunder med bestillinger ved bruk av EXISTS)
-- EXISTS Kan ha verdier TRUE/ FALSE
SELECT *
FROM Kunde
WHERE EXISTS
	(SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);


-- view'et "GodeKunder"
CREATE VIEW GodeKunder AS 
(
SELECT *
FROM Kunde
WHERE KNr IN
	(SELECT KNr FROM Ordre)
);

-- spørre mot view'et istedet
SELECT *
FROM GodeKunder;

