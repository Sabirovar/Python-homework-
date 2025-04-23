# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero

try:
    
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    
    result = numerator / denominator
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers.")

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    
    user_input = input("Enter an integer: ")
    2
    number = int(user_input)
    
    print(f"You entered the integer: {number}")

except ValueError:
    print("Error: That is not a valid integer!")

    # 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist

try:
    
    filename = input("Enter the filename to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

   
    result = num1 + num2
    print(f"The sum is: {result}")

except ValueError:
    print("Error: You must enter valid numbers.")

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue

try:
    
    filename = input("Enter the filename to open: ")
    
    
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except PermissionError:
    print("Error: You don't have permission to access this file.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    
    my_list = [10, 20, 30, 40, 50]
    
    
    index = int(input("Enter the index of the element you want to access: "))
    
    
    element = my_list[index]
    print(f"The element at index {index} is {element}")

except IndexError:
    print("Error: The index is out of range. Please enter a valid index.")

except ValueError:
    print("Error: Please enter a valid integer for the index.")

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the inpu

try:
   
    number = float(input("Enter a number: "))
    print(f"You entered: {number}")

except KeyboardInterrupt:
    print("\nInput cancelled by the user.")

except ValueError:
    print("\nError: You must enter a valid number.")

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    
    result = numerator / denominator
    print(f"The result is: {result}")

except ArithmeticError:
    print("Arithmetic error occurred during division!")

except ValueError:
    print("Error: Please enter valid numbers.")

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    
    filename = input("Enter the filename to open: ")
    

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:\n", content)

except UnicodeDecodeError:
    print("Error: Cannot decode the file content. It might have a different encoding.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    
    my_list = [1, 2, 3, 4, 5]
    
   
    my_list.push(6)  

except AttributeError:
    print("Error: The list does not have that attribute or method.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# File Input/Output Exercises

# 1. Write a Python program to read an entire text file

filename = input("Enter the filename: ")

try:
    
    with open(filename, 'r', encoding='utf-8') as file:
        
        content = file.read()
       
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except UnicodeDecodeError:
    print("Error: Cannot read file due to encoding issues.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 2. Write a Python program to read first n lines of a file. 

filename = input("Enter the filename: ")
n = int(input("Enter how many lines you want to read: "))

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[:n]:
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


