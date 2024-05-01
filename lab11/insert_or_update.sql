CREATE OR REPLACE PROCEDURE insert_or_update_user(IN p_name VARCHAR,IN p_id VARCHAR,IN p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phone_data WHERE name = p_name) THEN
        UPDATE phone_data SET phone_number = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phone_data (name,id, phone_number) VALUES (p_name,p_id, p_phone);
    END IF;
END;
$$;
