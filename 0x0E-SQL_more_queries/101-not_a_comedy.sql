-- Script to select shows that are not Comedy
SELECT title FROM tv_shows
EXCEPT
SELECT DISTINCT tv_shows.title
FROM tv_show_genres LEFT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id 
INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE name='Comedy'
ORDER BY title;" 
