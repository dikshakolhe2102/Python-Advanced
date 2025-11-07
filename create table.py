import sqlite3 
try:
    conn=sqlite3.connect('students.db')
    cursor=conn.cursor()

    #create table
    cursor.execute('''
    create table if not exists students (
            id integer,
            name text,
            age integer,
            marks real
    )
    ''')
    print("Table created successfully.")

    #Save changes
    conn.commit()
except sqlite3.Error as e:
    print("An error occured:",e)

finally:
    if conn:
        cursor.close()
        conn.close()


#write a program to create user with cloum userid username password usermailid phone number
try:
    conne=sqlite3.connect('user.db')
    cursor=conne.cursor()

    #create table
    cursor.execute('''
    create table if not exists user (
            userid integer,
            username text,
            userpass text,
            usermailid text,
            userphone integer
    )
    ''')
    print("Table created successfully.")

    #Save changes
    conne.commit()
except sqlite3.Error as e:
    print("An error occured:",e)

finally:
    if conne:
        cursor.close()
        conne.close()