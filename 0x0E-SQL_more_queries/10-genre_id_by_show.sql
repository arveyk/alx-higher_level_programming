-- Script to display all shows
SELECT title, tv_show_genres.genre_id AS genre_id
FROM tv_shows CROSS JOIN tv_show_genres
ORDER BY title, genre_id ASC;
