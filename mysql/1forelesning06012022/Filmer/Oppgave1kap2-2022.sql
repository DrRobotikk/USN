SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS `oppgave1kap2` ;
CREATE SCHEMA IF NOT EXISTS `oppgave1kap2` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;

USE `oppgave1kap2`;

--
-- Database: `Mediebedriften BlancaFlix`
--

--
-- Tabellstruktur for tabell `Film`
--

CREATE TABLE `Film` (
  `FNr` smallint PRIMARY KEY,
  `Tittel` char(25) NOT NULL,
  `År` smallint NOT NULL,
  `Land`char(25) NOT NULL,
  `Sjanger`char(15) NOT NULL,
  `Alder` smallint NOT NULL,
  `Tid` smallint NOT NULL,
  `Pris`decimal(6,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Data for tabell `Film`
--

INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(13, 'Beatles: Help', 1965,  'England', 'Musikk',11, 144, NULL);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(1, 'Casablanca', 1942, 'USA', 'Drama', 15, 102, 149.00);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(2, 'Fort Apache', 1948, 'USA', 'Western', 15, 127, NULL);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(12, 'Blues Brothers 2000', 1998, 'USA', 'Komedie', 11, 124, 135.00);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(7, 'Asterix hos britene', 1988, 'Frankrike', 'Tegnefilm', 7, 78, 149);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(6, 'Cinema Paradiso', 1988, 'Italia', 'Komedie', 11, 123, NULL);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(8, 'Veiviseren', 1987, 'Norge', 'Action', 15, 96, 87.00);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(5, 'High Noon', 1952, 'USA', 'Western', 15, 85, 123);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(9, 'Salmer fra kjøkkenet', 2002, 'Norge', 'Komedie', 7, 80, 149.00);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(4, 'Streets of Fire', 1984, 'USA', 'Action', 15, 93, NULL);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(10, 'Anastasia', 1997, 'USA', 'Tegnefilm', 7, 94, 123.00);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(3, 'Apocalypse Now', 1979, 'USA', 'Action', 18, 155, 123.00);
INSERT INTO `Film` (`FNr`, `Tittel`, `År`, `Land`, `Sjanger`, `Alder`, `Tid`, `Pris`) VALUES(11, 'La Grande bouffe', 1973, 'Frankrike', 'Drama', 15, 129, 87.00);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




