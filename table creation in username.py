def sanitize_email(email):
    # Replace characters that are not allowed in SQLite table names
    return email.replace('@', '_at_').replace('.', '_dot_')

def create_user_table(email):
    sanitized_table_name = sanitize_email(email)
    conn = sqlite3.connect('groceria.db')
    cursor = conn.cursor()
    
    try:
        # Create a table specifically for the user to store order information
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {sanitized_table_name} (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print(f"Table {sanitized_table_name} created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        
        
        
#Function Calling
email = email_address_login.get()  # or use email_address.get() on signup
create_user_table(email)
