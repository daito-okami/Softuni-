SELECT	
	b.booking_id,
	b.starts_at::date,
	b.apartment_id,
	CONCAT(c.first_name, c.last_name) AS customer_name
FROM
	bookings AS b
RIGHT JOIN
	customers AS c
USING
	(customer_id)
ORDER BY 
	customer_name ASC
LIMIT 10;