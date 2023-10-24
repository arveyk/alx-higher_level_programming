-- Script to count duplicate entries
SELECT score, COUNT(*) AS "number" FROM second_table
GROUP BY score 
ORDER BY score DESC;
