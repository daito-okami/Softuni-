CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
) RETURNS BOOLEAN
AS
$$
  BEGIN
      RETURN TRIM(upper(word), upper(set_of_letters)) = '';
  end;
    $$
language plpgsql
