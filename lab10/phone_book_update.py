import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phonebook', 
    user='postgres', 
    password='318520'
    )

# Create a cursor to work with the database
cur = conn.cursor()


conn.commit()

# Create a new table
'''cur.execute("""CREATE TABLE phone_data (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")'''

conn.commit()

# Create new students
'''cur.execute("""INSERT INTO phone_data (name, id, phone_number) VALUES 
            ('Alikhan', '1', '+77774469882'),
            ('Nurbolat', '2','+77714418420');
""")

conn.commit() '''

cur.execute("""UPDATE phone_data
            SET phone_number = '+77778884411'
            WHERE id = '2';
""")

conn.commit()