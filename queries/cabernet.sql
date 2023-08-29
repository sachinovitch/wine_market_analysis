SELECT
	v.name
	,v.ratings_average
	,v.price_euros * 750 / v.bottle_volume_ml price_per_750
	,bottle_volume_ml/750 as bottle_size
FROM
	vintages v
JOIN
	WINES w ON w.id = v.wine_id
JOIN
	keywords_wine kw ON kw.wine_id  = w.id
JOIN
	keywords k ON k.id = kw.keyword_id	
WHERE
	lower(v.name) LIKE '%cabernet sauvignon%'
AND
	k.name IN ('acacia', 'brioche') AND kw.keyword_type = 'primary'
AND
	v.ratings_count > 99 /*AND v.ratings_average > 4.5*/
ORDER BY v.ratings_average DESC
LIMIT 5
