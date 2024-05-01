import psycopg2

def insert_or_update_user(name,id,phone_number):
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            dbname="phonebook",
            user="postgres",
            password="318520",
            host="localhost"
        )
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Call the stored procedure using a regular SQL query
        sql_query = "CALL public.insert_or_update_user(%s,%s, %s);"
        cursor.execute(sql_query, (name, id, phone_number))
        
        # Commit the transaction
        connection.commit()
        print("User inserted/updated successfully.")
        
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        
    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

# Example usage:
insert_or_update_user("Adam","3", "+7877475442")
