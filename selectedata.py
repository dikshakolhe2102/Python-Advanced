#fetchall() : Gets all rows at once
import sqlite3

# try:
#     # Connect to the database
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     # Execute the SELECT query
#     cursor.execute('select * from students')
#     rows = cursor.fetchall()

#     print("rowcount:",cursor.rowcount)
#     # Display the results
#     print("Student Records:")
#     for row in rows:
#         print("***************")
#         print("ID",row[0])
#         print("Name",row[1])
#         print("Age:",row[2])
#         print("marks",row[3])
#         print("----------------")
        

# except sqlite3.Error as e:
#     print("An error occurred while fetching data:", e)

# finally:
#     if conn:
#         conn.close()




# # fetchone() → to retrieve one row at a time
# import sqlite3

# try:
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     cursor.execute('select * from students')

#     print("Student Records (using fetchone):")
#     row = cursor.fetchone()
#     while row is not None:
#         print(row)
#         row = cursor.fetchone()
#     #print(row)
# except sqlite3.Error as e:
#     print("An error occurred:", e)

# finally:
#     if conn:
#         conn.close()

# # fetchmany(size) → to retrieve a limited number of rows
# import sqlite3

try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('select * from students')

    print("Student Records (using fetchmany):")
    rows = cursor.fetchmany(2)  # fetch 2 rows at a time
    while rows:
        for row in rows:
            print(row)
        rows = cursor.fetchmany(2)

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()

        