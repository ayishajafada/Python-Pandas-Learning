import pandas as pd

data = {
    'Name': ['Asha', 'Rahul', 'Priya', 'John', 'Sneha', 'Arun'],
    'Age': [22, 25, 21, 28, 24, 26],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [25000, 40000, 35000, 50000, 30000, 45000],
    'City': ['Bangalore', 'Mysore', 'Bangalore', 'Chennai', 'Mysore', 'Bangalore']
}

df = pd.DataFrame(data)

print(df)


# Display only the Name column.
print(df["Name"])

# Display Name and Department columns.
print(df[["Name", "Department"]])

# Display the first three rows.
print(df.head(3))

# Display the last two rows using iloc.
print(df.iloc[-2:])

# Display the complete record of Rahul using loc.
print(df.loc[df["Name"] == "Rahul"])

# Display the Age of Priya.
print(df.loc[df["Name"] == "Priya", "Age"])

# Display rows from index 1 to 4 using loc.
print(df.loc[1:4])

# Display the first four rows and first two columns using iloc.
print(df.iloc[0:4, 0:2])

# Display the Name and Salary of employees at index 2 and 4.
print(df.loc[[2, 4], ["Name", "Salary"]])

# Display the complete record of John.
print(df.loc[df["Name"] == "John"])


# Find employees whose age is greater than 24.
print(df[df["Age"] > 24])

# Find employees whose salary is less than 40,000.
print(df[df["Salary"] < 40000])

# Find employees working in HR.
print(df[df["Department"] == "HR"])

# Find employees living in Mysore.
print(df[df["City"] == "Mysore"])

# Find employees whose salary is greater than or equal to 35,000.
print(df[df["Salary"] >= 35000])

# Find employees working in IT with a salary greater than 40,000.
print(df[(df["Department"] == "IT") & (df["Salary"] > 40000)])

# Find employees who live in Bangalore or Chennai.
print(df[(df["City"] == "Bangalore") | (df["City"] == "Chennai")])

# Find employees whose age is between 22 and 26.
print(df[(df["Age"] >= 22) & (df["Age"] <= 26)])

# Find employees who are not working in HR.
print(df[df["Department"] != "HR"])

# Find employees whose names contain the letter 'a'.
print(df[df["Name"].str.contains("a", case=False)])