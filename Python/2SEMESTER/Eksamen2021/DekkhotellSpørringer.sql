USE Dekkhotell;

SELECT *
FROM Oppbevaring;

SELECT Regnr,Innlevert
FROM Oppbevaring
WHERE Utlevert IS NULL
ORDER BY Innlevert ASC;

SELECT Etternavn,Epost,Oppbevaring.Mobilnr,Hylle
FROM Kunde JOIN Oppbevaring USING(Mobilnr)
WHERE Oppbevaring.Regnr='FF55555' AND Utlevert IS NULL;

SELECT *
FROM Kunde

SELECT *
FROM Dekksett

SELECT *
FROM Oppbevaring
