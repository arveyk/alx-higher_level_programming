-- Script to list all Dexter genres
SELECT tv_genres.name FROM tv_show_genres
INNER JOIN tv_genres
ON tv_genres.id=tv_show_genres.genre_id
WHERE show_id=(SELECT id FROM tv_shows
	WHERE title='DEXTER');
