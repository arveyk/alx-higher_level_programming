-- Script that lists all cities of calif
SELECT cities.id, cities.name states.name 
FROM hbtn_0d_usa WHERE cities.name=California ORDER BY ASC;
