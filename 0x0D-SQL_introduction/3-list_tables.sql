-- Script for listing all tables of a database in MySQL server
-- SET @var := CONCAT('SELECT * FROM information_schema.tables ');
-- SET @var := CONCAT('SELECT * FROM information_schema.TABLES');
-- PREPARE stmt FROM @var;
-- EXECUTE stmt;
-- DEALLOCATE PREPARE stmt;
SET @var := CONCAT('SHOW TABLES FROM mysql;');
PREPARE stmt FROM @var;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
