
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'kiwi': 12, 'apple': 3, 'orange': 29, 'date': 15}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending by value:", ascending)

print("Descending by value:", descending)

# 2. Add a Key to a Dictionary

my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print("Updated dictionary:", my_dict)

# 3. Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}

dic2 = {3: 30, 4: 40}

dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}

print("Merged dictionary:", merged_dict)

# 4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Enter a number: "))

squares = {x: x*x for x in range(1, n+1)}

print("Generated dictionary:", squares)

# 5. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

squares_dict = {x: x**2 for x in range(1, 16)}

print("Dictionary of squares from 1 to 15:")

print(squares_dict)

# Set excercise 

# 1. Create a Set

my_set = {'a', 'b', 'c', 'c'}

print("Created set:", my_set)

# 2. Iterate Over a Set

fruits = {"banana", "apple", "orange", "watermelon"}

print("Fruits in the set:")
for fruit in fruits:
    print(fruit)

# 3.  Add Member(s) to a Set

my_set = {"orange", "apple"}

my_set.add("cherry")

print("Set after adding one element:", my_set)

# 4. Write a Python program to remove item(s) from a given set.

my_set = {"apple", "banana", "cherry", "mango"}

my_set.remove("banana")  

my_set.discard("pineapple")  

print("Set after removals:", my_set)

# 5.  Remove an Item if Present in the Set

my_set = {"apple", "banana", "cherry"}

item_to_remove = "banana"

if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"'{item_to_remove}' has been removed.")
else:
    print(f"'{item_to_remove}' not found in the set.")

print("Updated set:", my_set)
