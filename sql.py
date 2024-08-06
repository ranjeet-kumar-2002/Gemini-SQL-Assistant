import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create the table
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

cursor.execute(table_info)

# Insert some records
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Krish', 'Data Science', 'A', 40)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Radha', 'Data Analysis', 'B', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Kamal', 'Data Engineer', 'C', 80)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Pinki', 'Machine Learning', 'D', 70)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Komal', 'Data Science', 'A', 90)")

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit the transaction and close the connection
connection.commit()
connection.close()

