SELECT countries.name AS Country,
        ROUND(AVG((vintages.price_euros/vintages.bottle_volume_ml)*750), 2) AS Average_price_per_bottle
FROM vintages JOIN wines
ON vintages.wine_id = wines.id
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE vintages.ratings_average >= 4.2
GROUP BY countries.name
ORDER BY Average_price_per_bottle
LIMIT 3