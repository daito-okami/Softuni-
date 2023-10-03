SELECT
	CONCAT(a.address, ' ', a.address_2) AS " apartment_adress",
	b.booked_for AS "nights"
FROM 
	apartments AS a
JOIN 
	bookings AS b
USING 
	(booking_id)
ORDER BY
	a.apartment_id