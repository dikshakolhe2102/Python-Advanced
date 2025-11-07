import sqlite3
try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        insert into student1 (id,name,age,marks)
        values (?, ?, ?, ?)
        ''',(1,"Diksha",18,80))
    conn.commit()
    
    print("Records are inserted successfully.")

except sqlite3.Error as e:
    print("An error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()
        conn.close()

# import sqlite3
# try:
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()


#     students=[
#         (1,'abc',20,85.5),
#         (2,'pqr',22,78.0),
#         (3,'asd',19,92.3)
#     ]
#     for student in students:
#         cursor.execute('''
#             insert into students (id,name,age,marks)
#             values (?, ?, ?, ?)
#             ''',student)
#         conn.commit()
    
#     print("Records are inserted successfully.")

# except sqlite3.Error as e:
#     print("An error occured while inserting data:",e)

# finally:
#     if conn:
#         cursor.close()
#         conn.close()


# try:
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()


#     students=[
#         (1,'abc',20,85.5),
#         (2,'pqr',22,78.0),
#         (3,'asd',19,92.3)
#     ]
    
#     # cursor.executemany('''
#     #     insert into students (id,name,age,marks)
#     #     values (?, ?, ?, ?)
#     #     ''',students)
#     print("No of rows in table",cursor.rowcount)
#     conn.commit()
    
#     print("Records are inserted successfully.")

# except sqlite3.Error as e:
#     print("An error occured while inserting data:",e)

# finally:
#     if conn:
#         cursor.close()
#         conn.close()



#write a program to insert data in user table and print all data from users table

# try:
#     conn = sqlite3.connect('user.db')
#     cursor = conn.cursor()


#     lis=[
#         (1,'abc','asd','sdfghj',1234567),
#         (2,'pqr','hgf','rtyhujhgf',783456)
#     ]
#     for i in lis:
#         cursor.execute('''
#             insert into user (userid,username,userpass,usermailid,userphone)
#             values (?, ?, ?, ?,?)
#             ''',i)
#         conn.commit()
    
#     print("Records are inserted successfully.")

#     #Execute the SELECT query
#     cursor.execute('select * from user')
#     rows = cursor.fetchall()

#     print("rowcount:",cursor.rowcount)
#     # Display the results
#     print("user Records:")
#     for row in rows:
#         print("***************")
#         print("ID",row[0])
#         print("Name",row[1])
#         print("Age:",row[2])
#         print("marks",row[3])
#         print("----------------")

# except sqlite3.Error as e:
#     print("An error occured while inserting data:",e)

# finally:
#     if conn:
#         cursor.close()
#         conn.close()


# try:
#     conn = sqlite3.connect('user.db')
#     cursor = conn.cursor()
#     lis=[
#         (1,'abc','asd','sdfghj',1234567),
#         (2,'pqr','hgf','rtyhujhgf',783456)
#     ]
#     for i in lis:
#         cursor.execute('''
#             insert into user (userid,username,userpass,usermailid,userphone)
#             values (?, ?, ?, ?,?)
#             ''',i)
#         conn.commit()
    
#     print("Records are inserted successfully.")

#     #Execute the SELECT query
#     cursor.execute('select *from user where userid = 1')

#     rows = cursor.fetchall()

#     print("rowcount:",cursor.rowcount)
#     # Display the results
#     print("user Records:")
#     for row in rows:
#         print("***************")
#         print("ID",row[0])
#         print("Name",row[1])
#         print("Age:",row[2])
#         print("marks",row[3])
#         print("----------------")

# except sqlite3.Error as e:
#     print("An error occured while inserting data:",e)

# finally:
#     if conn:
#         cursor.close()
#         conn.close()





