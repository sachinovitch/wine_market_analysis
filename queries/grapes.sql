SELECT g.name AS grape_name, SUM(m.wines_count) AS sum
FROM most_used_grapes_per_country m
JOIN grapes g ON m.grape_id = g.id
GROUP BY g.name
ORDER BY sum DESC
LIMIT 3