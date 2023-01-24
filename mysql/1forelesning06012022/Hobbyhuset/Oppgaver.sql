USE `hobbyhusetkap2`;

-- 1a) skriv ut hele tabellen
SELECT *
FROM Vare;

-- 1b) skriv ut hele tabellen sortert etter varenr
SELECT *
FROM Vare
ORDER BY VNr;

-- 1c) hele varesortimentet/vareutvalget (varenr og varenavn) 
SELECT VNr, Betegnelse
FROM Vare;

-- 1d) alle kategoriene for en vare (med dubletter) 
SELECT Kategori
FROM Vare;

-- 1e) alle kategoriene for en vare (uten dubletter) 
SELECT DISTINCT Kategori
FROM Vare;

-- 1f) alle varene i kategorien ‘Fiske’
SELECT *
FROM Vare
WHERE Kategori='Fiske';

-- 1g) alle varene i kategorien fiske, generell løsning som tar hensyn til at 
--     kategorinavnet kan være registrert på forskjellige måter
SELECT *
FROM Vare 
WHERE Kategori LIKE '%iske';

-- 1h) alle varer med en pris under 100 kr
SELECT *
FROM Vare
WHERE Pris<100;

-- 1i) alle varer med en pris på 100 kr eller mere 
SELECT *
FROM Vare
WHERE Pris>=100;

-- 1j) alle varer med en pris i intervallet [100,200] kr 
SELECT *
FROM Vare
WHERE Pris BETWEEN 100 AND 200;
-- EVENTUELT
SELECT *
FROM Vare
WHERE Pris>=100 AND Pris<=200;

-- 1k) alle varer som ikke er hylleplasserte 
SELECT *
FROM Vare
WHERE Hylle IS NULL;

-- 1l) alle varer som er hylleplasserte 
SELECT *
FROM Vare
WHERE Hylle IS NOT NULL;