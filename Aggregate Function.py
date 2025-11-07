# import sqlite3
# ##count function= it counts the no of rows
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select count(id) from students where id=?',(1,))
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##Sum function= it gives sum of all rows
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select sum(marks) from students')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##Avg function= it gives average of numbers
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select avg(marks) from students')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##min function= it gives minimum no
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select min(marks) from students')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##Max function= it gives max no
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select max(marks) from students')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()



# import sqlite3
# ##upper function= it gives all names in uppercase
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select upper(name) from students')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##Lower function= it gives all names in lowercase
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select lower(name) from students')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()



########  ORDER BY CLAUSE #############
# import sqlite3
# ##ascending order
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select * from students order by id')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##descending order
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select * from students order by id desc')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##ascending order
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select * from students order by name')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##limit == it gives limit 
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select * from students order by id limit 3')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ## sort by multiple coloums
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select * from students order by id,marks')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()


##Group By##
# import sqlite3
# ##Group by = It groups common elements
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     cursor.execute('select id,max(marks) from students group by id')
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:
#         conn.close()

# import sqlite3
# ##Group by = It groups common elements
# try:
#     conn=sqlite3.connect("students.db")
#     cursor=conn.cursor()
#     # cursor.execute('alter table students add column city text')
#     # conn.commit()
    
#     cursor.execute('''insert into students
#             values(?,?,?,?,?)''',(12,'fgkjh',21,90,'Pune'))
#     conn.commit()
#     cursor.execute('select name from students group by city order by name desc')
#     conn.commit()
#     rows=cursor.fetchall()
#     print("Students Records:")
#     for row in rows:
#         print(row)

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:",e)

# finally:
#     if conn:  
#         conn.close()


##Primary Increment##
import sqlite3
try:
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()
    cursor.execute('''
    create table if not exists students1 (
            id integer primary key autoincrement,
            name text not null,
            age integer,
            marks real
    )
    ''')
    cursor.execute('''insert into students1
                values(?,?,?,?)''',(1,'Diksha',21,90))
    conn.commit()

except sqlite3.Error as e:
    print("An error occurred while fetching data:",e)

finally:
    if conn:  
        conn.close()