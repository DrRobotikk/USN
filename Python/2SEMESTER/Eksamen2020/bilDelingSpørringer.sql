use bilDeling;
-- Lag et vindu hvor du har en liste med alle utleier som ikke er avslutta (regnr og utlevert), sortert på 
-- utleveringstidspunkt, og når en velger i lista får en informasjon om hvem som leier bilen (mobilnr, 
-- fornavn og etternavn). 
-- Oppgave 3:
SELECT regnr,utlevert,kunde.mobilnr,fornavn,etternavn
from utleie join kunde using(mobilnr)
where innlevert is null;

SELECT mobilnr,fornavn,etternavn
FROM kunde JOIN utleie USING (mobilnr)
WHERE utleie.regnr='%s';
-- Oppgave 4:
SELECT regnr,utlevert,innlevert
FROM utleie
WHERE utlevert<=CURRENT_TIMESTAMP() AND innlevert<=CURRENT_TIMESTAMP();

SELECT regnr,utlevert
FROM utleie
WHERE innlevert IS NOT NULL;
-- 
SELECT kunde.mobilnr,utlevert,innlevert,beløp
FROM kunde LEFT OUTER JOIN utleie USING(mobilnr)
WHERE innlevert IS NOT NULL

SELECT regnr,merke,modell
FROM bil
WHERE regnr NOT IN(SELECT regnr FROM utleie WHERE innlevert IS NULL)

SELECT *
FROM utleie
ORDER BY utlevert ASC


