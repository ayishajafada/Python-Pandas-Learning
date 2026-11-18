#Pandas Assignment: 50 Questions
#Section A: Creating a Series (1–15)

#create a Series containing the marks [80, 85, 90, 95, 88].

import pandas as pd
marks=pd.Series([80,85,90,95,88])
print(marks)

#Create a Series containing the ages [18, 19, 20, 21, 22] and print it.

age=pd.Series([18,19,20,21,22])
print(age)

#Create a Series containing the numbers [10, 20, 30, 40, 50]
numbers=pd.Series([10,20,30,40,50])
print(numbers)

#Create a Series containing the prices [100, 250, 350, 450, 500].

prices=pd.Series([100, 250, 350, 450, 500])
print(prices)

#Create a Series containing the temperatures [25, 28, 30, 32, 27].

temperatures=pd.Series([25,28,30,32,27])
print(temperatures)

#Create a Series containing the values [12.5, 15.5, 18.5, 20.5].

values=pd.Series([12.5, 15.5, 18.5, 20.5])
print(values)

#Create a Series containing the names ["Aisha", "Rahul", "Sana", "Arjun"].

names=pd.Series(["Aisha", "Rahul", "Sana", "Arjun"])
print(names)

#Create a Series containing the subjects ["Python", "Java", "SQL", "Pandas"].
subjects=pd.Series(["Python", "Java", "SQL", "Pandas"])
print(subjects)

##Create a Series containing the values [100, 200, 300] and print it.
values=pd.Series([100,200,300])
print(values)

#Create a Series containing the numbers [5, 10, 15, 20, 25, 30].
numbers = pd.Series([5,10,15,20,25,30])
print(numbers)

#Create a Series containing the employee salaries [25000, 30000, 35000, 40000].
salaries=pd.Series([25000,30000,35000,40000])
print(salaries)
print(type(pd.Series))
#Create a Series containing the percentages [75.5, 82.5, 91.0, 68.5].

percentage=pd.Series([75.5, 82.5, 91.0, 68.5])
print(percentage)

#Create a Series containing the quantities [12, 24, 36, 48, 60].

quantities=pd.Series([12, 24, 36, 48, 60])
print(quantities)

#Create a Series containing the values [True, False, True, False].
values=pd.Series([True, False, True, False])
print(values)

#Create a Series containing the following city names: "Bangalore", "Mumbai", "Delhi", and "Chennai".
city_names=pd.Series(["Bangalore","Mumbai","Delhi","Chennai"])
print(city_names)

#Section B: Series with Custom Indexes (16–25)
# Create a Series containing the marks [85, 90, 78] with the custom indexes ["Aisha", "Rahul", "Sana"].

marks=pd.Series([85, 90, 78],index=["ayisha","rahul","sana"])
print(marks)

#Create a Series containing the ages [21, 22, 23] with the custom indexes ["Student1", "Student2", "Student3"].

ages=pd.Series([21,22,23],index=["Student1","student2","Student3"])
print(ages)

#Create a Series containing the salaries [25000, 30000, 45000] with the custom indexes ["Employee_A", "Employee_B", "Employee_C"].
salaries=pd.Series([25000,30000,45000],index=["Employee_A","Employee_B","Employee_C"])
print(salaries)

#Create a Series containing the prices [100, 200, 300, 400] with the custom indexes ["Pen", "Book", "Bag", "Bottle"].

prices=pd.Series([100,200,300,400],["Pen","Book","Bag","Bottle"])
print(prices)

#Create a Series containing the scores [70, 80, 90, 95] with the custom indexes ["Python", "Java", "SQL", "Pandas"].
scores=pd.Series([70,80,90,95],index=["Python","Java","SQL","Pandas"])
print(scores)

#Create a Series containing the values [10, 20, 30] with the custom indexes ["A", "B", "C"].

values=pd.Series([10,20,30],index=["A","B","C"])
print(values)

#Create a Series containing the quantities [5, 10, 15, 20] with the custom indexes ["Monday", "Tuesday", "Wednesday", "Thursday"].

quantities=pd.Series([5,10,15,20],index=["Monday","Tuesday","Wednesday","Thursday"])
print(quantities)

# Create a Series containing the temperatures [28, 30, 32] with the custom indexes ["Morning", "Afternoon", "Evening"].

temperatures = pd.Series([28, 30, 32], index=["Morning", "Afternoon", "Evening"])
print(temperatures)


# Create a Series containing the marks [88, 76, 92, 81] with the custom indexes ["Aisha", "Rahul", "Sana", "Arjun"].

marks = pd.Series([88, 76, 92, 81], index=["Aisha", "Rahul", "Sana", "Arjun"])
print(marks)


# Create a Series containing the values [500, 1000, 1500] with the custom indexes ["Product_A", "Product_B", "Product_C"].

values = pd.Series([500, 1000, 1500], index=["Product_A", "Product_B", "Product_C"])
print(values)


# Section C: Accessing Values Using Custom Indexes (26–35)

# Create a Series containing marks [85, 90, 78] with indexes ["Aisha", "Rahul", "Sana"]. Print Aisha's marks.

marks = pd.Series([85, 90, 78], index=["Aisha", "Rahul", "Sana"])
print(marks["Aisha"])


# Using the same Series structure, print Rahul's marks.

marks = pd.Series([85, 90, 78], index=["Aisha", "Rahul", "Sana"])
print(marks["Rahul"])


# Create a Series containing ages [21, 22, 23] with indexes ["Aisha", "Rahul", "Sana"]. Print Sana's age.

ages = pd.Series([21, 22, 23], index=["Aisha", "Rahul", "Sana"])
print(ages["Sana"])


# Create a Series containing prices [100, 200, 300] with indexes ["Pen", "Book", "Bag"]. Print the price of the Book.

prices = pd.Series([100, 200, 300], index=["Pen", "Book", "Bag"])
print(prices["Book"])


# Create a Series containing salaries [25000, 35000, 45000] with indexes ["Employee_A", "Employee_B", "Employee_C"]. Print Employee_C's salary.

salaries = pd.Series([25000, 35000, 45000], index=["Employee_A", "Employee_B", "Employee_C"])
print(salaries["Employee_C"])


# Create a Series containing scores [70, 80, 90, 95] with indexes ["Python", "Java", "SQL", "Pandas"]. Print the SQL score.

scores = pd.Series([70, 80, 90, 95], index=["Python", "Java", "SQL", "Pandas"])
print(scores["SQL"])


# Create a Series containing quantities [10, 20, 30] with indexes ["Product_A", "Product_B", "Product_C"]. Print the quantity of Product_A.

quantities = pd.Series([10, 20, 30], index=["Product_A", "Product_B", "Product_C"])
print(quantities["Product_A"])


# Create a Series containing temperatures [25, 30, 35] with indexes ["Morning", "Afternoon", "Evening"]. Print the evening temperature.

temperatures = pd.Series([25, 30, 35], index=["Morning", "Afternoon", "Evening"])
print(temperatures["Evening"])


# Create a Series containing marks [75, 85, 95] with indexes ["Student_A", "Student_B", "Student_C"]. Print Student_B's marks.

marks = pd.Series([75, 85, 95], index=["Student_A", "Student_B", "Student_C"])
print(marks["Student_B"])


# Create a Series containing prices [150, 250, 350, 450] with indexes ["Pen", "Notebook", "Bag", "Bottle"]. Print the prices of the Pen and Bottle separately.

prices = pd.Series([150, 250, 350, 450], index=["Pen", "Notebook", "Bag", "Bottle"])

print(prices["Pen"])
print(prices["Bottle"])

#Section D: Creating DataFrames (36–45),For these questions, create DataFrames using a Python dictionary and pd.DataFrame().

#Create a DataFrame containing three columns: name, age, and marks. Add records for Aisha, Rahul, and Sana.

data={
    "name":["ayisha","rahul","sana"],
    "age":[22,23,24],
    "marks":[87,98,86]
}

df=pd.DataFrame(data)
print(df)

#Create a DataFrame containing the columns name, age, and city for four students.

data={
    "name":["ayisha","sneha","hamda"],
    "age":[23,25,22],
    "city":["Bangalore","Mumbai","Kochi"]
}

df=pd.DataFrame(data)
print(df)

# Create a DataFrame containing the columns employee_name, salary, and department for three employees.

data = {
    "employee_name": ["Aisha", "Rahul", "Sana"],
    "salary": [25000, 30000, 35000],
    "department": ["HR", "IT", "Finance"]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns product, price, and quantity for four products.

data = {
    "product": ["Pen", "Book", "Bag", "Bottle"],
    "price": [10, 200, 500, 150],
    "quantity": [100, 50, 25, 75]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns student_name, python_marks, and java_marks for three students.

data = {
    "student_name": ["Aisha", "Rahul", "Sana"],
    "python_marks": [85, 90, 88],
    "java_marks": [80, 86, 92]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns name, age, and course for five students.

data = {
    "name": ["Aisha", "Rahul", "Sana", "Arjun", "Sneha"],
    "age": [21, 22, 20, 23, 22],
    "course": ["BCA", "BCom", "BSc", "BCA", "BBA"]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns subject, total_marks, and passing_marks for four subjects.

data = {
    "subject": ["Python", "Java", "SQL", "Pandas"],
    "total_marks": [100, 100, 100, 100],
    "passing_marks": [40, 40, 40, 40]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns city, temperature, and humidity for three cities.

data = {
    "city": ["Bangalore", "Mumbai", "Kochi"],
    "temperature": [28, 32, 30],
    "humidity": [65, 80, 75]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns employee_id, employee_name, and salary for four employees.

data = {
    "employee_id": [101, 102, 103, 104],
    "employee_name": ["Aisha", "Rahul", "Sana", "Arjun"],
    "salary": [25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns product_name, price, and category for five products.

data = {
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "price": [50000, 500, 1200, 10000, 8000],
    "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"]
}

df = pd.DataFrame(data)
print(df)

#Section E: Combined Practice (46–50)
#Create a Series containing the marks [85, 90, 78, 95] with custom indexes ["Aisha", "Rahul", "Sana", "Arjun"].

marks=pd.Series([85,90,78,95],index=["ayisha","rahul","sana","arjun"])
print(marks)
print(marks["arjun"])

# Create a DataFrame containing the columns name, age, and marks for four students. Print the complete DataFrame.

data = {
    "name": ["Aisha", "Rahul", "Sana", "Arjun"],
    "age": [21, 22, 20, 23],
    "marks": [87, 90, 78, 85]
}

df = pd.DataFrame(data)
print(df)


# Create a DataFrame containing the columns employee_name, department, and salary for five employees. Print the DataFrame.

data = {
    "employee_name": ["Aisha", "Rahul", "Sana", "Arjun", "Zoya"],
    "department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "salary": [25000, 30000, 35000, 40000, 45000]
}

df = pd.DataFrame(data)
print(df)


# Create a Series containing the prices [100, 250, 350, 450] with custom indexes ["Pen", "Book", "Bag", "Bottle"].
# Print the Series and then print the price of the Bag.

prices = pd.Series(
    [100, 250, 350, 450],
    index=["Pen", "Book", "Bag", "Bottle"]
)

print(prices)
print(prices["Bag"])


# Create a DataFrame containing the columns student_name, age, and marks for five students.
# Names: Aisha, Rahul, Sana, Arjun, Zoya
# Ages: 21, 22, 20, 23, 21
# Marks: 87, 90, 78, 67, 95
# Print the complete DataFrame.

data = {
    "student_name": ["Aisha", "Rahul", "Sana", "Arjun", "Zoya"],
    "age": [21, 22, 20, 23, 21],
    "marks": [87, 90, 78, 67, 95]
}

df = pd.DataFrame(data)
print(df)