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

# Delete table
#cur.execute('DROP TABLE students_data;')

#conn.commit()

# Create a new table
'''cur.execute("""CREATE TABLE students_data (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")

conn.commit()
'''
import csv

filename = 'phone_data.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, id, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phone_data (name, id, phone_number) VALUES 
                    ('{name}', '{id}', '{phone_number}');
        """)

        conn.commit()