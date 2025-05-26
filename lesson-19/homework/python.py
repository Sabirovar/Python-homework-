# 1.
def categorize(product):
    if 'Shoes' in product or 'Sneakers' in product:
        return 'Footwear'
    elif 'Shirt' in product or 'Dress' in product or 'Pants' in product or 'Jacket' in product or 'Skirt' in product or 'Sweater' in product or 'Hoodie' in product:
        return 'Apparel'
    elif 'Smart TV' in product or 'Laptop' in product or 'Tablet' in product or 'Smartphone' in product or 'Gaming Console' in product or 'Projector' in product or 'Drone' in product or 'Camera' in product:
        return 'Electronics'
    elif 'Wireless' in product or 'Bluetooth' in product or 'Speaker' in product or 'Headphones' in product:
        return 'Accessories'
    elif 'Backpack' in product or 'Desk' in product or 'Lamp' in product or 'Bookshelf' in product or 'Chair' in product or 'Table' in product:
        return 'Home/Office'
    elif 'Coffee Maker' in product or 'Toaster' in product or 'Cookware' in product or 'Comforter' in product or 'Iron' in product or 'Scale' in product:
        return 'Home Appliances'
    else:
        return 'Other'

# 2.

# === StackOverflow QA Homework ===
import pandas as pd

# Load StackOverflow dataset
df = pd.read_csv('task/stackoverflow_qa.csv')

# 1. Questions created before 2014
df_before_2014 = df[pd.to_datetime(df['creationdate']) < '2014-01-01']

# 2. Questions with score more than 50
df_score_gt_50 = df[df['score'] > 50]

# 3. Questions with score between 50 and 100
df_score_between_50_100 = df[df['score'].between(50, 100)]

# 4. Questions answered by Scott Boston
df_scott_boston = df[df['ans_name'] == 'Scott Boston']

# 5. Questions answered by specific 5 users
users = ['Scott Boston', 'unutbu', 'Demitri', 'Mike Pennington', 'doug']
df_answered_by_5 = df[df['ans_name'].isin(users)]

# 6. Questions created Mar 2014–Oct 2014, answered by Unutbu, score < 5
df_march_oct_unutbu = df[(df['ans_name'] == 'unutbu') &
                         (df['score'] < 5) &
                         (pd.to_datetime(df['creationdate']).between('2014-03-01', '2014-10-31'))]

# 7. Score between 5 and 10 or viewcount > 10000
df_score_or_view = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]

# 8. Questions NOT answered by Scott Boston
df_not_scott_boston = df[df['ans_name'] != 'Scott Boston']


# === Titanic Homework ===
titanic_df = pd.read_csv('task/titanic.csv')

# 1. Female passengers in Class 1 aged 20-30
female_class1_20_30 = titanic_df[(titanic_df['Sex'] == 'female') &
                                 (titanic_df['Pclass'] == 1) &
                                 (titanic_df['Age'].between(20, 30))]

# 2. Passengers who paid > $100
fare_gt_100 = titanic_df[titanic_df['Fare'] > 100]

# 3. Survived and were alone
survived_alone = titanic_df[(titanic_df['Survived'] == 1) &
                            (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)]

# 4. Embarked from 'C' and paid > $50
embarked_c_fare_gt_50 = titanic_df[(titanic_df['Embarked'] == 'C') &
                                   (titanic_df['Fare'] > 50)]

# 5. Had both siblings/spouses and parents/children
df_sibsp_parch = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]

# 6. Aged <= 15 and did not survive
kids_didnt_survive = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]

# 7. Known cabin and fare > $200
cabin_fare_gt_200 = titanic_df[titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)]

# 8. Odd-numbered PassengerIds
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# 9. Unique ticket numbers
ticket_counts = titanic_df['Ticket'].value_counts()
unique_ticket_df = titanic_df[titanic_df['Ticket'].isin(ticket_counts[ticket_counts == 1].index)]

# 10. 'Miss' in name and Class 1
miss_class1 = titanic_df[(titanic_df['Name'].str.contains('Miss')) & (titanic_df['Pclass'] == 1)]


# === Customer Orders Homework ===
customer_df = pd.read_csv("task/customer_orders.csv")

# 1. Customers with 20 or more orders
customer_order_counts = customer_df.groupby('CustomerID')['OrderID'].count()
frequent_customers = customer_order_counts[customer_order_counts >= 20].index
filtered_customers_df = customer_df[customer_df['CustomerID'].isin(frequent_customers)]

# 2. Customers who ordered products with avg price > $120
customer_avg_price = customer_df.groupby('CustomerID')['Price'].mean()
high_price_customers = customer_avg_price[customer_avg_price > 120].index
avg_price_filtered_df = customer_df[customer_df['CustomerID'].isin(high_price_customers)]

# 3. Total quantity and total price per product, filter by quantity >= 5
product_stats = customer_df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': 'mean'
})
product_stats['TotalPrice'] = product_stats['Quantity'] * product_stats['Price']
filtered_products = product_stats[product_stats['Quantity'] >= 5]

import pandas as pd
import numpy as np

# Пример генерации данных
np.random.seed(42)
states = ['California', 'Texas', 'Florida', 'New York', 'Illinois']
num_records = 1000

# Создание DataFrame
data = {
    'PersonID': range(1, num_records + 1),
    'State': np.random.choice(states, num_records),
    'Salary': np.random.randint(50000, 2000000, size=num_records)
}
df = pd.DataFrame(data)

# Категории Salary Band
salary_bins = [
    0, 200000, 400000, 600000, 800000, 1000000,
    1200000, 1400000, 1600000, 1800000, float('inf')
]
salary_labels = [
    "till $200,000", "$200,001 - $400,000", "$400,001 - $600,000", "$600,001 - $800,000",
    "$800,001 - $1,000,000", "$1,000,001 - $1,200,000", "$1,200,001 - $1,400,000",
    "$1,400,001 - $1,600,000", "$1,600,001 - $1,800,000", "$1,800,001 and over"
]

# Добавление категории зарплаты
df['Salary Band'] = pd.cut(df['Salary'], bins=salary_bins, labels=salary_labels, right=True)

# Группировка по Salary Band
summary = df.groupby('Salary Band').agg(
    Number_of_population=('PersonID', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()


total = len(df)
summary['Percentage'] = (summary['Number_of_population'] / total) * 100


summary = summary[['Salary Band', 'Percentage', 'Average_Salary', 'Median_Salary', 'Number_of_population']]
summary = summary.round({'Percentage': 2, 'Average_Salary': 2, 'Median_Salary': 2})

print(summary)
