-- Script to show genres with their ratings
SELECT name, SUM(rate) ratings FROM tv_show_ratings
INNER JOIN tv_genres ON tv_genres.id=tv_show_ratings.show_id
GROUP BY name
ORDER BY ratings DESC;
