-- Script that lists all cities of calif
SELECT cities.id, name
FROM cities
WHERE 
	cities.state_id = (SELECT id FROM states
		WHERE states.name = 'California')
ORDER BY id ASC;
