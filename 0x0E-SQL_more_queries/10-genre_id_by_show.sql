-- Script to display all shows
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id AS genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NOT NULL
ORDER BY title, genre_id ASC;
