USE heltnydatabase;

DROP USER IF EXISTS 'Lagersjefen2022'@'localhost';

CREATE USER IF NOT EXISTS 'Lagersjefen2022'@'localhost' IDENTIFIED BY 'lagerpw';

GRANT SELECT ON Vare TO 'Lagersjefen2022'@'localhost';

GRANT INSERT ON Vare TO 'Lagersjefen2022'@'localhost';

GRANT UPDATE ON Vare TO 'Lagersjefen2022'@'localhost';

GRANT DELETE ON Vare TO 'Lagersjefen2022'@'localhost';

SELECT *
FROM Vare;