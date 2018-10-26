/*Create database called project*/
CREATE DATABASE project CHARACTER SET UTF8;
USE project;

/* Database table for measurements */
CREATE TABLE measurement
(
id INTEGER AUTO_INCREMENT NOT NULL, 
controller_id varchar(32) NOT NULL,
measurement_time TIMESTAMP NOT NULL,
sensor_id varchar(32) NOT NULL,
temperature DOUBLE(5,2) NOT NULL,
humidity DOUBLE(5,2) NOT NULL,
pressure DOUBLE(7,2) NOT NULL,
PRIMARY KEY (id)

) COMMENT='Database table for measurements';

/* Create user for write endpoint with password 'password' and grant INSERT access to the create database and the table*/
CREATE USER 'writer'@'%'  IDENTIFIED BY 'password';
GRANT  INSERT ON project.measurement TO 'writer'@'%' ;

/* Create user for reader endpoint with password 'password' and grant SELECT access to the create database and the table*/
CREATE USER 'reader'@'%'  IDENTIFIED BY 'password';
GRANT  SELECT ON project.measurement TO 'reader'@'%' ;

FLUSH PRIVILEGES;