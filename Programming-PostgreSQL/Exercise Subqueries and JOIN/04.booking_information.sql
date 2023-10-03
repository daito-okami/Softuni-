SELECT	
	b.booking_id,
	a.name AS apartment_owner,
	a.apartment_id,
	CONCAT(c.first_name, ' ', c.last_name) as customer_name
FROM
	apartments as a
FULL JOIN
	bookings as b
USING 
	(booking_id)
FULL JOIN customers as c
USING 
	(customer_id)
ORDER BY
	booking_id ASC,
	apartment_owner ASC,
	customer_name asc