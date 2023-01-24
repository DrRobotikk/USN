SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS `hobbyhusetkap2` ;
CREATE SCHEMA IF NOT EXISTS `hobbyhusetkap2` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;

USE `hobbyhusetkap2`;

--
-- Database: `Hobbyhuset`
--

-- --------------------------------------------------------

--
-- Sletter tabeller i korrekt rekkefølge
--


DROP TABLE IF EXISTS `Vare`;


--
-- Tabellstruktur for tabell `Vare`
--

CREATE TABLE IF NOT EXISTS `Vare` (
  `VNr` char(5) NOT NULL DEFAULT '',
  `Betegnelse` char(30) NOT NULL,
  `Pris` decimal(8,2) NOT NULL DEFAULT '0.00',
  `Kategori`char(30) NOT NULL,
  `Antall` int(11) NOT NULL,
  `Hylle` char(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dataark for tabell `Vare`
--

INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('90693', 'Marsipantang', '57.00', 'Konfekt og marsipan', 0, 'B17');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('44939', 'Hobbymaling, 6 farger', '115.00', 'Hobbymaling', 2, 'B02');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('10830', 'Nisseskjegg, 30 cm', '57.50', 'Dukker og nisser', 42, NULL);
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('33044', 'Blandet blomsterfrø', '14.50', 'Blomsterfrø', 1080, 'E05');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('15217', 'Kram tørrfluekorker, 5stk', '32.00', 'Fiske', 213, 'B42');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('90164', 'Lakrisekstrakt, 100g', '75.50', 'Konfekt og marsipan', 104, 'B06');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('15207', 'Antron garn, hvit', '24.50', 'Fiske', 21, 'B41');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('13001', 'Glasskuler, 100 gr', '38.00', 'Dukker og nisser', 0, 'E11');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('21032', 'Furuspon, 3 cm', '57.50', 'Dekorasjoner', 240, 'B32');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('33045', 'Blomkarse', '17.50', 'Blomsterfrø', 1206, 'E05');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('55130', 'Moro med marsipan', '298.50', 'Bøker', 140, 'C20');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('15211', 'Tubeflue verktøy', '209.00', 'Fiske', 39, 'B42');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('42615', 'Gipsform marihøner', '106.00', 'Keramikk', 124, 'B03');
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('64551', 'Hengebegonia, 10 stk.', '118.00', 'Blomsterløker', 206, NULL);
INSERT INTO `Vare` (`VNr`, `Betegnelse`, `Pris`, `Kategori`, `Antall`, `Hylle`) VALUES('65247', 'Liten plantespade', '75.00', 'Hageutstyr', 76, 'A25');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




