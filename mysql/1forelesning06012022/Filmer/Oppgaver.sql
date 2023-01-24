USE `oppgave1kap2`;

SELECT *
FROM Film;

-- 1a) all info om filmer produsert i 1988
SELECT *
FROM Film
Where År LIKE 1988;
-- EVENTUELT
SELECT *
FROM Film
Where År=1988;

-- 1b) Tittel på amerikanske filmer produsert på 80-tallet
SELECT Tittel
FROM Film
WHERE (År BETWEEN 1980 AND 1990) AND Land='USA';

-- 1c) komedier med aldersgrense under 10 år og lengde under 130 min
SELECT *
FROM Film
WHERE Sjanger='Komedie' AND Alder<10 AND Tid<130;
-- 1d) tittel på alle action- og western-filmer
SELECT *
FROM Film
WHERE Sjanger='Action' OR Sjanger='Western';
-- 1e) alle produksjonsland sortert og uten gjentagelse
SELECT DISTINCT Land
FROM Film
ORDER BY Land;
-- 1i) filmer med tittel som slutter på 'now'
SELECT *
FROM Film
WHERE Tittel LIKE '%now';