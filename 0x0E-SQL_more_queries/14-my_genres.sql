-- Script to list all Dexter genres
SELECT name FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title='DEXTER'
ORDER BY name ASC;
