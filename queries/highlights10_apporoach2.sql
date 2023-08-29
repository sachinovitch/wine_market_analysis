SELECT 
    DISTINCT vtr.vintage_id, vintages.name, vintages.ratings_average, vintages.price_euros
FROM vintages 
JOIN vintage_toplists_rankings vtr
    ON vintages.id = vtr.vintage_id 
ORDER BY vtr.rank, vintages.ratings_average DESC 
LIMIT 10