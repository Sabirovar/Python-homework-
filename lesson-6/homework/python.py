# 1. Modify String with Underscores

def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0
    count = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == "_"):
                i += 1
                if i < len(txt):
                    result.append(txt[i])
            if i + 1 < len(txt): 
                result.append("_")
            count = 0
        i += 1

    return ''.join(result)

print(insert_underscores("hello"))           
print(insert_underscores("assalom"))         
print(insert_underscores("abcabcabcdeabcdefabcdefg")) 

# 2. Task The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input())

for i in range(n):
    print(i ** 2)

# 3. Exercise 1: Print first 10 natural numbers using a while loop

i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print the following pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given numb 

n = int(input("Enter number: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum is:", total)

# Exercise 4: Print multiplication table of a given number

num = int(input("Enter number: "))

i = 1
while i <= 10:
    print(num * i)
    i += 1

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0 and num < 200:
        print(num)

# Exercise 5: Count the total number of digits in a number

num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)

# Exercise 7: Print reverse number pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution

for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Print all prime numbers within a range

for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


# Exercise 12: Display Fibonacci series up to 10 terms

n1, n2 = 0, 1
count = 0

while count < 10:
    print(n1, end=" ")
    nth = n1 + n2
    n1, n2 = n2, nth
    count += 1

# Exercise 13: Find the factorial of a given number

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print(f"{num}! = {fact}")


# 4. Return Uncommon Elements of Lists

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)

    
    diff1 = c1 - c2  
    diff2 = c2 - c1  

    result = list(diff1.elements()) + list(diff2.elements())
    return result
