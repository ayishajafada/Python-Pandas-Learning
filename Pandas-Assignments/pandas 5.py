import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Amit', 'Rahul'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'Salary': [30000, 25000, 40000, 35000, 45000, 28000],
    'Age': [23, 25, 24, 26, 27, 28]
}

df = pd.DataFrame(data)

print(df)
import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Amit', 'Rahul'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'Salary': [30000, 25000, 40000, 35000, 45000, 28000],
    'Age': [23, 25, 24, 26, 27, 28]
}

df = pd.DataFrame(data)
print(df)

#evel 1: Basic Aggregation (1–10)

#1. Find the total salary of all employees.
print(df["Salary"].sum())
#2. Calculate the average salary of employees.
print(df["Salary"].mean())
#3. Find the highest salary.
print(df["Salary"].max())
#4. Find the lowest salary.
print(df["Salary"].min())
#5. Count the total number of employees using count().
print(df["Name"].count())
#6. Calculate the average age of employees.
print(df["Age"].mean())
#7. Find the maximum age.
print(df["Age"].max())
#8. Find the minimum age.
print(df["Age"].min())
#9. Calculate the sum of all employee ages.
print(df["Age"].sum())
#10. Find the sum, mean, maximum and minimum salary using a single agg() function.

result=df["Salary"].agg(["sum","mean","max","min"])
print(result)

#Level 2: Basic Grouping (11–20)
#11. Group employees based on their department.

print(df.groupby("Department"))

#12. Find the total salary of each department.
result=df.groupby("Department")["Salary"].sum()
print(result)

#13. Calculate the average salary of each department.
result=df.groupby("Department")["Salary"].mean()
print(result)

#14. Find the highest salary in each department.

result=df.groupby("Department")["Salary"].max()
print(result)
#15. Find the lowest salary in each department.
result=df.groupby("Department")["Salary"].min()
print(result)
#16. Count the number of employees in each department.
result=df.groupby("Department")["Name"].count()
print(result)

#17. Find the average age of employees in each department.

result=df.groupby("Department")["Age"].mean()
print(result)

#18. Find the maximum age in each department.
result=df.groupby("Department")["Age"].max()
print(result)

#19. Find the minimum age in each department.
result=df.groupby("Department")["Age"].min()
print(result)
#20. Calculate the total age of employees in each department.
result=df.groupby("Department")["Age"].sum()
print(result)
#Level 3: Grouping with Multiple Aggregations (21–30)

#21. Find the sum and mean salary of each department.

result=df.groupby("Department")["Salary"].agg(["sum","mean"])
print(result)

#22. Find the maximum and minimum salary of each department

result=df.groupby("Department")["Salary"].agg(["max","min"])
print(result)

#23. Calculate sum, mean, max and min salary department-wise.
result=df.groupby("Department")["Salary"].agg(["sum","mean","max","min"])
print(result)

#24. Find the average age and average salary of each department.
result=df.groupby("Department")[["Age","Salary"]].mean()
print(result)

#25. Find the total salary and employee count of each department.

result=df.groupby("Department").agg({"Salary":"sum","Name":"count"})

print(result)

#26. Calculate the maximum age and minimum age of each department.
result=df.groupby("Department")["Age"].agg(["max","min"])
print(result)
#27. Find the sum, mean and count of salaries department-wise.
result=df.groupby("Department")["Salary"].agg(["sum","mean","count"])
print(result)
#28. Calculate multiple aggregations on both Salary and Age columns.
result=df.groupby("Department")[["Salary","Age"]].agg(["sum","mean","max","min"])
print(result)
#29. Find the total salary, average salary and maximum salary of each department.
result=df.groupby("Department")["Salary"].agg(["sum","mean","max"])
print(result)

#30. Generate a department-wise statistical summary using agg().

result=df.groupby("Department").agg({"Salary":["sum","mean","max","min"],
                                     "Age":["sum","mean","max","min"]})

print(result)

#Level 4: Intermediate Practice (31–40)
#31. Group employees by department and calculate their average salary. Store the result in a variable called result.

result=df.groupby("Department")["Salary"].mean()
print(result)
#32. Group employees by department and calculate total salary. Convert the result into a DataFrame using reset_index().
result=df.groupby("Department")["Salary"].sum().reset_index()
print(result)

#33. Find the department with the highest average salary.
result=df.groupby("Department")["Salary"].mean().idxmax()
print(result)
#34. Find the department with the lowest average salary.
result=df.groupby("Department")["Salary"].mean().idxmin()
print(result)
#35. Find the department with the highest total salary.
result=df.groupby("Department")["Salary"].sum().idxmax()
print(result)
#36. Group by department and count how many employees belong to each department.
result=df.groupby("Department")["Name"].count()
print(result)
#37. Group by department and calculate average salary. Sort the result in descending order.
result=df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(result)
#38. Group by department and calculate maximum salary. Sort the result in ascending order
result = df.groupby("Department")["Salary"].max().sort_values()

print(result)

#39. Group by department and calculate total salary and average age.
result=df.groupby("Department").agg({"Salary":"sum","Age":"mean"})
print(result)

#40. Create a summary table containing department, employee count, total salary and average salary

result=df.groupby("Department").agg({"Name":"count","Salary":["sum","mean"]})
print(result)

#Level 5: Real-World Data Analysis (41–50)

#41. Which department has the highest-paid employee?
result = df.groupby("Department")["Salary"].max().idxmax()

print(result)

#42. Which department has the youngest average employee age?

result=df.groupby("Department")["Age"].mean().idxmin()
print(result)

#43. Calculate the salary difference between the highest-paid and lowest-paid employee in each department.

result = df.groupby("Department")["Salary"].agg(
    lambda x: x.max() - x.min()
)
print(result)


#44. Find the percentage contribution of each department to the company's total salary expenditure.

total_salary = df["Salary"].sum()

result = (df.groupby("Department")["Salary"].sum() / total_salary) * 100
print(result)


#45. Calculate the average salary-to-age ratio for each department.

df["Salary_Age_Ratio"] = df["Salary"] / df["Age"]

result = df.groupby("Department")["Salary_Age_Ratio"].mean()
print(result)


#46. Find departments where the average salary is greater than ₹30,000.

result = df.groupby("Department")["Salary"].mean()

print(result[result > 30000])


#47. Find departments where the total salary expenditure is greater than ₹90,000.

result = df.groupby("Department")["Salary"].sum()

print(result[result > 90000])


#48. Generate a report showing the employee count, average age, average salary and maximum salary for each department.

result = df.groupby("Department").agg({
    "Name": "count",
    "Age": "mean",
    "Salary": ["mean", "max"]
})

print(result)

#49. Find the department with the highest average salary and display its department name and average salary.

result = df.groupby("Department")["Salary"].mean()

highest_department = result.idxmax()

print("Department:", highest_department)
print("Average Salary:", result.max())


#50. Create a complete department-wise report containing:
# Employee count
# Total salary
# Average salary
# Maximum salary
# Minimum salary
# Average age
# Maximum age
# Minimum age

result = df.groupby("Department").agg({
"Name": "count",
"Salary": ["sum", "mean", "max", "min"],
"Age": ["mean", "max", "min"]
})

print(result)

