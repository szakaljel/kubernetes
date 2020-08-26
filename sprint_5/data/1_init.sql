create table cities (
    id int primary key AUTO_INCREMENT,
    name varchar(50) not null unique,
    population int not null,
    time_zone varchar(50) not null
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

insert into cities (id, name, population, time_zone) values
(1, 'Gdańsk', 470900, 'Europe/Warsaw'),
(2, 'Paryż', 2243833, 'Europe/Paris'),
(3, 'Lisbona', 547631, 'Europe/Lisbon');