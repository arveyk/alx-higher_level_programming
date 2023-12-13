-- Script that lists all cities of calif
SELECT id, name
FROM cities
WHERE 
	id IN (SELECT state_id FROM states
		WHERE states.name = 'California')
ORDER BY id ASC;
