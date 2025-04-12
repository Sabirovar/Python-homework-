# 1. Create and Access List Elements

fruit = ['banana', 'apple', 'watermelon', 'orange', 'peach']

print(fruit)

print("The third fruit is:", fruit[2])

#2. Create two lists of numbers and concatenate them into a single list.

list1 = [7,8,9]

list2 = [1,2,3]

combined_list = list1 + list2

print("Combined list:", combined_list)

# 3. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers = [1,2,3,10,15,5]

first = (numbers[0])

middle_index = len(numbers) // 2
middle = numbers[middle_index]

last = numbers[-1]

result = [first, middle, last]

print("New list:", result)

# 4. Create a list of your five favorite movies and convert it into a tuple.

favorite_movies = ["lalaland", "dekster", "interstellar", "the lawyer", "1+1"]

movies_tuple = tuple(favorite_movies)

print("List:", favorite_movies)
print("Tuple:", movies_tuple)

# 5.Given a list of cities, check if "Paris" is in the list and print the result.

cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]
if "Paris" in cities:
 print("Paris is in the list.")
else:
 print("Paris is not in the list.")

# 6. Create a list of numbers and duplicate it without using loops.

numbers = [1, 2, 3, 4, 5]

duplicated = numbers * 2

print("Duplicated list:", duplicated)

# 7. Given a list of numbers, swap the first and last elements.

numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping:", numbers)

# 8. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers = tuple(range(1, 11))

slice_result = numbers[3:7]

print("Slice from index 3 to 7:", slice_result)

# 9. Create a list of colors and count how many times "blue" appears in the list.

colors = ['blue', 'red', 'orange', 'pink', 'blue', 'black']

count_blue = colors.count('blue')

print("The color 'blue' appears", count_blue, "times.")

# 10. Given a tuple of animals, find the index of "lion"

animals = ("cat", "dog", "lion", "tiger", "elephant")

lion_index = animals.index("lion")

print("Index of 'lion':", lion_index)

# 11. Create two tuples of numbers and merge them into a single tuple.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print("Merged tuple:", merged_tuple)

# 12. Given a list and a tuple, find and print their lengths.

my_list = [16, 25, 30, 45, 50]
my_tuple = (1, 2, 3, 4)

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

# 13. Create a tuple of five numbers and convert it into a list.

my_tuple = (10, 20, 30, 40, 50)

my_list = list(my_tuple)

print("Original tuple:", my_tuple)
print("Converted list:", my_list)

# 14. Given a tuple of numbers, find and print the maximum and minimum values.

numbers = (7, 1, 3, 55, 8, 12)


maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)

# 15. Create a tuple of words and print it in reverse order.

words = ("apple", "banana", "cherry", "date", "fig")

reversed_words = words[::-1]

print("Reversed tuple:", reversed_words)
