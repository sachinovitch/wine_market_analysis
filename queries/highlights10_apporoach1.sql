SELECT 
    name, ratings_average 
FROM vintages 
ORDER BY ratings_average DESC, 
        ratings_count DESC 
LIMIT 10