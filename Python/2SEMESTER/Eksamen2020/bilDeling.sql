drop schema if exists bilDeling;
create schema bilDeling;

use bilDeling;

create table bil
(
	regnr char(7),
    merke char(20),
    modell char(20),
    startdato date,
    posisjon char(30) default NULL,
    constraint bilPK primary key (regnr)
);

create table kunde
(
	mobilnr char(8),
    fornavn char(20),
    etternavn char(30),
    kortnr char(16),
    constraint kundePK primary key (mobilnr)
); 

create table utleie
(
	regnr char(7),
    utlevert timestamp,
    kmut int(10),
    mobilnr char(8),
    innlevert timestamp NULL default NULL,
    kminn int(10) default NULL,
    beløp decimal(8,2) default NULL,
    constraint utleiePK primary key (regnr,utlevert),
    constraint utleieBilFK foreign key (regnr) references bil(regnr),
    constraint utleieKundeFK foreign key (mobilnr) references kunde(mobilnr)
);

insert into bil values
('AA11111','Audi','A4',20110101,'Jevnaker'),
('BB22222','BMW','335i',20130101,'Tyristrand'),
('CC33333','Citroen','Berlingo',20150101,'Vik'),
('DD44444','Dacia','Delta',20170101,'Hønefoss'),
('EE55555','VW','Golf',20190101,'Sundvollen'),
('FF66666','Fiat','Abarth500',20200101,'Roa');

insert into kunde values
('11111111','Roman','Kollar','1000100010001000'),
('22222222','Maria','Cata','2000200020002000'),
('33333333','Robin','Tangen','3000300030003000'),
('44444444','Erik','Bøhle','4000400040004000'),
('55555555','Mira','Eske','5000500050005000'),
('66666666','Tomko','Bergli','6000600060006000');

insert into utleie(regnr,utlevert,kmut,mobilnr,innlevert,kminn,beløp)values
('AA11111','2022-01-01 11:00:00',12345,'11111111','2022-01-02 12:00:00',12350,270.00),
('BB22222','2022-02-02 12:00:00',246,'22222222','2022-02-04 12:00:00',300,900.00),
('CC33333','2022-03-03 12:00:00',1111,'33333333','2022-03-08 12:00:00',2000,1800.00),
('DD44444','2022-04-04 12:00:00',10000,'44444444',NULL,NULL,NULL),
('EE55555','2022-05-05 12:00:00',20000,'55555555',NULL,NULL,NULL),
('AA11111','2022-05-06 12:00:00',12350,'22222222',NULL,NULL,NULL),
('FF66666','2022-02-07 12:00:00',120,'33333333','2022-02-08 12:00:00',150,500.00);

drop user if exists 'Bilsjef';
create user 'Bilsjef' identified by 'eksamen2020';

grant select on bil to 'Bilsjef';
grant insert on bil to 'Bilsjef';
grant update on bil to 'Bilsjef';
grant delete on bil to 'Bilsjef';

grant select on kunde to 'Bilsjef';
grant insert on kunde to 'Bilsjef';
grant update on kunde to 'Bilsjef';
grant delete on kunde to 'Bilsjef';

grant select on utleie to 'Bilsjef';
grant insert on utleie to 'Bilsjef';
grant update on utleie to 'Bilsjef';
grant delete on utleie to 'Bilsjef';
