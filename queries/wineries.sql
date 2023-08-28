SELECT
	wr.name
	, COUNT(*)
FROM
	wines w
JOIN
	wineries wr ON w.winery_id = wr.id
GROUP BY
	wr.name
