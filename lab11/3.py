import psycopg2

def delete_user_data(deleter):
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
        
        # Call the stored procedure
        sql_query = "CALL delete_user_data(%s);"
        cursor.execute(sql_query, (deleter,))
        
        # Commit the transaction
        connection.commit()
        print("User data deleted successfully.")
        
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        
    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

# Example usage:
delete_user_data("Nikita")  # Or provide a phone number instead
