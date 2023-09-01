SELECT 
    name AS Name
FROM vintages 
WHERE  ratings_average > 4.4
    AND
    ratings_count > 500
    AND
    price_euros < 1000
ORDER BY ratings_count DESC
LIMIT 10