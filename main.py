```python
# Importing required libraries
import pandas as pd
import numpy as np

# Creating a dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
        'Age': [28, 24, 35, 32, 30],
        'City': ['New York', 'Paris', 'London', 'Berlin', 'Amsterdam']}
df = pd.DataFrame(data)

# Displaying the dataframe
print(df)

# Basic Data Processing

# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000, 90000]
print(df)

# Deleting a column
df = df.drop('Age', axis=1)
print(df)

# Renaming columns
df = df.rename(columns={'Name': 'Employee Name', 'City': 'Employee City', 'Salary': 'Employee Salary'})
print(df)

# Changing index of dataframe
df = df.set_index('Employee Name')
print(df)

# Data selection operations

# Selecting a column
print(df['Employee City'])

# Selecting multiple columns
print(df[['Employee City', 'Employee Salary']])

# Selecting rows by index
print(df.loc[['John', 'Linda']])

# Selecting rows by condition
print(df[df['Employee Salary'] > 60000])

# Data aggregation operations

# Finding maximum value
print(df['Employee Salary'].max())

# Finding minimum value
print(df['Employee Salary'].min())

# Finding mean value
print(df['Employee Salary'].mean())

# Finding median value
print(df['Employee Salary'].median())

# Data cleaning operations

# Checking for missing values
print(df.isnull().sum())

# Filling missing values
df['Employee Salary'] = df['Employee Salary'].fillna(df['Employee Salary'].mean())
print(df)

# Replacing values
df['Employee City'] = df['Employee City'].replace('London', 'Lisbon')
print(df)

# Data transformation operations

# Applying a function on column
df['Employee Salary'] = df['Employee Salary'].apply(lambda x: x*1.1)
print(df)

# Grouping data
grouped_data = df.groupby('Employee City')

# Aggregating grouped data
print(grouped_data['Employee Salary'].mean())

# Resetting index
df = df.reset_index()
print(df)
```
Цей код показує різні основні операції обробки даних, такі як створення, видалення, перейменування та вибір колонок та рядків, агрегацію даних, перевірку на наявність пропущених значень, заповнення пропущених значень, заміну значень, застосування функцій на колонці, групування даних, агрегацію групованих даних та скидання індексу.