USE ansattpersonal2022;

-- data i tabellen Ansatt
SELECT *
FROM Ansatt;

-- data i tabellen Postkatalog
SELECT *
FROM Postkatalog;

-- Kryssprodukt av Postkatalog og Ansatt
-- denne printer all data fra begge tabellene, så om begge tabellene har 5
-- poster, så blir resultatet 5x5=25 linjer med alle kombinasjoner
SELECT *
FROM Postkatalog, Ansatt;

-- Likekobling, liste over ansatte med postadresser, med WHERE-betingelse
-- her vil den sammenligne postnr i begge tabellene og
-- kun vise de postene der postnr er like
SELECT *
FROM Ansatt,Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- som over, men med kolloneutvalg
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt,Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- Likekobling, liste over ansatte med postadresse, med INNER JOIN
-- dette er kun en annen måte å få samme resultat som med 
-- Likekobling med WHERE-betingelse
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt INNER JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;

-- Likekobling 3 tabeller, liste over ansatte med stilling og avdeling, 
-- med WHERE-betingelser
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;

-- koble 3 eller flere tabeller, først 2, "steg-for-steg" tankegang
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Poststed, Avdelingsnavn
FROM Ansatt, Stillingstype, Postkatalog, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Postnr=Postkatalog.Postnr
		AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;

-- likekobling av 3 eller flere, med INNER JOIN
-- her er det kjempeviktig å velge riktige tabeller utifra
-- hvordan de er satt sammen
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Avdeling INNER JOIN 
	(Ansatt INNER JOIN Stillingstype
		ON Ansatt.Stillingskode=Stillingstype.Stillingskode)
		ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;

-- View/ Utsnitt
-- oppretting av View Ansattliste
-- Etternavn, Fornavn, Stilling, Avdeling med info fra de 3 tabellene
-- Ansatt, Stillingstype, Avdeling
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

-- ytre koblinger
-- ønsker også stillingsbetegnelser som ikke er i bruk (ingen har pt)
SELECT *
FROM Stillingstype LEFT OUTER JOIN ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;

-- ekvivalent med (samme spørreresultat, annen presentasjon)
SELECT *
FROM Ansatt RIGHT OUTER JOIN Stillingstype
	ON Ansatt.Stillingskode=Stillingstype.Stillingskode;

-- ønsker også avdelinger som ingen er tilknytta pt
SELECT *
FROM Avdeling LEFT OUTER JOIN Ansatt
	ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;

-- ekvivalent med (samme spørreresultat, annen presentasjon)
SELECT *
FROM Ansatt RIGHT OUTER JOIN Avdeling
	ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;