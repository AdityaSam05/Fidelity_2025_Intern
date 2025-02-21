select 
    date_format(transaction_date,'%Y-%m') as month,
    sum(quantity*unit_price) as total
from
fil.sales_db
group by
date_format(transaction_date,'%Y-%m')