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

# lesson 20

import pandas as pd
import sqlite3

# Connect to the chinook database
conn = sqlite3.connect("chinook.db")

✅ Part 1: Customer Purchases Analysis
1️⃣ Total amount spent by each customer
python
Копировать
Редактировать
query = """
SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, SUM(i.Total) AS TotalSpent
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
"""

df_total_spent = pd.read_sql(query, conn)
print(df_total_spent.head())
2️⃣ Top 5 customers by purchase amount
python
Копировать
Редактировать
top5_customers = df_total_spent.head(5)
print("Top 5 Customers:\n", top5_customers)
✅ Part 2: Album vs Individual Track Purchases
To analyze customer preference, we need to determine whether a customer purchased:

All tracks of an album (considered album purchase), or

Only a subset (considered individual tracks).

Step-by-step:
1️⃣ Get album-track mappings
python
Копировать
Редактировать
album_tracks = pd.read_sql("""
SELECT a.AlbumId, t.TrackId
FROM Album a
JOIN Track t ON a.AlbumId = t.AlbumId
""", conn)
2️⃣ Get customer track purchases
python
Копировать
Редактировать
purchases = pd.read_sql("""
SELECT DISTINCT i.CustomerId, il.TrackId
FROM InvoiceLine il
JOIN Invoice i ON il.InvoiceId = i.InvoiceId
""", conn)
3️⃣ Merge purchase data with album info
python
Копировать
Редактировать
purchases_with_album = purchases.merge(album_tracks, on="TrackId")
4️⃣ Group and compare
python
Копировать
Редактировать
# Count how many tracks exist per album
album_track_counts = album_tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

# Count how many tracks each customer bought per album
customer_album_track_counts = purchases_with_album.groupby(["CustomerId", "AlbumId"])["TrackId"].count().reset_index()
customer_album_track_counts.rename(columns={"TrackId": "TracksBought"}, inplace=True)

# Merge with total available tracks per album
merged = customer_album_track_counts.merge(album_track_counts, on="AlbumId")

# Determine full album purchases
merged["FullAlbum"] = merged["TracksBought"] == merged["TotalTracks"]
5️⃣ Analyze preferences
python
Копировать
Редактировать
# Group by customer and check if they purchased any full album
customer_preferences = merged.groupby("CustomerId")["FullAlbum"].any().reset_index()
customer_preferences["Preference"] = customer_preferences["FullAlbum"].map(lambda x: "Full Album" if x else "Individual Tracks")

# Summary
summary = customer_preferences["Preference"].value_counts(normalize=True) * 100
print("Customer Preference Summary (%):\n", summary)
