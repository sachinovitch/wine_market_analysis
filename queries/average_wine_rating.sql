select avg(w.ratings_average) as avg, c.name
from wines w
join regions r 
on w.region_id = r.id
join countries c
on r.country_code = c.code
group by c.name
order by avg desc