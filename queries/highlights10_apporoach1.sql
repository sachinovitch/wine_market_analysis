SELECT 
    name, ratings_average 
FROM vintages 
ORDER BY ratings_count DESC,
        ratings_average DESC
LIMIT 10