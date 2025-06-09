#lesson 17

import pandas as pd
import numpy as np

# Step 1: Create the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Step 2: Rename columns using a function
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# Step 3: Print first 3 rows
print("First 3 rows:\n", df.head(3))

# Step 4: Find mean age
mean_age = df["age"].mean()
print("Mean age:", mean_age)

# Step 5: Select and print only 'first_name' and 'city'
print("Selected columns:\n", df[["first_name", "city"]])

# Step 6: Add random salary column
df["salary"] = np.random.randint(50000, 100000, size=len(df))

# Step 7: Summary statistics
print("Summary statistics:\n", df.describe())


Homework 2: Sales and Expenses Analysis
python
Копировать
Редактировать
# Create the DataFrame
sales_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)

# Calculate maximum
print("Max Sales:", sales_and_expenses["Sales"].max())
print("Max Expenses:", sales_and_expenses["Expenses"].max())

# Calculate minimum
print("Min Sales:", sales_and_expenses["Sales"].min())
print("Min Expenses:", sales_and_expenses["Expenses"].min())

# Calculate average
print("Average Sales:", sales_and_expenses["Sales"].mean())
print("Average Expenses:", sales_and_expenses["Expenses"].mean())
✅ Homework 3: Monthly Category-wise Expenses
python
Копировать
Редактировать
# Create the DataFrame
expenses_data = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expenses_data)

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# Maximum expense per category
print("Max expense per category:\n", expenses.max(axis=1))

# Minimum expense per category
print("Min expense per category:\n", expenses.min(axis=1))

# Average expense per category
print("Average expense per category:\n", expenses.mean(axis=1))
