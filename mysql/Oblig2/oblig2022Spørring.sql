USE bysykkelordning;

-- B.
SELECT *
FROM Sykkel;

-- C
SELECT Etternavn, Fornavn, Mobilnr
FROM Kunde
ORDER BY Etternavn;

-- D
SELECT *
FROM Sykkel
WHERE Startdato>="20180401";

-- E
SELECT COUNT(*) AS AntallKunder
FROM Kunde;

-- F
SELECT Fornavn,Etternavn,Kunde.Mobilnr, COUNT(Utleie.Mobilnr) AS AntallUtleier
FROM Kunde LEFT OUTER JOIN Utleie
	ON Kunde.Mobilnr=Utleie.Mobilnr
GROUP BY Fornavn,Etternavn,Kunde.Mobilnr
ORDER BY AntallUtleier DESC;

-- G
SELECT *
FROM Kunde
WHERE Mobilnr NOT IN (SELECT Mobilnr FROM Utleie);

-- H
SELECT *
FROM Sykkel
WHERE SykkelID NOT IN(SELECT SykkelID FROM Utleie);

-- I
INSERT INTO Kunde VALUES
("+4711111111","Tore","Syklesen","1111222233334444");

-- J
DROP VIEW IF EXISTS LedigeSykler;
CREATE VIEW LedigeSykler (StativID,Sted,SykkelID) AS
(SELECT SST.StativID,SST.Sted,SykkelID
FROM Sykkelstativ AS SST,Sykkel
WHERE SST.StativID=Sykkel.StativID);

-- K
DROP USER IF EXISTS Sykkelsjef;
CREATE USER IF NOT EXISTS Sykkelsjef;

-- L
GRANT SELECT ON LedigeSykler TO Sykkelsjef;

-- M
SELECT SykkelID, COUNT(*) AS AntallUtleie
FROM Utleie
GROUP BY SykkelID
HAVING COUNT(*)>2
ORDER BY AntallUtleie DESC;

-- N
SELECT Kunde.Mobilnr,Fornavn,Etternavn, SUM(Utleie.Beløp) AS Totalbeløpet
FROM Kunde LEFT OUTER JOIN Utleie
	ON Kunde.Mobilnr=Utleie.Mobilnr
GROUP BY Kunde.Mobilnr,Fornavn,Etternavn
ORDER BY Totalbeløpet DESC;

-- O
SELECT S.StativID, Sted, COUNT(*) AS AntallLedigeSykler
FROM Sykkelstativ AS S, Sykkel
WHERE S.StativID=Sykkel.StativID
GROUP BY S.StativID,S.Sted;

-- P
SELECT K.Etternavn, K.Mobilnr, U.SykkelID, S.Startdato, U.Utlevert
FROM Kunde AS K, Utleie AS U, Sykkel AS S
WHERE (K.Mobilnr=U.Mobilnr
	AND U.SykkelID=S.SykkelID)
		AND U.Innlevert IS NULL;

-- Q
SELECT SykkelID,Fornavn,Etternavn,Kunde.Mobilnr
FROM Kunde,Utleie
WHERE Kunde.Mobilnr=Utleie.Mobilnr
		AND TIMESTAMPDIFF(HOUR,Utleie.Utlevert,Utleie.Innlevert)>24;

-- R
SELECT U.SykkelID, COUNT(U.Utlevert) AS FlestUtleier
FROM (Utleie AS U) JOIN (Utleie AS UT)
	ON U.SykkelID=UT.SykkelID
WHERE U.Utlevert LIKE UT.Utlevert
GROUP BY U.SykkelID
HAVING FlestUtleier=
	(SELECT MAX(FlestUtleier)
    FROM 
		(SELECT U.SykkelID, COUNT(U.Utlevert) AS FlestUtleier
        FROM (Utleie AS U) JOIN (Utleie AS UT)
			ON U.SykkelID=UT.SykkelID
		WHERE U.Utlevert LIKE UT.Utlevert
        GROUP BY U.SykkelID) AS Sammenligning);

-- BEDRE LØSNING
-- r) Lag en spørring som gir oversikt over den sykkelen/de syklene som har vært utleid flest ganger (flere kan altså ha «like mange og flest»).
-- Alt ok.
SELECT SykkelID, COUNT(SykkelID) AS Antall
FROM Utleie
GROUP BY SykkelID
HAVING COUNT(SykkelID) =
    (SELECT MAX(antallUtleid) FROM
        (SELECT SykkelID, COUNT(SykkelID) AS antallUtleid FROM Utleie GROUP BY SykkelID) 
        Utleie)
;