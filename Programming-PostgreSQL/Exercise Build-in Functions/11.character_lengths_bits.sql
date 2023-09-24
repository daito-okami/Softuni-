SELECT 
	CONCAT_WS(' ', m.mountain_range, p.peak_name) AS "Mountain Information",
	CHAR_LENGTH(CONCAT_WS(' ', m.mountain_range, p.peak_name)) AS "Character Length",
	BIT_LENGTH(CONCAT_WS(' ', m.mountain_range, p.peak_name)) AS "Bit of a String"
FROM
	mountains AS m,
	peaks AS p 
WHERE
	m."id" = p.mountain_id;