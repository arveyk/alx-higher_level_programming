-- Script to display shows by genre
SELECT tv_shows.title title, tv_genres.name name FROM tv_show_genres
RIGHT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
ORDER BY title ASC, name ASC;
