-- Script that lists all cities of calif
SELECT cities.id AS id, name
FROM cities
WHERE 
	id = (SELECT state_id FROM states
		WHERE states.name = 'California')
ORDER BY id ASC;
