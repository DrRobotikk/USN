-- oppgave en var å fylle ut resten av databasen gruppering2022
USE gruppering2022;

SELECT *
FROM Ansatt;

-- oppgave 1 b) lag ulike SQL-setninger for å gruppere og «telle opp» på 
-- Stillingskode
-- Stillingskode,Lønnstrinn

SELECT Stillingskode, COUNT(Avdelingsnr) AS antallAnsatte
FROM Ansatt
GROUP BY Stillingskode;

SELECT Stillingskode,Lønnstrinn, COUNT(Ansattnr) AS antallAnsatte
FROM Ansatt
GROUP BY Stillingskode, Lønnstrinn;