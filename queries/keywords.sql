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

--WITH wines_with_flavour AS (
--	SELECT kw.wine_id
--	FROM keywords k JOIN  keywords_wine kw ON kw.keyword_id = k.id
--	WHERE k.name IN ('coffee','citrus','cream','green apple','toast')
--)
--
--SELECT w.name, COUNT(w.id) as cnt
--FROM wines w JOIN wines_with_flavour wf ON wf.wine_id = w.id
--GROUP BY w.name
--HAVING COUNT(w.id) = 5
--SELECT
--	w.name
--	, kw.group_name
--FROM
--	keywords k
--JOIN
--	keywords_wine kw ON k.id = kw.keyword_id
--JOIN
--	wines w ON w.id = kw.wine_id
--WHERE
--	k.name IN ('coffee','citrus','cream','green apple','toast')

