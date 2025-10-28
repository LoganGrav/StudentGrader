import pandas as pd # import pandas for data frames and csv reading
import sqlite3  #import sqlite3 for database

conn = sqlite3.connect("Task2.db")  #create database
cursor = conn.cursor() 

#1- Create a database  named "Student" that contains a table "Ten_Students" with the following schema:
 #"ID"  primary key , INT ;  First_name : TEXT ;  Last_name: TEXT ; Midterm: REAL , Final: REAL , Project1: REAL , Project2:  REAL , Grade: REAL ; Letter_Grade: TEXT
cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Ten_Students (
        ID INTEGER PRIMARY KEY,
        First_name TEXT,
        Last_name TEXT,
        Midterm REAL,
        Final REAL,
        Project1 REAL,
        Project2 REAL,
        Grade REAL,
        Letter_Grade TEXT
    )
''')
conn.commit()



#2- Develop an insert-query  to import records from 'Ten_Students_Grades.CSV' into the 'Ten_Students' table.
df = pd.read_csv("Ten_Students_Grades.CSV") #read csv file

#rename dataframe columns to match sql table names
df.rename(columns={
    "id": "ID",
    "first_name": "First_name",
    "last_name": "Last_name",
    "Midterm Exam- 100 Pts.": "Midterm",
    "Final Exam- 100 Pts.": "Final",
    "Project 1- 100 Pts.": "Project1",
    "Project 2 - 100 Pts.": "Project2",
    "Letter Grade": "Letter_Grade"
}, inplace=True)

df.drop_duplicates(subset=["ID"], inplace=True) #remove duplicates
for index, row in df.iterrows(): #iterate through dataframe
    cursor.execute('''
        INSERT OR IGNORE INTO Ten_Students (ID, First_name, Last_name, Midterm, Final, Project1, Project2, Grade, Letter_Grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (row["ID"], row["First_name"], row["Last_name"], row["Midterm"], row["Final"], row["Project1"], row["Project2"], row["Grade"], row["Letter_Grade"]))
conn.commit()    #add data into table



#3- Implement a query to display students sorted alphabetically by name (ascending order).
students_sorted = pd.read_sql_query('''
    SELECT First_name, Last_Name FROM Ten_Students
    ORDER BY First_name ASC, Last_name ASC
''', conn)
print("Sorted names:")
print(students_sorted)



#4- Develop a query to generate a frequency distribution of Letter Grades, showing the count of students per grade category.
grade_distribution = pd.read_sql_query('''
    SELECT Letter_Grade, COUNT(*) AS Frequency
    FROM Ten_Students
    GROUP BY Letter_Grade
''', conn)
print("\nFrequency Distribution:")
print(grade_distribution)



#5- Execute a query to remove all records where Letter_Grade equals 'D'."
cursor.execute('''
    DELETE FROM Ten_Students
    WHERE Letter_Grade = 'D'
''')
conn.commit()
print("\nAll students with a grade of 'D' removed.")


conn.close() #close connection
