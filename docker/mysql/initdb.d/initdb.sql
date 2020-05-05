DROP SCHEMA IF EXISTS event;
CREATE SCHEMA event;
USE event;

DROP TABLE IF EXISTS users;
CREATE TABLE users
(
  user_id INT(100) AUTO_INCREMENT,
  user_name VARCHAR(20) NOT NULL,
  password VARCHAR(80),
  PRIMARY KEY (user_id)
) ENGINE = InnoDB;

DROP TABLE IF EXISTS event_overview;
CREATE TABLE event_overview
(
  event_id INT(20) AUTO_INCREMENT,
  event_name VARCHAR(20) UNIQUE NOT NULL,
  event_details VARCHAR(40),
  date DATETIME NOT NULL,
  PRIMARY KEY (event_id)
) ENGINE = InnoDB;

DROP TABLE IF EXISTS event_attendees;
CREATE TABLE event_attendees
(
  event_id INT(20) AUTO_INCREMENT,
  event_name VARCHAR(20) UNIQUE NOT NULL,
  user_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (event_id)
) ENGINE = InnoDB;
