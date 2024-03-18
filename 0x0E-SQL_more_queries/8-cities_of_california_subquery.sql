-- Script that lists all cities of calif
SELECT cities.id, name
FROM cities
WHERE 
	cities.id IN (SELECT state_id FROM states
		WHERE states.name = 'California')
ORDER BY id ASC;
