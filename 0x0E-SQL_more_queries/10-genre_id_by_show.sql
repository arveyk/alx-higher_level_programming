-- Script to display all shows
SELECT title, id AS genre_id
FROM tv_shows
ORDER BY title, genre_id ASC;
