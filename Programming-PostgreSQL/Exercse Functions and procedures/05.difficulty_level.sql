CREATE OR REPLACE FUNCTION  fn_difficulty_level(
    level INT
) returns VARCHAR(50)
AS
$$
    DECLARE
        difficulty_level VARCHAR(50);
    BEGIN
        IF (level <=40) THEN
                difficulty_level := 'Normal Difficulty';
        ELSIF (level BETWEEN 41 AND 60) THEN
                difficulty_level := 'Nightmare Difficulty';
        ELSE
            difficulty_level := 'Hell Difficulty';
        end if;

        RETURN difficulty_level;
    end;
$$
language plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level)
FROM
    users_games
ORDER BY user_id ASC