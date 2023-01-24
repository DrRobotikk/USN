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
VALUES('1000','Ole','Olsen','Olsenveien 01','11111111','1000','1000','1000');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('2000','Hans','Hansen','Hansenveien 02','22222222','2000','2000','1500');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('3000','Jens','Jensen','Jensenveien 03','33333333','3000','3000','2000');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('4000','Trine','Trinesen','Trinesenveien 04','44444444','4000','4000','2500');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) 
VALUES('5000','Kari','Karisen','Karisenveien 05','55555555','5000','50000','3000');

INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','1000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','2000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','1000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','2000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('3000','3000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('4000','2000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','2000',NULL,NULL);
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','3000',NULL,NULL);
