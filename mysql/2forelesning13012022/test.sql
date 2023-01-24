USE `hobbyhusetkap2`;
-- avledet informasjon/ ny kolonne med navngivning og avrunding
SELECT VNr, Betegnelse, Pris, ROUND(Pris*1.25)
FROM Vare

-- Jokernotasjon/mønstersammenligning ved bruk av LIKE
-- Varer som begynner på M
SELECT *
FROM Vare
WHERE UPPER(Betegnelse) LIKE 'M%';

-- varer som begynner på M uten mønstersammenligning/ dvs uten likhet
SELECT *
FROM Vare
WHERE UCASE(LEFT(Betegnelse,1))='M';

-- Varer som inneholder 'marsipan' i navnet
SELECT*
FROM Vare
WHERE UPPER(Betegnelse) LIKE '%marsipan';

-- Sortering
-- ASC/stigende, DESC/synkende
SELECT *
FROM Vare
ORDER BY Kategori ASC, Pris DESC;

-- Mengdefunksjoner
-- Gjennomsnittpris
SELECT ROUND(AVG(Pris),2) AS Gjennomsnittspris

-- Gjennomsnittspris pr kategori
-- Utvidet med største og minste pris i hver kategori
SELECT Kategori, ROUND(AVG(Pris),2) AS GjennomsnittsPris,
	MIN(Pris) AS Billigste,
    MAX(Pris) AS Dyreste
FROM Vare
GROUP BY Kategori;

-- Opptelling, antall varer i kategoriene Blomsterfrø og blomsterløker
SELECT COUNT(*) AS AntallBlomsterVarer
FROM Vare
WHERE UPPER (Kategori) LIKE 'BLOMSTER%';

-- Gruppebetingelse
SELECT Kategori, COUNT(*) AS AntallVarer
FROM Vare
GROUP BY Kategori
HAVING COUNT(*)>1;