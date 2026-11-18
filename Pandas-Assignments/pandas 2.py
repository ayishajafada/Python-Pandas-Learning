import pandas as pd

# 1. Create a Pandas Series containing the numbers [10, 20, 30, 40, 50] and print it.
s = pd.Series([10, 20, 30, 40, 50])
print(s)

# 2. Create a Series containing five student names: Aisha, Rahul, Sana, John and Priya.
students = pd.Series(["Aisha", "Rahul", "Sana", "John", "Priya"])
print(students)

# 3. Create a Series containing the marks [85, 90, 78, 95, 88].
marks = pd.Series([85, 90, 78, 95, 88])
print(marks)

# 4. Create a Series containing the ages [21, 22, 23, 24, 25].
ages = pd.Series([21, 22, 23, 24, 25])
print(ages)

# 5. Create a Series containing the prices of five products.
prices = pd.Series([100, 250, 300, 450, 500])
print(prices)

# 6. Create a Series with custom indexes representing five employee names and their salaries.
salary = pd.Series(
    [25000, 30000, 35000, 40000, 45000],
    index=["Aisha", "Rahul", "Sana", "John", "Priya"]
)
print(salary)

# 7. Create a Series with custom indexes representing five subjects and their marks.
subject_marks = pd.Series(
    [90, 85, 88, 92, 80],
    index=["Python", "Java", "SQL", "Pandas", "HTML"]
)
print(subject_marks)

# 8. Create a Series with custom indexes representing five cities and their populations.
population = pd.Series(
    [1000000, 900000, 1200000, 800000, 700000],
    index=["Bangalore", "Mumbai", "Delhi", "Chennai", "Kochi"]
)
print(population)

# 9. Create a Series containing five different temperatures with weekdays.
temp = pd.Series(
    [25, 26, 27, 28, 29],
    index=["Mon", "Tue", "Wed", "Thu", "Fri"]
)
print(temp)

# 10. Create a Series containing five product ratings.
ratings = pd.Series(
    [4.5, 4.2, 4.8, 4.0, 4.6],
    index=["Laptop", "Phone", "TV", "Mouse", "Keyboard"]
)
print(ratings)

# 11. Access the marks of Aisha.
marks = pd.Series([85, 90, 78], index=["Aisha", "Rahul", "Sana"])
print(marks["Aisha"])

# 12. Access the salary of Rahul.
salary = pd.Series([25000, 30000, 35000], index=["Aisha", "Rahul", "Sana"])
print(salary["Rahul"])

# 13. Print the value associated with the third index.
cities = pd.Series(
    ["Bangalore", "Mumbai", "Delhi", "Chennai", "Kochi"],
    index=["c1", "c2", "c3", "c4", "c5"]
)
print(cities.iloc[2])

# 14. Access the first element using iloc.
s = pd.Series([100, 200, 300, 400, 500])
print(s.iloc[0])

# 15. Access the third element using iloc.
s = pd.Series([15, 25, 35, 45, 55])
print(s.iloc[2])

# 16. Print the first and last elements using positional indexing.
marks = pd.Series([85, 90, 78, 95, 88])
print(marks.iloc[0])
print(marks.iloc[-1])

# 17. Access the price of a specific product using custom index.
prices = pd.Series([50000, 30000, 20000], index=["Laptop", "Phone", "Tablet"])
print(prices["Laptop"])

# 18. Access the information of the fourth employee.
employees = pd.Series(
    ["Aisha", "Rahul", "Sana", "John", "Priya"],
    index=["e1", "e2", "e3", "e4", "e5"]
)
print(employees.iloc[3])

# 19. Print the second and fourth elements using iloc.
s = pd.Series([12, 24, 36, 48, 60])
print(s.iloc[1])
print(s.iloc[3])

# 20. Access Mathematics marks.
subjects = pd.Series([95, 90, 88], index=["Mathematics", "Science", "English"])
print(subjects["Mathematics"])

# 21. Add 5 to every element.
s = pd.Series([10, 20, 30, 40, 50])
print(s + 5)

# 22. Subtract 20 from every element.
s = pd.Series([100, 200, 300, 400, 500])
print(s - 20)

# 23. Multiply every element by 2.
s = pd.Series([10, 20, 30, 40, 50])
print(s * 2)

# 24. Divide every element by 10.
s = pd.Series([100, 200, 300, 400, 500])
print(s / 10)

# 25. Find maximum mark.
marks = pd.Series([85, 90, 78, 95, 88])
print(marks.max())

# 26. Find minimum salary.
salary = pd.Series([25000, 30000, 35000, 40000])
print(salary.min())

# 27. Calculate average using mean().
s = pd.Series([45, 67, 89, 90, 76])
print(s.mean())

# 28. Calculate total using sum().
s = pd.Series([10, 20, 30, 40, 50])
print(s.sum())

# 29. Find maximum and minimum prices.
prices = pd.Series([100, 250, 300, 450, 500])
print(prices.max())
print(prices.min())

# 30. Perform addition, multiplication and maximum-value operations.
marks = pd.Series([85, 90, 78, 95, 88])
print(marks + 5)
print(marks * 2)
print(marks.max())

# 31. Create a student DataFrame.
data = {
    "name":["Aisha","Rahul","Sana","John","Priya"],
    "age":[21,22,23,24,25],
    "marks":[85,90,78,95,88]
}
df = pd.DataFrame(data)
print(df)

# 32. Employee DataFrame.
data = {
    "employee_name":["Aisha","Rahul","Sana","John","Priya"],
    "department":["HR","IT","Finance","Sales","Marketing"],
    "salary":[25000,30000,35000,40000,45000]
}
df = pd.DataFrame(data)
print(df)

# 33. Product DataFrame.
data = {
    "product_name":["Pen","Book","Bag","Bottle","Pencil"],
    "price":[10,50,500,100,5],
    "quantity":[100,50,20,75,200]
}
df = pd.DataFrame(data)
print(df)

# 34. City DataFrame.
data = {
    "city_name":["Bangalore","Mumbai","Delhi","Chennai","Kochi"],
    "state":["KA","MH","DL","TN","KL"],
    "population":[1000000,900000,1200000,800000,700000]
}
df = pd.DataFrame(data)
print(df)

# 35. Student marks DataFrame.
data = {
    "name":["Aisha","Rahul","Sana","John","Priya"],
    "python_marks":[90,85,88,92,80],
    "java_marks":[88,84,90,86,82]
}
df = pd.DataFrame(data)
print(df)

# 36. Employee DataFrame.
data = {
    "name":["Aisha","Rahul","Sana","John","Priya"],
    "age":[25,28,27,30,26],
    "experience":[2,4,3,5,2]
}
df = pd.DataFrame(data)
print(df)

# 37. Mobile phones DataFrame.
data = {
    "brand":["Samsung","Apple","Vivo","Oppo","OnePlus"],
    "model":["A54","iPhone15","V29","F25","12R"],
    "price":[25000,70000,30000,28000,40000]
}
df = pd.DataFrame(data)
print(df)

# 38. Books DataFrame.
data = {
    "book_name":["Book1","Book2","Book3","Book4","Book5"],
    "author":["A","B","C","D","E"],
    "price":[200,250,300,350,400]
}
df = pd.DataFrame(data)
print(df)

# 39. Students and courses DataFrame.
data = {
    "name":["Aisha","Rahul","Sana","John","Priya"],
    "course":["BCA","BCom","BSc","BBA","BCA"],
    "joining_year":[2023,2022,2024,2023,2022]
}
df = pd.DataFrame(data)
print(df)

# 40. Customer DataFrame.
data = {
    "customer_name":["A","B","C","D","E"],
    "age":[21,25,28,23,30],
    "city":["Bangalore","Mumbai","Delhi","Chennai","Kochi"]
}
df = pd.DataFrame(data)
print(df)

# 41. Print only name column.
print(df["customer_name"])

# 42. Print only salary column.
employee_df = pd.DataFrame({
    "employee_name":["Aisha","Rahul"],
    "salary":[25000,30000]
})
print(employee_df["salary"])

# 43. Print only product_name column.
product_df = pd.DataFrame({
    "product_name":["Pen","Book","Bag"]
})
print(product_df["product_name"])

# 44. Print name and age columns together.
student_df = pd.DataFrame({
    "name":["Aisha","Rahul"],
    "age":[21,22]
})
print(student_df[["name","age"]])

# 45. Print employee_name and department.
employee_df = pd.DataFrame({
    "employee_name":["Aisha","Rahul"],
    "department":["HR","IT"]
})
print(employee_df[["employee_name","department"]])

# 46. Print product_name and price.
product_df = pd.DataFrame({
    "product_name":["Pen","Book"],
    "price":[10,50]
})
print(product_df[["product_name","price"]])

# 47. Access marks column.
student_df = pd.DataFrame({
    "name":["Aisha","Rahul"],
    "marks":[85,90]
})
print(student_df["marks"])

# 48. Access age and experience.
employee_df = pd.DataFrame({
    "age":[25,30],
    "experience":[2,5]
})
print(employee_df[["age","experience"]])

# 49. Access name and python_marks.
student_df = pd.DataFrame({
    "name":["Aisha","Rahul"],
    "python_marks":[90,85]
})
print(student_df[["name","python_marks"]])

# 50. Access brand and price.
product_df = pd.DataFrame({
    "brand":["Samsung","Apple"],
    "price":[25000,70000]
})
print(product_df[["brand","price"]])