-- Script for listing all tables of a database in MySQL server
-- SET @var := CONCAT('SELECT * FROM information_schema.tables ');
SET @var := CONCAT('SELECT *  FROM information_schema.tables ');
PREPARE stmt FROM @var;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
