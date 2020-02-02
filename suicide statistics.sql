/
select age,
Suicides_no
sum(suicides_no)  OVER(PARTITION BY age) as total_suicides_no
from who_suicide_statistics
/
select country,
sum(suicides_no) over (partition by country) as suicides_by_country
from who_suicide_statistics
/
select year,
sum(suicides_no)  OVER(PARTITION BY year) as suicides_by_yr_global
from who_suicide_statistics
/
select year,
sum(suicides_no)  OVER(PARTITION BY year) as suicides_by_yr_us
from who_suicide_statistics
where country = 'United States of America'
/
