CREATE OR REPLACE PROCEDURE delete_user_data(IN p_deleter VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phone_data WHERE name = p_deleter OR phone_number = p_deleter;
END;
$$;
