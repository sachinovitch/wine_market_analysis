SELECT countries.name,
        AVG(vintages.price_euros/vintages.bottle_volume_ml) AS avg
FROM vintages JOIN wines
ON vintages.wine_id = wines.id
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE vintages.ratings_average >= 4.6
GROUP BY countries.name
ORDER BY avg
LIMIT 10