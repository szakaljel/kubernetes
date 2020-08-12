create table cities (
    id int primary key AUTO_INCREMENT,
    name varchar(50) not null unique,
    population int not null,
    time_zone varchar(50) not null
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;
