# 1. Leep year

def is_leap_year(year):

    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    print("Leap Year Checker")
    while True:
        user_input = input("Enter a year (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting. Goodbye!")
            break
        try:
            year = int(user_input)
            if is_leap_year(year):
                print(f"✅ {year} is a leap year.\n")
            else:
                print(f"❌ {year} is NOT a leap year.\n")
        except ValueError as ve:
            print(f"Error: {ve}\n")

if __name__ == "__main__":
    main()

# 2. Conditional Statements Exercise

def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
n = int(input("Enter a number: "))
check_weird(n)

# 2.  

a = int(input("Enter a: "))
b = int(input("Enter b: "))


if a > b:
    a, b = b, a


if a % 2 != 0:
    a += 1  

even_numbers = list(range(a, b + 1, 2))
print("Even numbers:", even_numbers)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

even_numbers = list(range(min(a, b) + (min(a, b) % 2), max(a, b) + 1, 2))
print("Even numbers:", even_numbers)

# 3. 
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    a, b = b, a
if a % 2 != 0:
    a += 1
even_numbers = list(range(a, b + 1, 2))
print("Even numbers:", even_numbers)





       
