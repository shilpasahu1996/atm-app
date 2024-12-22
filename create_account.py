from atm import db_connection

conn = db_connection()

try:
def create_new_user():
        cur = conn.cursor()
        cur.execute('''
                INSERT INTO Accounts(
                Acc_No TEXT,Acc_Holder_First_Name,Acc_Holder_Last_Name,Acc_Balance,Mobile_no,Aadhaar
                )values ;
                ''')
        conn.commit()



