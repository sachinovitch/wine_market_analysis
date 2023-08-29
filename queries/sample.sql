SELECT
	w.name
	, kw.group_name
	, k.name
FROM
	keywords_wine kw 
JOIN
	keywords k ON k.id = kw.keyword_id
JOIN
	wines w ON w.id = kw.wine_id
WHERE
	kw.count > 10
AND
	kw.keyword_type = 'primary'
AND
	k.name IN ('coffee','citrus','cream','green apple','toast')
ORDER BY w.name
