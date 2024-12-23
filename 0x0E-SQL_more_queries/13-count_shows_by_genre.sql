-- Script that counts
SELECT tv_genres.name genre, count(*) AS number_of_shows FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
