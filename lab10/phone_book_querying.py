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

cur.execute('SELECT name, id, phone_number FROM phone_data')

print(cur.fetchall())
print(cur.fetchall())

cur.execute('SELECT name, id, phone_number FROM phone_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())