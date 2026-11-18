import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Aisha", "Rahul", "Sneha", "Arjun", "Priya", "Kiran", "Megha", "Rohan"],
    "Age": [21, 22, 20, 23, 21, 22, 20, 24],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Course": ["Python", "Java", "Python", "Data Science", "Java", "Python", "Data Science", "Java"],
    "Attendance": [90, 75, 85, 60, 95, 80, 70, 55],
    "Marks": [85, 65, 92, 45, 88, 78, 55, 40],
    "Fees": [15000, 12000, 15000, 20000, 12000, 15000, 20000, 12000],
    "Placement_Status": ["Placed", "Not Placed", "Placed", "Not Placed",
                         "Placed", "Placed", "Not Placed", "Not Placed"]
}

df = pd.DataFrame(data)

# Display only the Name column.
print(df["Name"])

# Display only the Student_ID column.
print(df["Student_ID"])

# Display the Course and Fees columns.
print(df[["Course", "Fees"]])

# Display the Name, Age and Gender columns.
print(df[["Name", "Age", "Gender"]])

# Display the Name, Course, Marks and Attendance columns.
print(df[["Name", "Course", "Marks", "Attendance"]])

# Display the Student_ID, Name and Placement_Status columns.
print(df[["Student_ID", "Name", "Placement_Status"]])

# Select the Age and Marks columns using loc.
print(df.loc[:, ["Age", "Marks"]])

# Select the Name, Gender and Course columns using loc.
print(df.loc[:, ["Name", "Gender", "Course"]])

# Select the first three columns using iloc.
print(df.iloc[:, 0:3])

# Select the last three columns using iloc.
print(df.iloc[:, -3:])

# Select the columns at positions 1, 3 and 5 using iloc.
print(df.iloc[:, [1, 3, 5]])

# Select the columns at positions 2, 4, 6 and 7.
print(df.iloc[:, [2, 4, 6, 7]])

# Display columns from position 0 to position 4 using slicing.
print(df.iloc[:, 0:5])

# Display columns from position 3 to position 6 using slicing.
print(df.iloc[:, 3:7])

# Select only Name and Placement_Status using loc.
print(df.loc[:, ["Name", "Placement_Status"]])

# Select Course, Attendance and Fees using loc.
print(df.loc[:, ["Course", "Attendance", "Fees"]])

# Select the first five columns using iloc.
print(df.iloc[:, 0:5])

# Select the last two columns using iloc.
print(df.iloc[:, -2:])

# Create a new column called Result.
df["Result"] = ["Pass" if x >= 50 else "Fail" for x in df["Marks"]]
print(df)

# Create a new column called Percentage.
df["Percentage"] = df["Marks"]
print(df)

# Create a new column called Attendance_Status.
df["Attendance_Status"] = ["Good" if x >= 75 else "Poor" for x in df["Attendance"]]
print(df)

# Create a new column called Student_Category.
df["Student_Category"] = ["Senior" if x > 22 else "Junior" for x in df["Age"]]
print(df)

# Create a new column called Scholarship.
df["Scholarship"] = ["Eligible" if x >= 85 else "Not Eligible" for x in df["Marks"]]
print(df)

# Create a new column called Course_Fees_Status.
df["Course_Fees_Status"] = ["High Fees" if x > 15000 else "Normal Fees" for x in df["Fees"]]
print(df)

# Create a new column called Bonus_Marks.
df["Bonus_Marks"] = df["Marks"] + 5
print(df)

# Create a new column called Total_Fees.
df["Total_Fees"] = df["Fees"] + 2000
print(df)

# Create a new column called Age_After_5_Years.
df["Age_After_5_Years"] = df["Age"] + 5
print(df)

# Create a new column called Attendance_Bonus.
df["Attendance_Bonus"] = df["Attendance"] * 2
print(df)

# Create a new column called Double_Marks.
df["Double_Marks"] = df["Marks"] * 2
print(df)

# Create a new column called Student_Status.
df["Student_Status"] = ["Successful" if x == "Placed" else "Pending"
                        for x in df["Placement_Status"]]
print(df)

# Increase every student's attendance by 5.
df["Attendance"] = df["Attendance"] + 5
print(df)

# Decrease every student's attendance by 10.
df["Attendance"] = df["Attendance"] - 10
print(df)

# Increase every student's marks by 10.
df["Marks"] = df["Marks"] + 10
print(df)

# Reduce every student's fees by ₹500.
df["Fees"] = df["Fees"] - 500
print(df)

# Increase every student's age by 1.
df["Age"] = df["Age"] + 1
print(df)

# Multiply every student's marks by 2.
df["Marks"] = df["Marks"] * 2
print(df)

# Add 10 to every student's attendance.
df["Attendance"] = df["Attendance"] + 10
print(df)

# Rename Student_ID to ID.
print(df.rename(columns={"Student_ID": "ID"}))

# Rename Name to Student_Name.
print(df.rename(columns={"Name": "Student_Name"}))

# Rename Placement_Status to Placement.
print(df.rename(columns={"Placement_Status": "Placement"}))

# Rename Attendance to Attendance_Percentage.
print(df.rename(columns={"Attendance": "Attendance_Percentage"}))

# Rename Marks to Exam_Marks and Fees to Course_Fees.
print(df.rename(columns={"Marks": "Exam_Marks",
                         "Fees": "Course_Fees"}))

# Delete the Gender column.
print(df.drop("Gender", axis=1))

# Delete the Age column.
print(df.drop("Age", axis=1))

# Delete the Student_ID column.
print(df.drop("Student_ID", axis=1))

# Delete both Gender and Age columns together.
print(df.drop(["Gender", "Age"], axis=1))

# 47. Student Academic Report
df["Result"] = ["Pass" if x >= 50 else "Fail" for x in df["Marks"]]

df["Performance"] = [
    "Excellent" if x >= 85
    else "Good" if x >= 70
    else "Average" if x >= 50
    else "Poor"
    for x in df["Marks"]
]

print(df[["Name", "Marks", "Result", "Performance"]])

# 48. Student Scholarship Report
df["Scholarship_Status"] = [
    "Full Scholarship" if x >= 90
    else "Half Scholarship" if x >= 80
    else "No Scholarship"
    for x in df["Marks"]
]

print(df[["Name", "Course", "Marks", "Scholarship_Status"]])

# 49. Student Attendance Report
df["Attendance_Status"] = [
    "Excellent" if x >= 90
    else "Good" if x >= 75
    else "Low"
    for x in df["Attendance"]
]

df["Attendance"] = df["Attendance"] + 5

print(df[["Name", "Attendance", "Attendance_Status"]])

# 50. Complete Student Report
df["Result"] = ["Pass" if x >= 50 else "Fail" for x in df["Marks"]]

df["Percentage"] = df["Marks"]

df["Attendance_Status"] = [
    "Good" if x >= 75 else "Poor"
    for x in df["Attendance"]
]

df["Scholarship"] = [
    "Eligible" if x >= 85 else "Not Eligible"
    for x in df["Marks"]
]

df = df.rename(columns={
    "Name": "Student_Name",
    "Fees": "Course_Fees"
})

df = df.drop("Gender", axis=1)

print(df[[
    "Student_Name",
    "Course",
    "Marks",
    "Percentage",
    "Result",
    "Attendance_Status",
    "Scholarship"
]])