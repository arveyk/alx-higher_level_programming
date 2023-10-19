-- Script to show full desc of table
SET @var := CONCAT('desc first_table FROM hbtn_0c_0');
PREPARE stmt FROM @var;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
