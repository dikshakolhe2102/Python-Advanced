import sqlite3
# try:
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     update students
#     set marks = ?
#     where name = ?
#     ''',(82.0,"Diksha"))
#     conn.commit()

#     if cursor.rowcount == 0:
#         print("Diksha not found. No update performed.")
#     else:
#         print(" grade updated.")
#         # Fetch and print updated record
#         cursor.execute('select * from students where name = ?', ('Diksha',))
#         updated_row = cursor.fetchone()
#         print("Updated row:", updated_row)

# except sqlite3.Error as e:
#     print("An error occurred:", e)

# finally:
#     if conn:
#         conn.close()


#write a program to accept userid and newpass from user and change old pass to newpass 
id=int(input("Enter id"))
passw=input("Enter password")
try:
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute('''
    update user
    set userpass = ?
    where userid = ?
    ''',(passw,id))
    conn.commit()

    if cursor.rowcount == 0:
        print("userid not found. No update performed.")
    else:
        print(" grade updated.")
        # Fetch and print updated record
        cursor.execute('select * from user where userid = ?', (id,))
        updated_row = cursor.fetchone()
        print("Updated row:", updated_row)

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()
