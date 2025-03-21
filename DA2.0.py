import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 250)

### 1. Data Collection
# Load dataset
url = "https://github.com/Code-Gen-Hub/Data_Analytic_Workshop/raw/main/Employee%20Sample%20Data.xlsx"
df = pd.read_excel(url, engine='openpyxl')
print(df.head())
print(df.info())

### 2. Data Cleaning
# Show Missing Values Summary
print("\nMissing Values Summary:")
print(df.isnull().sum())

# Show each Missing Values row
print("\nRows with Missing Values:")
print(df[df.isnull().any(axis=1)])

# drop all Missing Values row
df = df.dropna()

print("\nCleaned Data:")
print(df.info())

### 3.1 Data Mining (Finding Average Salary by Department)
department_salary = df.groupby('Department')['Annual Salary'].mean().reset_index()
print("\nAverage Salary by Department:")
print(department_salary)

### 4.1 Data Visualization (Pie Chart of Average Salary by Department)
plt.figure(figsize=(8,8))
plt.title("Average Salary by Department")
plt.pie(department_salary['Annual Salary'], labels=department_salary['Department'], autopct='%1.1f%%')
plt.show()

### 3.2 Data Mining (Finding Average Age by Department)
department_age = df.groupby('Department')['Age'].mean().reset_index()
print("\nAverage Age by Department:")
print(department_age)

### 4.2 Data Visualization (Bar Chart of Average Age by Department)
plt.figure(figsize=(8,5))
plt.title("Average Age by Department")
plt.xlabel("Department")
plt.ylabel("Average Age")
plt.xticks(rotation=45)
plt.bar(department_age['Department'], department_age['Age'], color='skyblue')
plt.show()
