# Mini Project : Student Performance Analysis Using Pandas

# Task 1: Load and explore

#1. Import Pandas.
import pandas as pd

#2. Read the CSV file.

df=pd.read_csv("student_performance.csv")

#3. Display the first five records.
print(df.head(5))

#4. Display the last five records.
print(df.tail(5))


##5. Find the number of rows and columns.

print(df.shape)

#6. Display column names.

print(df.columns.tolist())

#7. Check the data types.

print(df.dtypes)

# Task 2: Data Selection

#1. Display only student names.

print(df["Name"])

#2. Display names and Python marks.

print(df[["Name","Python"]])

#3. Display names, Maths and SQL marks.

print(df[["Name","Maths","SQL"]])

#4. Display the first five students' records.

print(df.head(5))

# Task 3: Filtering

#1. Find students who scored more than 80 in Python.

print(df[df["Python"]>80])

#2. Find students whose attendance is below 75%.
print(df[df["Attendance"]<75])

#3. Find female students.

print(df[df["Gender"]=="Female"])

#4. Find students who scored more than 80 in both Python and Maths

print(df[(df["Python"]>80) & (df["Maths"]>80)])

#5. Find students whose SQL marks are between 60 and 90.

print(df[df["SQL"].between(60,90)])

# Task 4: Sorting

#1. Sort students based on Python marks in ascending order.

print(df.sort_values(by="Python"))

#2. Sort students based on Maths marks in descending order.

print(df.sort_values(by="Maths",ascending=False))

#3. Find the top five students based on SQL marks.

print(df.sort_values(by="SQL",ascending=False).head(5))

#4. Display the student with the lowest attendance.

print(df.sort_values(by="Attendance").head(1))

# Task 5: Aggregation

#1. Calculate the average Python marks.

print("Average Python Marks:",df["Python"].mean())

#2. Calculate the average Maths marks.
print("Average Maths marks:", df["Maths"].mean())

#3. Find the highest Python mark.
print("Highest Python mark:", df["Python"].max())

#4. Find the lowest SQL mark.
print("Lowest SQL mark:", df["SQL"].min())

#5. Calculate the average attendance.
print("Average attendance:", df["Attendance"].mean())

#6. Find the total number of students.
print("Total number of students:", len(df))

# Task 6: Create new columns

# Create a new column called "Total_Marks"
df["Total_Marks"] = df["Python"] + df["Maths"] + df["SQL"]

# Create another column called "Average_Marks"

df["Average_Marks"]=df["Total_Marks"]/3

#1. Display student names with total marks.
print(df[["Name","Total_Marks"]])

#2. Find students with an average above 80.

print(df[df["Average_Marks"]>80][["Name","Average_Marks"]])

#3. Find students with an average below 50.
print(df[df["Average_Marks"] < 50][["Name", "Average_Marks"]])

#4. Find the topper based on average marks.

print(df.sort_values(by="Average_Marks",ascending=False).head(1)[["Name","Average_Marks"]])

# Task 7: Grouping

#1. Group students based on gender.

print(df.groupby("Gender").get_group("Male"))

print(df.groupby("Gender").get_group("Female"))

#2. Calculate average Python marks for each gender.
print(df.groupby("Gender")["Python"].mean())

#3. Calculate average Maths marks for each gender.
print(df.groupby("Gender")["Maths"].mean())

#4. Find the average attendance for each gender.
print(df.groupby("Gender")["Attendance"].mean())

# Final Project Challenge

print("\nSTUDENT PERFORMANCE REPORT :")
print("Total Students:", len(df))

print("\nHighest Python marks :")
print(df.sort_values("Python", ascending=False)[["Name", "Python"]].head(1))

print("\nHighest Maths marks :")
print(df.sort_values("Maths", ascending=False)[["Name", "Maths"]].head(1))

print("\nHighest SQL marks :")
print(df.sort_values("SQL", ascending=False)[["Name", "SQL"]].head(1))

print("\nOverall Topper :")
print(df.sort_values("Average_Marks", ascending=False)[["Name", "Average_Marks"]].head(1))

print("\nAverage Attendance:", df["Attendance"].mean())

print("\nStudents below 50 average:")
print(df[df["Average_Marks"] < 50]["Name"])

print("\nStudents above 80 average:")
print(df[df["Average_Marks"] > 80]["Name"])

# Bonus : Grades

df.loc[df["Average_Marks"] >= 90, "Grade"] = "A+"
df.loc[(df["Average_Marks"] >= 80) & (df["Average_Marks"] < 90), "Grade"] = "A"
df.loc[(df["Average_Marks"] >= 70) & (df["Average_Marks"] < 80), "Grade"] = "B"
df.loc[(df["Average_Marks"] >= 60) & (df["Average_Marks"] < 70), "Grade"] = "C"
df.loc[(df["Average_Marks"] >= 50) & (df["Average_Marks"] < 60), "Grade"] = "D"
df.loc[df["Average_Marks"] < 50, "Grade"] = "Fail"

print("\nStudent Grades :")
print(df[["Name", "Average_Marks", "Grade"]])

# Expected Final Output

print("\nSTUDENT PERFORMANCE REPORT :")

print("\nTotal Students:",len(df))

print("\nTopper :")
print(df.sort_values("Average_Marks", ascending=False)[["Name", "Average_Marks"]].head(1))

print("\nAverage Python Marks :",df["Python"].mean())

print("\nAverage Maths Marks :",df["Maths"].mean())

print("\nAverage SQL Marks :",df["SQL"].mean())

print("\nStudents Below 50 :")
print(df[df["Average_Marks"]<50]["Name"])

print("\nStudents Above 80 :")
print(df[df["Average_Marks"]>80]["Name"])

print("\Gender Wise Performance :")
print(df.groupby("Gender")[["Python", "Maths", "SQL", "Attendance"]].mean())

