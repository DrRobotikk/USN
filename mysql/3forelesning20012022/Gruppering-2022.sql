DROP SCHEMA IF EXISTS gruppering2022;
CREATE SCHEMA gruppering2022;

USE gruppering2022;

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(15) NOT NULL,
Stillingskode CHAR(4),
Lønnstrinn CHAR(2),
Avdelingsnr CHAR(4),
CONSTRAINT AnsattPK PRIMARY KEY (Ansattnr)
);

INSERT INTO Ansatt VALUES ('1','Brit','1008','66','3');
-- resten fyller du ut
-- flere ansatte på samme/forskjellige lønnstrinn på samme/forskjellige stillingskoder på samme/forskjellige avdelinger
