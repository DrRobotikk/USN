USE ansattpersonal2022;

-- data i tabellen ansatt
SELECT *
FROM Ansatt;

-- data i tabellen postkatalog
SELECT *
FROM postkatalog;

-- kryssprodukt av Postkatalog og Ansatt
SELECT *
FROM Postkatalog, Ansatt;

-- likekobling, liste over ansatte med postadresser, med WHERE-betingelse
SELECT *
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.postnr;

-- med et kolloneutvalg
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- enten så kobler vi med WHERE-betingelse, eller med INNER JOIN
-- ikke lag mine egne varianter, ikke skriv WHERE INNER JOIN i en linje 

-- Likekobling, liste over ansatte med postadresser, med INNER JOIN
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt INNER JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;

-- Likekobling, 3 tabeller, liste over ansatte med stilling og avdeling, med
-- WHERE-betingelser
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingskode, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;

-- koble tre eller flere tabeller, først 2, "steg-for-steg" tankegang
-- DEN ER EGT IKKE KOMPLETT...SE PDF-SKRIPTET TIL STÅLE
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;



-- enten så kobler vi med WHERE-betingelse, eller med INNER JOIN
-- ikke lag mine egne varianter, ikke skriv WHERE INNER JOIN i en linje 