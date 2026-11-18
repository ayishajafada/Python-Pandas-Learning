import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "John",
             "Kiran", "Meena", "Arjun", "Divya", "Rohit"],

    "Department": ["IT", "HR", "IT", "HR", "Finance",
                   "IT", "Finance", "HR", "IT", "Finance"],

    "Salary": [30000, 25000, 40000, 35000, 28000,
               45000, 32000, 25000, 40000, 35000],

    "Age": [23, 25, 24, 26, 22, 29, 27, 24, 28, 26],

    "Experience": [1, 2, 3, 4, 1, 5, 3, 2, 4, 3]
}

df = pd.DataFrame(data)

print(df)


# LEVEL 1: BASIC SORTING

# 1. Sort employees according to their salary in ascending order.
print(df.sort_values(by="Salary", ascending=True))


# 2. Sort employees according to their salary in descending order.
print(df.sort_values(by="Salary", ascending=False))


# 3. Sort employees according to their age from youngest to oldest.
print(df.sort_values(by="Age", ascending=True))


# 4. Sort employees according to their age from oldest to youngest.
print(df.sort_values(by="Age", ascending=False))


# 5. Sort employees alphabetically by their names.
print(df.sort_values(by="Name", ascending=True))


# 6. Sort employees according to their experience in ascending order.
print(df.sort_values(by="Experience", ascending=True))


# 7. Display the employee with the highest salary.
print(df.sort_values(by="Salary", ascending=False).head(1))


# 8. Display the employee with the lowest salary.
print(df.sort_values(by="Salary", ascending=True).head(1))


# 9. Display the five employees with the highest salaries.
print(df.sort_values(by="Salary", ascending=False).head(5))


# 10. Display the three youngest employees.
print(df.sort_values(by="Age", ascending=True).head(3))


# LEVEL 2: ADVANCED SORTING

# 11. Sort employees by Department alphabetically.
print(df.sort_values(by="Department", ascending=True))


# 12. Sort employees by Department and then Salary.
print(df.sort_values(by=["Department", "Salary"]))


# 13. Sort employees by Department in ascending order and Salary in descending order.
print(df.sort_values(by=["Department", "Salary"], ascending=[True, False]))


# 14. Sort employees by Age and Experience, both in descending order.
print(df.sort_values(by=["Age", "Experience"], ascending=[False, False]))


# 15. Sort employees by Salary first and Age second.
print(df.sort_values(by=["Salary", "Age"], ascending=[True, True]))


# 16. Sort employees by Salary in descending order and display only Name and Salary.
print(df.sort_values(by="Salary", ascending=False)[["Name", "Salary"]])


# 17. Sort employees by Experience in descending order and display the top three.
print(df.sort_values(by="Experience", ascending=False).head(3))


# 18. Sort employees by Department and then Name alphabetically.
print(df.sort_values(by=["Department", "Name"], ascending=[True, True]))


# 19. Sort employees by Age in ascending order and Salary in descending order.
print(df.sort_values(by=["Age", "Salary"], ascending=[True, False]))


# 20. Sort employees by Salary, Department and Age.
print(df.sort_values(by=["Salary", "Department", "Age"]))


# LEVEL 3: INDEX SORTING

# 21. Sort the DataFrame using its index in ascending order.
print(df.sort_index(ascending=True))


# 22. Sort the DataFrame using its index in descending order.
print(df.sort_index(ascending=False))


# 23. Create a new DataFrame with custom indexes and sort it using sort_index().
new_df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Sneha"],
    "Salary": [30000, 25000, 40000, 35000]
}, index=[103, 101, 104, 102])

print(new_df.sort_index())


# 24. Reset the index after sorting employees by salary.
sorted_df = df.sort_values(by="Salary")
sorted_df = sorted_df.reset_index(drop=True)
print(sorted_df)


# 25. Sort employees by salary using inplace=True and print the original DataFrame.
df.sort_values(by="Salary", ascending=True, inplace=True)
print(df)


# LEVEL 4: RANKING

# 26. Create a new column called Salary_Rank using the rank function.
df["Salary_Rank"] = df["Salary"].rank()
print(df[["Name", "Salary", "Salary_Rank"]])


# 27. Assign Rank 1 to the employee with the highest salary.
df["Salary_Rank"] = df["Salary"].rank(ascending=False)
print(df[["Name", "Salary", "Salary_Rank"]])


# 28. Rank employees according to their age, with the youngest getting Rank 1.
df["Age_Rank"] = df["Age"].rank(ascending=True)
print(df[["Name", "Age", "Age_Rank"]])


# 29. Rank employees according to experience, with the highest experience getting Rank 1.
df["Experience_Rank"] = df["Experience"].rank(ascending=False)
print(df[["Name", "Experience", "Experience_Rank"]])


# 30. Create a salary ranking using the average method.
df["Average_Rank"] = df["Salary"].rank(method="average", ascending=False)
print(df[["Name", "Salary", "Average_Rank"]])


# 31. Create a salary ranking using the min method.
df["Min_Rank"] = df["Salary"].rank(method="min", ascending=False)
print(df[["Name", "Salary", "Min_Rank"]])


# 32. Create a salary ranking using the max method.
df["Max_Rank"] = df["Salary"].rank(method="max", ascending=False)
print(df[["Name", "Salary", "Max_Rank"]])


# 33. Create a salary ranking using the first method.
df["First_Rank"] = df["Salary"].rank(method="first", ascending=False)
print(df[["Name", "Salary", "First_Rank"]])


# 34. Create a salary ranking using the dense method.
df["Dense_Rank"] = df["Salary"].rank(method="dense", ascending=False)
print(df[["Name", "Salary", "Dense_Rank"]])


# 35. Compare all five ranking methods using the Salary column.
df["Average"] = df["Salary"].rank(method="average", ascending=False)
df["Min"] = df["Salary"].rank(method="min", ascending=False)
df["Max"] = df["Salary"].rank(method="max", ascending=False)
df["First"] = df["Salary"].rank(method="first", ascending=False)
df["Dense"] = df["Salary"].rank(method="dense", ascending=False)

print(df[["Name", "Salary", "Average", "Min", "Max", "First", "Dense"]])


# LEVEL 5: REAL-WORLD CHALLENGES

# 36. Find the highest-paid employee in each department.
highest_paid = df.loc[df.groupby("Department")["Salary"].idxmax()]
print(highest_paid)


# 37. Find the lowest-paid employee in each department.
lowest_paid = df.loc[df.groupby("Department")["Salary"].idxmin()]
print(lowest_paid)


# 38. Rank employees within each department based on salary.
df["Department_Rank"] = df.groupby("Department")["Salary"].rank(
    method="dense", ascending=False
)
print(df[["Name", "Department", "Salary", "Department_Rank"]])


# 39. Identify the top two highest-paid employees in every department.
top_two = df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
).groupby("Department").head(2)

print(top_two)


# 40. Identify employees who share the same salary.
same_salary = df[df.duplicated(subset=["Salary"], keep=False)]
print(same_salary.sort_values(by="Salary"))


# 41. Find the employees whose salary rank is within the top three.
df["Salary_Rank"] = df["Salary"].rank(method="dense", ascending=False)

top_three = df[df["Salary_Rank"] <= 3]
print(top_three[["Name", "Salary", "Salary_Rank"]])


# 42. Create separate rankings for Age, Salary and Experience.
df["Age_Rank"] = df["Age"].rank(ascending=True)
df["Salary_Rank"] = df["Salary"].rank(ascending=False)
df["Experience_Rank"] = df["Experience"].rank(ascending=False)

print(df[["Name", "Age_Rank", "Salary_Rank", "Experience_Rank"]])


# 43. Find the department with the highest average salary.
average_salary = df.groupby("Department")["Salary"].mean()
print(average_salary.sort_values(ascending=False).head(1))


# 44. Display employees ranked by salary and then sort the result by rank.
df["Salary_Rank"] = df["Salary"].rank(method="dense", ascending=False)

ranked_df = df.sort_values(by="Salary_Rank", ascending=True)
print(ranked_df[["Name", "Salary", "Salary_Rank"]])


# 45. Create a final report containing Name, Department, Salary and Salary Rank.
df["Salary_Rank"] = df["Salary"].rank(method="dense", ascending=False)

final_report = df[["Name", "Department", "Salary", "Salary_Rank"]]
print(final_report.sort_values(by="Salary_Rank"))


# LEVEL 6: THINKING CHALLENGES

# 46. Two employees have the same salary. Explain how their ranks differ when using average, min and dense.

salary_data = pd.Series([40000, 35000, 35000, 30000])

print("Average Ranking:")
print(salary_data.rank(method="average", ascending=False))

print("Min Ranking:")
print(salary_data.rank(method="min", ascending=False))

print("Dense Ranking:")
print(salary_data.rank(method="dense", ascending=False))


# 47. What happens to the original DataFrame when you use inplace=True?

sample_df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Salary": [30000, 25000, 40000]
})

sample_df.sort_values(by="Salary", ascending=False, inplace=True)

print(sample_df)


# 48. Can you sort a DataFrame by two columns where one is ascending and the other is descending? Demonstrate it.
print(df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
))


# 49. If five employees have salaries of 50,000, 45,000, 45,000, 40,000 and 35,000, calculate their ranks using all five ranking methods.

salary = pd.Series([50000, 45000, 45000, 40000, 35000])

ranking = pd.DataFrame({
    "Salary": salary,
    "Average": salary.rank(method="average", ascending=False),
    "Min": salary.rank(method="min", ascending=False),
    "Max": salary.rank(method="max", ascending=False),
    "First": salary.rank(method="first", ascending=False),
    "Dense": salary.rank(method="dense", ascending=False)
})

print(ranking)


# 50. Create your own employee DataFrame containing at least 15 employees, five departments and repeated salary values. Perform sorting, ranking and top-performer analysis.

employee_data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "John",
             "Kiran", "Meena", "Arjun", "Divya", "Rohit",
             "Vijay", "Anjali", "Varun", "Neha", "Sanjay"],

    "Department": ["IT", "HR", "Finance", "Marketing", "Sales",
                   "IT", "HR", "Finance", "Marketing", "Sales",
                   "IT", "HR", "Finance", "Marketing", "Sales"],

    "Salary": [30000, 25000, 40000, 35000, 28000,
               45000, 32000, 25000, 40000, 35000,
               50000, 30000, 45000, 38000, 42000],

    "Age": [23, 25, 24, 26, 22, 29, 27, 24, 28, 26,
            30, 25, 31, 27, 29],

    "Experience": [1, 2, 3, 4, 1, 5, 3, 2, 4, 3,
                   6, 2, 7, 4, 5]
}

employee_df = pd.DataFrame(employee_data)

print("Original Employee DataFrame:")
print(employee_df)


# Sorting employees by salary in descending order.
print(employee_df.sort_values(by="Salary", ascending=False))


# Sorting employees by department and salary.
print(employee_df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
))


# Creating salary ranks.
employee_df["Salary_Rank"] = employee_df["Salary"].rank(
    method="dense", ascending=False
)

print(employee_df[["Name", "Salary", "Salary_Rank"]])


# Creating age and experience rankings.
employee_df["Age_Rank"] = employee_df["Age"].rank(ascending=True)

employee_df["Experience_Rank"] = employee_df["Experience"].rank(
    method="dense", ascending=False
)

print(employee_df[["Name", "Age_Rank", "Salary_Rank", "Experience_Rank"]])


# Finding the highest-paid employee in each department.
highest_salary = employee_df.loc[
    employee_df.groupby("Department")["Salary"].idxmax()
]

print(highest_salary)


# Finding the top two highest-paid employees in each department.
top_employees = employee_df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
).groupby("Department").head(2)

print(top_employees)


# Finding the highest-paid employee overall.
print(employee_df.loc[employee_df["Salary"].idxmax()])


# Finding the department with the highest average salary.
department_average = employee_df.groupby("Department")["Salary"].mean()

print(department_average.sort_values(ascending=False).head(1))


# Creating the final employee report.
final_report = employee_df[
    ["Name", "Department", "Salary", "Salary_Rank"]
].sort_values(by="Salary_Rank")

print(final_report)