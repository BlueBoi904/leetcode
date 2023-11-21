select count(DISTINCT customer_id) as rich_count
from Store
where amount >500