import psycopg2

# Function to get all contacts
def get_all_contacts():
    conn = psycopg2.connect("dbname=phonebook user=postgres password=318520")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phone_data")
    rows = cur.fetchall()
    
    conn.close()
    
    return rows

# Function to search contacts by first name
def search_by_first_name(name):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=318520")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phone_data WHERE name = %s", (name,))
    rows = cur.fetchall()
    
    conn.close()
    
    return rows

# Function to search contacts by phone number
def search_by_phone(phone_number):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=318520")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phone_data WHERE phone_number = %s", (phone_number,))
    rows = cur.fetchall()
    
    conn.close()
    
    return rows

# Function to delete contact by username
'''def delete_contact_by_username(name):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=318520")
    cur = conn.cursor()
    
    cur.execute("DELETE FROM phone_data WHERE name = %s", (name,))
    
    conn.commit()
    conn.close()'''

if __name__ == "__main__":
    # Example usage
    contacts = get_all_contacts()
    print("All Contacts:")
    for contact in contacts:
        print(contact)

    alikhan = search_by_first_name("Alikhan")
    print("\nContacts with first name 'Alikhan':")
    for contact in alikhan:
        print(contact)

    number = "+77476582147 "
    contact_by_phone = search_by_phone(number)
    print(f"\nContact with phone number {number}:")
    print(contact_by_phone)

    '''# Deleting a contact by username
    delete_contact_by_username("John")
    print("\nDeleted contact with first name 'John'")
    
    # Get all contacts again after deletion
    remaining_contacts = get_all_contacts()
    print("\nRemaining Contacts:")
    for contact in remaining_contacts:
        print(contact)'''