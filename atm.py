import sqlite3

try:
    #connect new database
    def db_connection():
        conn = sqlite3.connect("atm.db")
        print("Database connection established.")
        return conn
except sqlite3.Error as con_error:
    print(f"DB Connection Error: {con_error} ")

finally:
    pass

try:
    conn = db_connection()
    #create a table
    conn.execute(
                '''CREATE TABLE IF NOT EXISTS Accounts(
                Acc_No TEXT NOT NULL,
                Acc_Holder_First_Name TEXT,
                Acc_Holder_Last_Name TEXT,
                Acc_Balance REAL,
                Mobile_no TEXT,
                Aadhaar TEXT    
        );
        ''')

    conn.commit()
    print('Table created')
except Exception as e:
    print(f'Table createion failed {e}')
finally:
    db_connection().close()




