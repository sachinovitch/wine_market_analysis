SELECT 
    name
FROM vintages 
WHERE  ratings_average > 4.6
    AND
    price_euros < 200
ORDER BY ratings_count DESC
LIMIT 10