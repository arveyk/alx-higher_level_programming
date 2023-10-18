-- Script to display all shows
SELECT tv_show.title, tv_shows_genres.genre_id
FROM hbtn_0d_tvshows
ORDER BY tv_shows.title ASC tv_shows_genres.genre_id DESC;
