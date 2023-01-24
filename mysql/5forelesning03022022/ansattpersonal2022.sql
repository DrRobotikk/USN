-- Skript for basisstruktur ansattpersonal2022
DROP SCHEMA IF EXISTS ansattpersonal2022; -- ok
CREATE SCHEMA ansattpersonal2022; -- ok

USE ansattpersonal2022; -- ok

-- oppretter tabeller, runde (1)
CREATE TABLE Stillingstype -- ok
(
Stillingskode CHAR(4),
Stillingsbetegnelse CHAR(20) NOT NULL,
CONSTRAINT StillingstypePK PRIMARY KEY(Stillingskode)
);

CREATE TABLE Avdeling -- ok
(
Avdelingsnr CHAR(4),
Avdelingsnavn CHAR(20) NOT NULL,
CONSTRAINT AvdelingPK PRIMARY KEY(Avdelingsnr)
);

CREATE TABLE Kurs -- ok
(
Kursnr CHAR(4),
Kursnavn CHAR(20) NOT NULL,
CONSTRAINT KursPK PRIMARY KEY(Kursnr)
);

CREATE TABLE Postkatalog -- ok
(
Postnr CHAR(4),
Poststed CHAR(20) NOT NULL,
CONSTRAINT PostkatalogPK PRIMARY KEY(Postnr)
);
-- Oppretter tabeller runde (2)
CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn VARCHAR(15) NOT NULL,
Etternavn VARCHAR(20) NOT NULL,
Gateadresse CHAR(25) NOT NULL,
Telefonnr CHAR(8) NOT NULL,
Stillingskode CHAR(4),
Avdelingsnr CHAR(4),
Postnr CHAR(4) NOT NULL,
CONSTRAINT AnsattPK PRIMARY KEY(Ansattnr),
CONSTRAINT AnsattStillingstypeFK FOREIGN KEY(Stillingskode) REFERENCES 
Stillingstype(Stillingskode),
-- her kommer det ekstra kode (ON DELETE...) for å sette avdelingsnr til NULL dersom
-- tabell Avdeling blir slettet (f.eks. om usn campus ringerike blir lagt ned)
CONSTRAINT AnsattAvdelingFK FOREIGN KEY(Avdelingsnr) REFERENCES
Avdeling(Avdelingsnr) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT AnsattPostkatalogFK FOREIGN KEY(Postnr) REFERENCES
Postkatalog(Postnr)
);

CREATE TABLE Kursdeltagelse
(
Ansattnr CHAR(4),
Kursnr CHAR(4),
Dato DATE,
Vurdering CHAR(20),
CONSTRAINT KursdeltagelsePK PRIMARY KEY(Ansattnr,Kursnr,Dato),
CONSTRAINT AnsattKursdeltagelseFK FOREIGN KEY(Ansattnr) REFERENCES
Ansatt(Ansattnr),
CONSTRAINT KursKursdeltagelseFK FOREIGN KEY(Kursnr) REFERENCES
Kurs(Kursnr),
CONSTRAINT Vurderingsregel CHECK(Vurdering IN('Godkjent','Ikke godkjent'))
);

USE `ansattpersonal2022`;

INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('1000','Avdelingsjef');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('2000','Konsulent');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('3000','Økonomi medarbeider');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('4000','Sekretær');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('5000','Trainee');

INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('1000','IT');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('2000','Administrasjon');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('3000','Økonomi');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('4000','Personal');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('5000','Vedlikehold');

INSERT INTO Postkatalog(Postnr,Poststed) VALUES('1000','Storeby');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('1500','Lilleby');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('2000','Mellomby');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('2500','Storbygd');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('3000','Lillebygd');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('3500','Mellombygd');

INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('1000','HMS');
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('2000','Brannvakt');
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('3000','Førstehjelp');
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('4000','Sistehjelp');

INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('1000','Ole','Olsen','Olsenveien 01','11111111','1000','2000','2000');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('2000','Hans','Hansen','Hansenveien 02','22222222','2000','1000','1500');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('3000','Jens','Jensen','Jensenveien 03','33333333','3000','4000','1000');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('4000','Trine','Trinesen','Trinesenveien 04','44444444','4000','3000','2500');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('5000','Kari','Karisen','Karisenveien 05','55555555','5000','5000','3000');

INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','1000','1999-10.06','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','2000','1999-10.06','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','1000','1999-11.06','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','2000','1999-10.01','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('3000','3000','1998-10.06','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('4000','2000','1999-10.06','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','2000','1999-10.07','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','3000','1999-10.06','Ikke Godkjent');

SELECT *
FROM Ansatt;
