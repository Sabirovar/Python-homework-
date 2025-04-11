# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - year_of_birth

print(f"Name: {name}")
print(f"Year of birth: {year_of_birth}")
print(f"Current age: {age}")

# 2. Extract Car Names
# Extract car names from the following text:

txt = "LMaasleitbtui"

car1 = txt[0::2]
car2 = txt[1::2]

print(f"Car 1: {car1}")
print(f"Car 2: {car2}")

# 3. Extract Car Names
# Extract car names from the following text:

txt = 'MsaatmiazD'

car1 = txt[0::2]
car2 = txt[::-2]

print(f"Car 1: {car1}")
print(f"Car 2: {car2}")

# 4. Extract Residence Area
# Extract the residence area from the following text:

txt = "I'am John. I am from London"

splitted_text = txt.split(" ")

print(splitted_text)

print(f"Residence area: {splitted_text[len(splitted_text)-1]}")

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

txt = input("Enter your text: ")

reversed_txt = txt[::-1]

print(f"Reversed Text: {reversed_txt}")

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string. 

txt = input("Enter your value: ")

vowel_count = (
txt.count("a") + txt.count("e") + txt.count("i") + txt.count("o") + txt.count("u")
)
print("Vowel count:", vowel_count)

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

values_string = input("Enter values: ")
values = values_string.split(',')

max_value = 0

for i in values:
if float(i) > max_value:
max_value = float(i)
print(f"Max value: {max_value}")

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Enter a word: ")

if word == word[::-1]:
    print("Is Palindrome")
else:
    print("Not a palindrome")

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Enter your email: ")

splitted_email = email.split("@")
domain = splitted_email[1]

print(f"Domain: {domain}")

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

length = 12

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
