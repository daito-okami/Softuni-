SELECT
	magic_wand_creator,
	MIN(magic_wand_size) as "Minium Wand Size"
FROM 
	wizard_deposits
GROUP BY 
	magic_wand_creator
ORDER BY 
	"Minium Wand Size" ASC
LIMIT 5;