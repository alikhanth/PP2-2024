import psycopg2
from config import load_config

def get_vendors_fetchall():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, id, phone_number FROM phone_data ORDER BY id")
                rows = cur.fetchall()

                print(rows) 

                print("The number of parts: ", cur.rowcount)
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 

if __name__ == '__main__':
    print("--------------")
    get_vendors_fetchall()
    print("--------------")