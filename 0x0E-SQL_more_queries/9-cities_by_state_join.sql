-- Script that lists all cities of calif
-- SELECT cities.id AS id, cities.name AS name, states.name AS name
-- FROM cities INNER JOIN states
-- WHERE states.name = 'California'
-- ORDER BY id ASC;
SELECT cities.id ,cities.name, states.name FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
