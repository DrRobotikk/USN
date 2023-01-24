USE hobbyhuset;

-- Grunnstrukturen av spørringer
-- Vi tuller ikke med denne grunnstrukturen

-- SELECT
-- FROM
-- WHERE
-- GROUP BY  Kan brukes uten HAVING
-- HAVING   Kan ikke brukes uten GROPU BY
-- ORDER BY

-- lekse fra forelesning 7:
-- Gullklubben, spørringer og senere VIEW for å plukke ut 
-- kunder med 10 eller flere bestillinger
-- Gullklubblista, 'liste til sjefen' med info om alle kunder
-- i Gullklubben
-- med info om alle kunder i 'Gullklubben' basert på
-- VIEW'et og tabellene Kunde og Poststed

CREATE VIEW Gullklubben AS
(
SELECT KNr, COUNT(*) AS AntallBestillinger
FROM Ordre
GROUP BY KNr
HAVING AntallBestillinger>=10
);

SELECT *
FROM Gullklubben;
-- antall kunder med flere enn 10 bestillinger er 20

-- Gullklubblista
CREATE VIEW Gullklubblista AS
(
SELECT Gullklubben.KNr, Fornavn, Etternavn, Adresse, Kunde.Postnr,
Poststed, AntallBestillinger
FROM Gullklubben, Kunde, Poststed
WHERE Gullklubben.KNr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr
);
SELECT *
FROM Gullklubblista;

SELECT *
FROM Gullklubblista
ORDER BY AntallBestillinger DESC;

-- Oppgave:
-- Gullklubblista som en spørring uten bruk av VIEW
-- Tips: PASS PÅ gruppekriteriet

SELECT Ordre.KNr,Fornavn, Etternavn,Adresse,Kunde.Postnr, Poststed, COUNT(Ordre.KNr) AS
	AntallBestillinger 
FROM Ordre,Kunde,Poststed
WHERE (Ordre.KNr=Kunde.KNr
		AND Kunde.Postnr=Poststed.Postnr)
GROUP BY Ordre.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed
HAVING AntallBestillinger>=10
ORDER BY AntallBestillinger DESC;


