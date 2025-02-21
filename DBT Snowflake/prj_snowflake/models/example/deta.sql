WITH CustomerInfo AS (
    SELECT customerNumber AS c_id,customerName 
    FROM fil_db.fil_schema.customers
),
OrderInfo AS (
    SELECT orderNumber AS o_id,customerNumber,status 
    FROM fil_db.fil_schema.orders
),
ProductInfo AS (
    SELECT productCode,productName 
    FROM fil_db.fil_schema.products
),
Order_Detail AS (
    SELECT orderNumber,productCode 
    FROM fil_db.fil_schema.orderdetails
)
SELECT ci.c_id,ci.customerName,oi.o_id,pi.productName

FROM CustomerInfo ci
JOIN OrderInfo oi ON ci.c_id=oi.customerNumber
JOIN Order_Detail od ON oi.o_id=od.orderNumber
JOIN ProductInfo pi ON od.productCode=pi.productCode
WHERE oi.status='Pending'
