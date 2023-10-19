-- Display all rows from tables
SET @var := CONCAT('SELECT * FROM first_table');
PREPARE stmt FROM @var;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
