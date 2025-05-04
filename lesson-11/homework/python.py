# === math_operations.py ===
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")


# === string_utils.py ===
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')


# === geometry/__init__.py ===
# This file can be left empty or used to expose package functionality


# === geometry/circle.py ===
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


# === file_operations/__init__.py ===
# This file can be left empty or used to expose package functionality


# === file_operations/file_reader.py ===
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# === file_operations/file_writer.py ===
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
