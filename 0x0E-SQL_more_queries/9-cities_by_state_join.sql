-- Script that lists all cities of calif
SELECT cities.id, cities.name, states.name
FROM states JOIN cities
WHERE states.name = 'California'
ORDER BY cities.id ASC;
