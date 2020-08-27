
DROP TABLE IF EXISTS `users`;

CREATE TABLE IF NOT EXISTS `users` (
  `UID` INTEGER  PRIMARY KEY AUTOINCREMENT,
  `username`  TEXT      NOT NULL,
  `password`  TEXT      NOT NULL,
  `email`     TEXT      NOT NULL,
  `privilege` TEXT      NOT NULL

);

INSERT INTO `users` (`UID`, `username`, `password`, `email`, `privilege`) VALUES
(1, 'admin', 'admin', 'admin@admin.com', 'admin');


INSERT INTO `users` (`UID`, `username`, `password`, `email`, `privilege`) VALUES
(2, 'employee', 'employee', 'employee@employee.com', 'employee');


DROP TABLE IF EXISTS `movies`;

CREATE TABLE IF NOT EXISTS `movies` (
  `movie_ID` INTEGER  PRIMARY KEY AUTOINCREMENT,
  `title`  TEXT      NOT NULL,
  `overview`  TEXT      NOT NULL,
  `adult`     TEXT      NOT NULL,
  `status`     TEXT      NOT NULL,
  `release_date`     TEXT      NOT NULL,
  `imdb_id`     TEXT      NOT NULL,
  `tmdb_id`     TEXT      UNIQUE NOT NULL,
  `backdrop`     BLOB      NOT NULL,
  `poster`     BLOB      NOT NULL,
  `tagline` TEXT      NOT NULL

);



DROP TABLE IF EXISTS `auditorium`;

CREATE TABLE IF NOT EXISTS `auditorium` (
  `auditorium_ID` INTEGER  PRIMARY KEY AUTOINCREMENT,
  `total_seats`  INTEGER      NOT NULL,
  `regular_seats`  INTEGER      NOT NULL,
  `regular_price`  INTEGER      NOT NULL,
  `preminum_seats`     INTEGER      NOT NULL,
  `preminum_price`     INTEGER      NOT NULL,
  `gold_seats`     INTEGER     NOT NULL,
  `gold_price`     INTEGER     NOT NULL,
  `layout`     BLOB      NOT NULL

);

DROP TABLE IF EXISTS `projections`;

CREATE TABLE IF NOT EXISTS `projections` (
  `projection_ID` INTEGER  PRIMARY KEY AUTOINCREMENT,
  `movie_ID`  INTEGER      NOT NULL,
  `auditorium_ID`  INTEGER      NOT NULL,
  `startTime`    DATETIME     NOT NULL,
  `endTime`     DATETIME      NOT NULL,
  `available_seats`     INTEGER      NOT NULL,
  `total_seats`     INTEGER      NOT NULL,
  FOREIGN KEY (movie_ID) REFERENCES movies (movie_ID),
  FOREIGN KEY (auditorium_ID) REFERENCES auditorium (auditorium_ID)
);









