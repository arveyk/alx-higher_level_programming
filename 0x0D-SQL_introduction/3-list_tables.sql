-- Script for listing all tables of a database in MySQL server
-- SET @var := CONCAT('SELECT * FROM information_schema.tables ');
-- SET @var := CONCAT('SHOW  TABLES FROM information_schema');
-- PREPARE stmt FROM @var;
-- EXECUTE stmt;
-- DEALLOCATE PREPARE stmt;
USE mysql;
show TABLES FROM mysql;
