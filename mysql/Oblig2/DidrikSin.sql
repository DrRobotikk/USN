USE bysykkelordning;

-- b) Lag en spørring som viser alle sykler.
-- Alt ok.
SELECT *
FROM Sykkel;

-- c) Lag en spørring som viser etternavn, fornavn og mobilnr for alle kunder, alfabetisert på etternavn.
-- Alt ok.
SELECT Etternavn, Fornavn, Mobilnr
FROM Kunde
ORDER BY Etternavn, Fornavn, Mobilnr;

-- d) Lag en spørring som viser alle sykler som er tatt i bruk etter 1.4.2018.
-- Alt ok.
SELECT *
FROM Sykkel
WHERE Startdato>"2018-04-01";

-- e) Lag en spørring som viser antallet kunder i By-sykkelordningen.
-- Alt ok.
SELECT COUNT(*) AS AntallKunder
FROM Kunde;

-- f) Lag en spørring som viser alle kunder og teller opp antallet utleieforhold for hver kunde. Oversikten skal også vise kunder som ennå ikke har leid sykkel.
-- Alt ok her. Ikke nødvendig å gi tabellene nytt navn/ alias i FROM-delen da de allerede heter «Kunde» og «Utleie».
SELECT Kunde.Mobilnr, Kunde.Fornavn, Kunde.Etternavn, COUNT(Utleie.Mobilnr) AS AntallUtleieforhold
From Kunde AS Kunde LEFT OUTER JOIN Utleie AS Utleie ON Kunde.Mobilnr=Utleie.Mobilnr
GROUP BY Kunde.Mobilnr, Kunde.Fornavn, Kunde.Etternavn;

-- g) Lag en spørring som gir oversikt over hvilke kunder som aldri har leid en sykkel.
-- Alt ok.
SELECT *
FROM Kunde
WHERE NOT EXISTS (
    SELECT *
    FROM Utleie
    WHERE Kunde.Mobilnr=Utleie.Mobilnr
);

-- h) Lag en spørring som viser hvilke sykler som aldri har vært utleid.
-- Alt ok.
SELECT *
FROM Sykkel
WHERE NOT EXISTS (
    SELECT *
    FROM Utleie
    WHERE Sykkel.SykkelID=Utleie.SykkelID
);

-- i) Lag sql-setningen for å registrere kunden (som er ny) «Tore Syklesen, +4711111111, 1111222233334444»
-- Alt ok.
INSERT INTO Kunde (Mobilnr, Fornavn, Etternavn, Betalingskortnr) VALUES ("+4711111111","Tore","Syklesen","1111222233334444");


-- j) Lag et View som viser hvilke sykler som er tilgjengelig ved hvert sykkelstativ. Lista skal inneholde StativID, Sted og SykkelID. Kall View’et LedigeSykler.
-- Alt ok.
Drop View IF EXISTS LedigeSykler;
CREATE VIEW LedigeSykler AS
(
    SELECT Sykkel.StativID, Sykkelstativ.Sted, Sykkel.SykkelID
    FROM Sykkel LEFT OUTER JOIN Sykkelstativ ON Sykkel.StativID=Sykkelstativ.StativID
    WHERE NOT EXISTS(
        SELECT *
        FROM Utleie
        WHERE Sykkel.SykkelID=Utleie.SykkelID
    )
);

SELECT *
FROM LedigeSykler;

-- k) Lag sql-setningen for å opprette brukeren Sykkelsjef.
-- Alt ok. Har fikk brukeren til og med et passord
DROP USER IF EXISTS "Sykkelsjef";
CREATE USER "Sykkelsjef" IDENTIFIED BY "oblig2022";

-- l) Lag sql-setningen for å gi brukeren Sykkelsjef lesetilgang til View’et LedigeSykler.
-- Alt ok
GRANT SELECT ON LedigeSykler TO "Sykkelsjef";

-- m) Lag en spørring som viser alle sykler som er leid ut mer enn 100 ganger. Lista skal presenteres i synkende rekkefølge med den sykkelen med flest utleie først.
-- Alt ok her. Muligens ikke nødvendig å ha med kolonne StativID og Låsnr da de kun vil vise verdien NULL.
SELECT Sykkel.SykkelID, Sykkel.Startdato, Sykkel.StativID, Sykkel.Låsnr, COUNT(Utleie.SykkelID) AS antallUtleid
FROM Sykkel LEFT OUTER JOIN Utleie ON Sykkel.SykkelID=Utleie.SykkelID
GROUP BY Sykkel.SykkelID, Sykkel.Startdato, Sykkel.StativID, Sykkel.Låsnr
HAVING antallUtleid>2
ORDER BY antallUtleid DESC;

-- n) Lag en spørring som viser mobilnr, fornavn, etternavn og totalbeløpet for alle utleier for hver enkelt kunde. Lista skal presenteres i synkende rekkefølge med den kunden som har betalt mest i leie først.
-- Spørringen summerer prisen for alle kundene som har leid. Burde kanskje hatt med de kundene som ikke har leid sykkel også?
SELECT Kunde.Mobilnr, Kunde.Fornavn, Kunde.Etternavn, SUM(Utleie.Beløp) AS Totalbeløp
FROM Kunde LEFT OUTER JOIN Utleie ON Kunde.Mobilnr=Utleie.Mobilnr
GROUP BY Kunde.Mobilnr, Kunde.Fornavn, Kunde.Etternavn
HAVING Totalbeløp>0
ORDER BY Totalbeløp DESC;

-- o) Lag en spørring som viser hvor mange ledige sykler som er tilgjengelig ved hvert sykkelstativ. Lista skal inneholde StativID, Sted og antall ledige sykler.
-- Alt ok
SELECT Sykkel.StativID, Sykkelstativ.Sted, COUNT(Sykkel.SykkelID) AS LedigeSykler
    FROM Sykkel JOIN Sykkelstativ ON Sykkel.StativID=Sykkelstativ.StativID
    WHERE NOT EXISTS(
        SELECT *
        FROM Utleie
        WHERE Utlevert IS NULL
    )
    GROUP BY Sykkel.StativID, Sykkelstativ.Sted;
    


-- p) Lag en spørring som viser oversikt over hvilke kunder som leier en bysykkel akkurat nå. Lista skal inneholde Etternavn, Mobilnr, SykkelID, StartDato og starttidspunkt for utleien.
-- Alt ok
SELECT Kunde.Etternavn, Kunde.Mobilnr, Utleie.SykkelID, Sykkel.Startdato, Utleie.Utlevert
FROM Kunde LEFT OUTER JOIN Utleie ON Kunde.Mobilnr=Utleie.Mobilnr LEFT OUTER JOIN Sykkel ON Utleie.SykkelID=Sykkel.SykkelID
WHERE Utleie.Innlevert IS NULL AND Utleie.Utlevert IS NOT NULL;


-- q) Lag en spørring som viser hvilke sykler, med informasjon om kunde, som ikke er levert tilbake etter ett døgn.
-- Alt ok
SELECT Sykkel.SykkelID, Kunde.Mobilnr, Kunde.Fornavn, Kunde.Etternavn
FROM Sykkel, Kunde JOIN Utleie ON Kunde.Mobilnr=Utleie.Mobilnr
WHERE Sykkel.SykkelID=Utleie.SykkelID AND Utleie.Innlevert IS NOT NULL AND TIMESTAMPDIFF(HOUR, Utleie.Utlevert, Utleie.Innlevert)>24;

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