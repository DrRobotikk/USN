USE oblig2022;

-- Vitnemål, ved flere avlagte eksamener i samme emne skal kun ett/beste resultat komme på vitnemålet. 
-- Emnene sorteres på emnekode, dvs alle emnekoder i 1000-serien sorteres og kommer før 2000...
-- Vitnemålet må ha en summering av antall oppnådde studiepoeng for beståtte emner  
--  WHERE UPPER(Betegnelse) LIKE '%MARSIPAN%

SELECT Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Karakter,Studiepoeng
FROM Emne JOIN Eksamensresultat JOIN Student
	ON (Eksamensresultat.Studentnr=Student.Studentnr)
		ON(Emne.Emnekode=Eksamensresultat.Emnekode)
WHERE Eksamensresultat.Studentnr='1001' AND Karakter IS NOT NULL
GROUP BY Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Karakter,Studiepoeng 
ORDER BY RIGHT(Emne.Emnekode,4) ASC;

-- Andreas sin spørring
SELECT MIN(Karakter) AS Karakter, Studentnr, Emnekode, Emnenavn, Dato, Fornavn, Etternavn,Studiepoeng
FROM Eksamensresultat 
    JOIN Emne USING (Emnekode)
    JOIN Student USING(Studentnr)
WHERE Studentnr='1001'
GROUP BY Emnekode
ORDER BY Emnekode ASC;

-- Min egen spørring
SELECT Student.Studentnr, Emne.Emnekode, Emnenavn, Dato, Fornavn, Etternavn, Studiepoeng, MIN(Karakter) AS Karakter
FROM Student JOIN Eksamensresultat JOIN Emne
	ON(Eksamensresultat.Emnekode=Emne.Emnekode)
		ON(Student.Studentnr=Eksamensresultat.Studentnr)
WHERE Student.Studentnr='1001'
GROUP BY Student.Studentnr, Emne.Emnekode,Emnenavn,Fornavn,Etternavn,Studiepoeng
ORDER BY Emne.Emnekode ASC;

-- Christian sin spørring
SELECT s.*, r.Karakter, r.Emnekode
FROM Student AS s
    JOIN (
    SELECT MIN(Karakter) AS Karakter, Emnekode, Studentnr FROM Eksamensresultat
    WHERE Studentnr = '1001'
    GROUP BY Emnekode, Studentnr) as r
on s.Studentnr = r.Studentnr;


-- bør være ok til nest siste oppgave AntallStudiepoeng
SELECT SUM(Studiepoeng) AS AntallStudiepoeng
FROM Emne JOIN Eksamensresultat
	ON(Emne.Emnekode=Eksamensresultat.Emnekode)
WHERE Eksamensresultat.Studentnr='1010' AND Karakter<'F' AND Karakter IS NOT NULL;


SELECT Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Studiepoeng, MIN(Karakter) AS Karakter
FROM Emne JOIN Eksamensresultat JOIN Student
	ON (Eksamensresultat.Studentnr=Student.Studentnr)
		ON(Emne.Emnekode=Eksamensresultat.Emnekode)
WHERE Eksamensresultat.Studentnr='1001' AND Karakter IS NOT NULL
GROUP BY Karakter 
ORDER BY RIGHT(Emne.Emnekode,4) ASC, (Emne.Emnekode)ASC, Dato ASC;


SELECT Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Karakter,Studiepoeng
FROM Emne 
	JOIN Eksamensresultat USING(Emnekode)
    JOIN Student USING (Studentnr)
WHERE Studentnr='1001' AND Emnekode='INF1000'
GROUP BY Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Karakter,Studiepoeng
HAVING Karakter LIKE (SELECT MIN(Karakter) AS Karakter FROM Eksamensresultat WHERE Emnekode='INF1000');



-- Christian sin kode som er godkjent
SELECT R1.Karakter, R1.Studentnr, R1.Emnekode, Emnenavn, R1.Dato, Fornavn, Etternavn,Studiepoeng
FROM Eksamensresultat AS R1
	JOIN Emne USING (Emnekode)
	JOIN Student USING (Studentnr)
WHERE R1.Karakter =
(SELECT MIN(R2.Karakter) FROM Eksamensresultat AS R2 WHERE R1.Emnekode = R2.Emnekode AND R1.Studentnr = R2.Studentnr)
AND R1.Studentnr = '1001';

-- Endelig kode for Vitnemål
SELECT R1.Emnekode, Emnenavn, Fornavn, Etternavn, R1.Dato, R1.Karakter, Studiepoeng
FROM Student JOIN (Eksamensresultat AS R1) JOIN Emne
	ON(R1.Emnekode=Emne.Emnekode)
		ON(Student.Studentnr=R1.Studentnr)
WHERE R1.Karakter =(
	SELECT MIN(R2.Karakter) 
	FROM Eksamensresultat AS R2 
    WHERE R1.Emnekode = R2.Emnekode AND R1.Studentnr = R2.Studentnr) AND R1.Studentnr = '1001'
ORDER BY RIGHT(R1.Emnekode,4) ASC, (R1.Emnekode)ASC;






SELECT Fornavn,Etternavn,Emne.Emnekode,Studiepoeng,Karakter
FROM Student JOIN Eksamensresultat JOIN Emne
	ON (Eksamensresultat.Emnekode=Emne.Emnekode)
		ON(Student.Studentnr=Eksamensresultat.Studentnr)
WHERE Student.Studentnr='1001'

