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
