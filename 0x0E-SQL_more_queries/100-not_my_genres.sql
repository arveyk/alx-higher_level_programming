-- Script to list all Dexter genres
SELECT name FROM tv_genres
EXCEPT SELECT DISTINCT name FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
LEFT JOIN tv_shows on tv_shows.id=tv_show_genres.show_id 
WHERE title='Dexter'
ORDER BY name;
