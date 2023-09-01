WITH popular_wines AS (
SELECT
	w.name
	,w.acidity
	,w.intensity
	,w.sweetness
	,w.tannin	
	,w.user_structure_count 
FROM
	wines w
WHERE
	w.user_structure_count > 5000
)
SELECT
	w.name, w.id
FROM wines w JOIN popular_wines pw
ON w.acidity < 1.05 * pw.acidity AND w.acidity > 0.95 * pw.acidity 
AND w.intensity < 1.05 * pw.intensity AND w.intensity > 0.95 * pw.intensity 
AND w.sweetness < 1.05 * pw.sweetness AND w.sweetness > 0.95 * pw.sweetness 
AND w.tannin < 1.05 * pw.tannin AND w.tannin > 0.95 * pw.tannin 
AND w.name <> pw.name
