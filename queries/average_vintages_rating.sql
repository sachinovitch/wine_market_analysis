select avg(v.ratings_average) as avg, c.name
from vintages v
join vintage_toplists_rankings vtr
on v.id = vtr.vintage_id
join toplists t
on vtr.top_list_id= t.id
join countries c
on t.country_code = c.code
group by c.name
order by avg desc