DROP SCHEMA IF EXISTS oblig2022;

CREATE SCHEMA oblig2022;

USE oblig2022;

CREATE TABLE Student
(
Studentnr CHAR(6),
Fornavn CHAR(30),
Etternavn CHAR(20),
Epost CHAR(40),
Telefon CHAR(8),
CONSTRAINT StudentPK PRIMARY KEY (Studentnr)
);

CREATE TABLE Emne
(
Emnekode CHAR(8),
Emnenavn CHAR(40),
Studiepoeng DECIMAL(3,1),
CONSTRAINT EmnePK PRIMARY KEY (Emnekode)
);

CREATE TABLE Rom
(
Romnr CHAR(4),
AntallPlasser INTEGER(3),
CONSTRAINT RomPK PRIMARY KEY (Romnr)
);

CREATE TABLE Eksamen
(
Emnekode CHAR(8),
Dato DATE,
Romnr CHAR(4),
CONSTRAINT EksamenPK PRIMARY KEY (Dato,Emnekode),
CONSTRAINT EmneEksamenFK FOREIGN KEY (Emnekode) REFERENCES Emne(Emnekode),
CONSTRAINT RomEksamenFK FOREIGN KEY (Romnr) REFERENCES Rom(Romnr)
);

CREATE TABLE Eksamensresultat
(
Studentnr CHAR(6),
Emnekode CHAR(8),
Dato DATE,
Karakter CHAR(1),
CONSTRAINT EksamensresultatPK PRIMARY KEY (Studentnr,Emnekode,Dato),
-- FIKS SAMMENSATTE FK'er
CONSTRAINT StudentEksamensresultatFK FOREIGN KEY (Studentnr) REFERENCES Student(Studentnr),
CONSTRAINT EmneEksamensresultatDatoFK FOREIGN KEY (Dato,Emnekode) REFERENCES Eksamen(Dato,Emnekode)
);

INSERT INTO Student (Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES
('1001','Roman','Kollar','roman@kollar','11111111'),
('1002','Robin','Tangen','robin@tangen','22222222'),
('1003','Erik','Bøhle','erik@bøhle','33333333'),
('1004','Vegard','Sveinsvoll','vegard@sveindsvoll','44444444'),
('1005','Haider','Ahmed','haider@ahmed','55555555'),
('1006','Didrik','Sawkins','didrik@sawkins','66666666'),
('1007','Sander','Korneliussen','sander@korneliussen','77777777'),
('1008','Even','Nyhus','even@nyhus','88888888'),
('1010','Sondre','Pedersen','sondre@pedersen','99999999'),
('1009','Mats','Hauk','mats@hauk','10101010');

INSERT INTO Emne (Emnekode, Emnenavn, Studiepoeng) VALUES
('INF1000','Informasjonssystemer',7.5),
('SYS1000','Systemutvikling',7.5),
('PRG1000','Grunnleggende programering 1',7.5),
('WEB1100','Webutvikling og HCI',15),
('DAT1000','Databasesystemer',7.5),
('ORL1000','Organisering og ledelse',7.5),
('PRG2000','Grunnleggende programering 2',7.5),
('PRO1000','Praktisk prosjektutvikling',7.5),
('INF2000','InfoTEST',7.5),
('SYS2000','SystemTEST',7.5);

INSERT INTO Rom (Romnr,Antallplasser) VALUES
('B101',50),
('B103',75),
('B105',90),
('E111',110),
('E121',220),
('E201',80),
('E206',123),
('E209',155),
('E211',55),
('E215',101);

INSERT INTO Eksamen (Emnekode,Dato,Romnr) VALUES
('INF1000',20211005,'E209'),
('INF1000',20221005,'E209'),
('INF2000',20211005,'B101'),
('SYS1000',20211125,'E111'),
('PRG1000',20211210,'E209'),
('WEB1100',20211221,'B103'),
('DAT1000',20220425,'E215'),
('ORL1000',20220505,'E121'),
('PRG2000',20220525,'E215'),
('PRO1000',20220608,'B101'),
('PRO1000',20220610,'B101');

INSERT INTO Eksamensresultat (Studentnr,Emnekode,Dato,Karakter) VALUES
('1001','PRG1000',20211210,'A'),
('1001','WEB1100',20211221,'D'),
('1001','INF1000',20211005,'C'),
('1001','INF1000',20221005,'A'),
('1001','SYS1000',20211125,'A'),
('1001','PRO1000',20220608,'F'),
('1001','PRO1000',20220610,'C'),
('1001','PRG2000',20220525,'D'),
('1002','PRG1000',20211210,'A'),
('1002','WEB1100',20211221,NULL),
('1002','INF1000',20211005,'D'),
('1002','INF1000',20221005,'B'),
('1002','SYS1000',20211125,'A'),
('1003','PRG1000',20211210,'D'),
('1003','INF1000',20211005,'B'),
('1003','SYS1000',20211125,'A'),
('1004','PRG1000',20211210,'D'),
('1004','WEB1100',20211221,NULL),
('1004','SYS1000',20211125,'A'),
('1004','INF1000',20211005,'D'),
('1005','PRG1000',20211210,'E'),
('1005','ORL1000',20220505,'C'),
('1006','PRG1000',20211210,'B'),
('1006','INF1000',20211005,'D'),
('1006','WEB1100',20211221,NULL),
('1007','ORL1000',20220505,'B'),
('1007','PRG2000',20220525,'A'),
('1007','PRG1000',20211210,'C'),
('1008','PRG1000',20211210,'A'),
('1008','WEB1100',20211221,NULL),
('1008','INF1000',20211005,'D'),
('1008','SYS1000',20211125,'C'),
('1009','PRG1000',20211210,'C'),
('1009','WEB1100',20211221,'D'),
('1009','INF1000',20211005,'B'),
('1009','SYS1000',20211125,'A'),
('1010','PRG1000',20211210,'F'),
('1010','INF1000',20211005,'C'),
('1010','SYS1000',20211125,'D'),
('1010','WEB1100',20211221,NULL);

DROP USER IF EXISTS 'Eksamenssjef';

CREATE USER IF NOT EXISTS 'Eksamenssjef' IDENTIFIED BY 'oblig2022';

GRANT SELECT ON Student TO 'Eksamenssjef';
GRANT INSERT ON Student TO 'Eksamenssjef';
GRANT UPDATE ON Student TO 'Eksamenssjef';
GRANT DELETE ON Student TO 'Eksamenssjef';

GRANT SELECT ON Emne TO 'Eksamenssjef';
GRANT INSERT ON Emne TO 'Eksamenssjef';
GRANT UPDATE ON Emne TO 'Eksamenssjef';
GRANT DELETE ON Emne TO 'Eksamenssjef';

GRANT SELECT ON Rom TO 'Eksamenssjef';
GRANT INSERT ON Rom TO 'Eksamenssjef';
GRANT UPDATE ON Rom TO 'Eksamenssjef';
GRANT DELETE ON Rom TO 'Eksamenssjef';

GRANT SELECT ON Eksamen TO 'Eksamenssjef';
GRANT INSERT ON Eksamen TO 'Eksamenssjef';
GRANT UPDATE ON Eksamen TO 'Eksamenssjef';
GRANT DELETE ON Eksamen TO 'Eksamenssjef';

GRANT SELECT ON Eksamensresultat TO 'Eksamenssjef';
GRANT INSERT ON Eksamensresultat TO 'Eksamenssjef';
GRANT UPDATE ON Eksamensresultat TO 'Eksamenssjef';
GRANT DELETE ON Eksamensresultat TO 'Eksamenssjef';


select max(Studentnr)
from Student;