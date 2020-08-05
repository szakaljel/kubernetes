CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `test` (id, name) VALUES (1,'test1'),(2,'test2'),(3,'test3'),(4,'test4'),(5,'test5')
    ON DUPLICATE KEY UPDATE id=id, name=name;