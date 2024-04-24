import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='suppliers', 
    user='postgres', 
    password='318520'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# Querying the database
cur.execute('SELECT Version()')

db_ver = cur.fetchall()

print(db_ver)