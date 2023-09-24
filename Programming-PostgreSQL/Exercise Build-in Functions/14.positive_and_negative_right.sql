SELECT
	peak_name,
	RIGHT(peak_name, 4) AS "Positive Left",
	RIGHT(peak_name, -4) AS "Negative Left"
FROM
	peaks;