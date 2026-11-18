
import pandas as pd
## Dataset 1: Students


students = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6],
    'name': ['Asha', 'Rahul', 'John', 'Sara', 'David', 'Priya'],
    'course': ['Python', 'Java', 'Python', 'SQL', 'Java', 'Python']
})


## Dataset 2: Marks


marks = pd.DataFrame({
    'student_id': [1, 2, 3, 5, 7],
    'marks': [85, 90, 78, 65, 88],
    'grade': ['A', 'A+', 'B', 'C', 'A']
})

## Dataset 3: Fees


fees = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 7],
    'fees_paid': [15000, 18000, 15000, 12000, 20000],
    'payment_status': ['Paid', 'Paid', 'Pending', 'Paid', 'Paid']
})


## Dataset 4: Contact


contact = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 6],
    'city': ['Bangalore', 'Mysore', 'Chennai', 'Delhi', 'Mumbai'],
    'phone': [98761, 98762, 98763, 98764, 98765]
})


## Dataset 5: New Batch


new_batch = pd.DataFrame({
    'student_id': [7, 8, 9, 10],
    'name': ['Kiran', 'Meena', 'Arun', 'Neha'],
    'course': ['Python', 'Java', 'SQL', 'Python']
})





#1. Merge students and marks using student_id.

result = pd.merge(students, marks, on="student_id")
print(result)

#2. Perform an inner merge between students and marks.

result = pd.merge(students, marks, on="student_id", how="inner")
print(result)

#3. Perform a left merge between students and marks.

result = pd.merge(students, marks, on="student_id", how="left")
print(result)

#4. Perform a right merge between students and marks.

result = pd.merge(students, marks, on="student_id", how="right")
print(result)

#5. Perform an outer merge between students and marks.

result = pd.merge(students, marks, on="student_id", how="outer")
print(result)

#6. Find all students who have examination marks.

result = pd.merge(students, marks, on="student_id", how="inner")
print(result)

#7. Find students who do not have examination marks.

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="left",
    indicator=True
)

print(result[result["_merge"] == "left_only"])

#8. Find records that exist only in the marks DataFrame.

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="outer",
    indicator=True
)

print(result[result["_merge"] == "right_only"])

#9. Merge students and fees using student_id.

result = pd.merge(students, fees, on="student_id")
print(result)

#10. Perform an outer merge between students and fees.

result = pd.merge(
    students,
    fees,
    on="student_id",
    how="outer"
)

print(result)

#11. Merge students and contact details using student_id.

result = pd.merge(
    students,
    contact,
    on="student_id"
)

print(result)

#12. Find students who do not have contact details.

result = pd.merge(
    students,
    contact,
    on="student_id",
    how="left",
    indicator=True
)

print(result[result["_merge"] == "left_only"])

#13. Merge students and marks using the left DataFrame as the primary DataFrame.

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="left"
)

print(result)

#14. Use the indicator=True parameter to identify the source of each record.

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="outer",
    indicator=True
)

print(result)

#15. Count how many records belong to both, left_only and right_only.

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="outer",
    indicator=True
)

print(result["_merge"].value_counts())

#16. Merge students, marks and fees into one DataFrame.

result = pd.merge(students, marks, on="student_id", how="outer")
result = pd.merge(result, fees, on="student_id", how="outer")
print(result)

#17. Merge all four DataFrames: students, marks, fees and contact.

result = pd.merge(students, marks, on="student_id", how="outer")
result = pd.merge(result, fees, on="student_id", how="outer")
result = pd.merge(result, contact, on="student_id", how="outer")

print(result)

#18. Create a final student report.

result = pd.merge(students, marks, on="student_id", how="outer")
result = pd.merge(result, fees, on="student_id", how="outer")
result = pd.merge(result, contact, on="student_id", how="outer")

print(result)

#19. Students who paid fees but do not have marks.

result = pd.merge(students, marks, on="student_id", how="outer")
result = pd.merge(result, fees, on="student_id", how="outer")

print(
    result[
        (result["fees_paid"].notna()) &
        (result["marks"].isna())
    ]
)

#20. Students with marks but no fees.

print(
    result[
        (result["marks"].notna()) &
        (result["fees_paid"].isna())
    ]
)

#21. Students having marks and contact details.

result = pd.merge(students, marks, on="student_id")
result = pd.merge(result, contact, on="student_id")

print(result)

#22. Students present in all four DataFrames.

result = pd.merge(students, marks, on="student_id")
result = pd.merge(result, fees, on="student_id")
result = pd.merge(result, contact, on="student_id")

print(result)

#23. Students missing either fees or marks.

result = pd.merge(students, marks, on="student_id", how="outer")
result = pd.merge(result, fees, on="student_id", how="outer")

print(
    result[
        result["marks"].isna() |
        result["fees_paid"].isna()
    ]
)

#24. Calculate average marks.

result = pd.merge(students, marks, on="student_id")

print(result["marks"].mean())

#25. Number of students enrolled in each course having marks.

result = pd.merge(students, marks, on="student_id")

print(
    result.groupby("course")["student_id"].count()
)

#Another dataset

employee = pd.DataFrame({
    'name': ['Asha', 'Rahul', 'John', 'Sara', 'David'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}, index=[1, 2, 3, 4, 5])

salary = pd.DataFrame({
    'salary': [25000, 35000, 40000, 30000, 45000]
}, index=[1, 2, 3, 5, 6])

attendance = pd.DataFrame({
    'days_present': [22, 25, 20, 24, 26]
}, index=[1, 2, 3, 4, 6])


#26. Inner join employee and salary.

result = employee.join(salary, how="inner")
print(result)

#27. Left join employee and salary.

result = employee.join(salary, how="left")
print(result)

#28. Right join employee and salary.

result = employee.join(salary, how="right")
print(result)

#29. Outer join employee and salary.

result = employee.join(salary, how="outer")
print(result)

#30. Join employee and attendance.

result = employee.join(attendance)
print(result)

#31. Join employee, salary and attendance.

result = employee.join(salary, how="outer")
result = result.join(attendance, how="outer")

print(result)

#32. Employees without salary records.

result = employee.join(salary, how="left")

print(result[result["salary"].isna()])

#33. Salary records without employee details.

result = employee.join(salary, how="outer")

print(result[result["name"].isna()])

#34. Employees salary > 30000.

result = employee.join(salary)

print(result[result["salary"] > 30000])

#35. Average salary.

result = employee.join(salary)

print(result["salary"].mean())


#Another dataset


batch1 = pd.DataFrame({
    'name': ['Asha', 'Rahul', 'John'],
    'marks': [85, 90, 78]
})

batch2 = pd.DataFrame({
    'name': ['Sara', 'David', 'Priya'],
    'marks': [88, 65, 92]
})

batch3 = pd.DataFrame({
    'name': ['Kiran', 'Meena'],
    'marks': [75, 89]
})


#36. Concatenate batch1 and batch2 vertically.

result = pd.concat([batch1, batch2])
print(result)

#37. Concatenate batch1 and batch2 horizontally.

result = pd.concat([batch1, batch2], axis=1)
print(result)

#38. Concatenate all batches.

result = pd.concat([batch1, batch2, batch3])
print(result)

#39. Concatenate all batches with ignore index.

result = pd.concat(
    [batch1, batch2, batch3],
    ignore_index=True
)

print(result)

#40. Concatenate without resetting indexes.

result = pd.concat([batch1, batch2])
print(result)

#41. Total students.

result = pd.concat(
    [batch1, batch2, batch3],
    ignore_index=True
)

print(result.shape[0])

#42. Average marks.

print(result["marks"].mean())

#43. Sort by marks descending.

print(
    result.sort_values(
        "marks",
        ascending=False
    )
)

#44. Highest scoring student.

print(
    result.loc[
        result["marks"].idxmax()
    ]
)

#45. Different columns and missing values.

df1 = pd.DataFrame({
    "name":["Asha","Rahul"],
    "marks":[85,90]
})

df2 = pd.DataFrame({
    "name":["John","Sara"],
    "city":["Delhi","Mysore"]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

print(result.isna())

#46. Student Management System

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="outer"
)

result = pd.merge(
    result,
    fees,
    on="student_id",
    how="outer"
)

print(result)

#47. Employee Management System

result = employee.join(salary, how="outer")
result = result.join(attendance, how="outer")

print(result)

#48. Sales Management

sales_january = pd.DataFrame({
    "product":["Laptop","Mobile","Tablet"],
    "sales":[50000,30000,20000]
})

sales_february = pd.DataFrame({
    "product":["Laptop","Mobile","Tablet"],
    "sales":[60000,35000,25000]
})

sales = pd.concat(
    [sales_january, sales_february],
    ignore_index=True
)

print(sales)

print(
    sales.groupby("product")["sales"].sum()
)

print(
    sales.groupby("product")["sales"].sum().idxmax()
)

#49. Missing Information Challenge

result = pd.merge(
    students,
    marks,
    on="student_id",
    how="outer",
    indicator=True
)

print(result)

print(
    result[
        result["_merge"]=="left_only"
    ]
)

print(
    result[
        result["_merge"]=="right_only"
    ]
)

#50. Final Data Analysis Challenge

students_df = pd.read_csv("students.csv")
marks_df = pd.read_csv("marks.csv")
fees_df = pd.read_csv("fees.csv")
attendance_df = pd.read_csv("attendance.csv")

result = pd.merge(
    students_df,
    marks_df,
    on="student_id",
    how="outer"
)

result = pd.merge(
    result,
    fees_df,
    on="student_id",
    how="outer"
)

result = pd.merge(
    result,
    attendance_df,
    on="student_id",
    how="outer"
)

print(result[result["marks"].isna()])

print(
    result[
        result["payment_status"]=="Pending"
    ]
)

print(
    result[
        result["attendance"] < 75
    ]
)

print(result["marks"].mean())

print(
    result.loc[
        result["marks"].idxmax()
    ]
)

result.to_csv(
    "final_report.csv",
    index=False
)

print(result)
