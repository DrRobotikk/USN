-- Importerer databasen inn i querytab 
USE hobbyhusetkap2;
-- Leser alle postene i tabellen
SELECT *
FROM Vare

-- Varer som koster under 100 kr i kategoriene bøker, keramikk
SELECT *
FROM Vare
WHERE (Pris<100) AND ((Kategori='Bøker') OR (Kategori='Keramikk'))

-- VNr, Betegnelse, Pris og beregning a PrisInklMva avrundet med 2 desimaler
SELECT VNr, Betegnelse, Pris, ROUND(Pris*1.25,2) AS PrisInklMva
FROM Vare

-- VNr, Betegnelse og Hyllebokstav navngitt som Hylleseksjon
SELECT VNr, Betegnelse, LEFT (Hylle,1) AS Hylleseksjon
FROM Vare

-- varer som koster mellom 57 og 75,50 kr
-- først med bruk av logiske operatorer
SELECT *
FROM Vare
WHERE (Pris>=57) AND (Pris<=75.50)

-- så ved bruk av BETWEEN
SELECT *
FROM Vare
WHERE Pris BETWEEN 57 AND 75.50

-- Varer med varenavn som begynner på M
-- først med mønstersammenligning (LIKE)
SELECT *
FROM Vare
WHERE UPPER(Betegnelse) LIKE 'M%';

-- så med test på likhet (=)
SELECT *
FROM Vare
WHERE UCASE(LEFT(Betegnelse,1))='M';

-- Varer som inneholder 'marsipan' i navnet
SELECT *
FROM Vare
WHERE UPPER(Betegnelse) LIKE '%MARSIPAN%'

-- Alle varer sortert på kategori stigende og pris synkende
SELECT *
FROM Vare
ORDER BY Kategori ASC, Pris DESC

-- beregning av gjennomsnittspris for varer i kategorien Fiske,
-- avrundet med 2 desimaler
SELECT ROUND(AVG(Pris),2) AS GjennomsnittsPris
FROM Vare
WHERE UPPER(Kategori='FISKE');

-- Totalt antall varer i kategoriene Blomsterfrø og Blomsterløker
SELECT COUNT(*) AS AntallBlomsterVarer
FROM Vare
WHERE UPPER (Kategori) LIKE 'BLOMSTER%';

-- Alle kategorier som har flere enn 1 AntallVarer
SELECT Kategori, COUNT(*) AS AntallVarer
FROM Vare
GROUP BY Kategori
HAVING COUNT(*)>1;