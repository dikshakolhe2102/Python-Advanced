import sqlite3
try:
    conn=sqlite3.connect("PrimeryKey.db")
    cursor=conn.cursor()
    # cursor.execute('''
    # create table if not exists Focus (
    #         id integer primary key autoincrement,
    #         name text not null
    #     )''')
    # print("Table created successfully.")
    # conn.commit()

    cursor.execute('''
    insert into Focus (name)
    values (?)''',('ABC',))
    conn.commit()
except sqlite3.Error as e:
    print("An error occured:",e)

finally:
    if conn:
        cursor.close()
        conn.close()

