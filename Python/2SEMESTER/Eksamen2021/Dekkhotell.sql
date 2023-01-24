DROP SCHEMA IF EXISTS Dekkhotell;
CREATE SCHEMA Dekkhotell;
USE Dekkhotell;

CREATE TABLE Kunde
(
Mobilnr CHAR(11),
Fornavn CHAR(20),
Etternavn CHAR(30),
Epost CHAR(40),
CONSTRAINT KundePK PRIMARY KEY (Mobilnr)
);

CREATE TABLE Dekksett
(
Mobilnr CHAR(11),
Regnr CHAR(7),
CONSTRAINT DekksettPK PRIMARY KEY(Mobilnr,Regnr),
CONSTRAINT DekksettKundeFK FOREIGN KEY (Mobilnr) REFERENCES Kunde(Mobilnr)
);


CREATE TABLE Oppbevaring
(
Mobilnr CHAR(11),
Regnr CHAR(7),
Innlevert TIMESTAMP,
Utlevert TIMESTAMP,
Hylle CHAR(4),
Pris DECIMAL(8,2),
CONSTRAINT OppbevaringPK PRIMARY KEY (Mobilnr,Regnr,Innlevert),
CONSTRAINT OppbevaringDekksettFK FOREIGN KEY (Mobilnr,Regnr) REFERENCES Dekksett(Mobilnr,Regnr)
);

INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn,Epost) VALUES
('11111111','Roman','Kollar','roman@kollar.no'),
('22222222','Robin','Tangen','robin@tangen.no'),
('33333333','Sander','Korneliussen','sander@korneliussen.no'),
('44444444','Sondre','Pedersen','sondre@pedersen.no');


INSERT INTO Dekksett(Mobilnr,Regnr) VALUES
('11111111','AA11111'),
('22222222','BB22222'),
('33333333','CC33333'),
('44444444','DD44444'),
('11111111','FF55555');


INSERT INTO Oppbevaring(Mobilnr,Regnr,Innlevert,Utlevert,Hylle,Pris) VALUES
('11111111','AA11111','2020-11-01 12:00:00','2021-04-01 12:00:00','A101',2500.00),
('11111111','AA11111','2021-04-01 12:00:00','2021-11-01 12:00:00','A101',3500.00),
('22222222','BB22222','2021-11-02 11:00:00','2022-04-02 11:00:00','A102',2500.00),
('22222222','BB22222','2022-04-02 11:00:00',NULL,'A102',NULL),
('33333333','CC33333','2020-01-01 10:00:00','2022-01-01 10:00:00','A103',5000.00),
('44444444','DD44444','2022-03-03 12:00:00',NULL,'A102',NULL),
('11111111','FF55555','2022-04-04 11:00:00',NULL,'A105',NULL);

DROP USER IF EXISTS Dekksjef;
CREATE USER Dekksjef IDENTIFIED BY 'Eksamen2021';

GRANT SELECT ON Kunde TO Dekksjef;
GRANT INSERT ON Kunde TO Dekksjef;
GRANT UPDATE ON Kunde TO Dekksjef;
GRANT DELETE ON Kunde TO Dekksjef;

GRANT SELECT ON Dekksett TO Dekksjef;
GRANT INSERT ON Dekksett TO Dekksjef;
GRANT UPDATE ON Dekksett TO Dekksjef;
GRANT DELETE ON Dekksett TO Dekksjef;

GRANT SELECT ON Oppbevaring TO Dekksjef;
GRANT INSERT ON Oppbevaring TO Dekksjef;
GRANT UPDATE ON Oppbevaring TO Dekksjef;
GRANT DELETE ON Oppbevaring TO Dekksjef;

