USE oppgave1kap2;
-- Oppgave: 
-- 1 g) Antall filmer som ikke er til salgs
SELECT COUNT(*) AS AntallFilmer
FROM Film
WHERE Pris IS NULL;
-- select count (*) vil regne med alt, mens 
-- select count (kolonneNavn) vil ikke regne med NULL-merker

-- 1 h) Antall filmer under 100 kr
SELECT COUNT(*) as FilmerU100
FROM Film
WHERE Pris<100;

-- 1 i) Filmer som slutter på now
SELECT *
FROM Film
WHERE UPPER(Tittel) LIKE '%NOW';

-- Oppgave 2:
-- a) Nummer og beskrivelse av hyttene som koster under 4500 kr og har flere enn 4 senger
SELECT Nr, Beskrivelse
FROM Hytte
WHERE (Pris<4500) AND (AntallSenger>=4);

-- b) Hytter med strøm og dusj sortert på stigende ukespris
-- Kollone strøm og dusj inneholder verdiene J og N
-- e)
SELECT COUNT(*) AS AntallHytter
FROM Hytte
WHERE AvstandAlpin<500;

-- Oppgave 3
-- når man søker på g så kommer marsipantanG med. søk derfor på både ',' og %g
USE hobbyhusetkap2;

SELECT *
FROM Vare
WHERE Betegnelse LIKE '%,%g'; -- det kan være hva som helst forran komma og forran g