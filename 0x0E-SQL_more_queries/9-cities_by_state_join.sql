-- Script that lists all cities of calif
SELECT cities.id, cities.name, states.name
FROM cities JOIN states
WHERE states.name = 'California'
ORDER BY cities.id ASC;
