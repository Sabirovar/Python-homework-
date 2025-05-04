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


# === threaded_prime_checker.py ===
import threading

primes = []
lock = threading.Lock()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end):
    local_primes = [n for n in range(start, end) if is_prime(n)]
    with lock:
        primes.extend(local_primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    chunk_size = (end - start) // num_threads
    for i in range(num_threads):
        sub_start = start + i * chunk_size
        sub_end = start + (i + 1) * chunk_size if i != num_threads - 1 else end
        thread = threading.Thread(target=check_primes_in_range, args=(sub_start, sub_end))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Primes:", primes)


# === threaded_file_processor.py ===
import threading
from collections import Counter

word_count = Counter()
lock = threading.Lock()

def process_lines(lines):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with lock:
        word_count.update(local_counter)

def threaded_file_processing(file_path, num_threads=4):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    chunk_size = len(lines) // num_threads
    threads = []
    for i in range(num_threads):
        chunk = lines[i * chunk_size : (i + 1) * chunk_size] if i != num_threads - 1 else lines[i * chunk_size:]
        thread = threading.Thread(target=process_lines, args=(chunk,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Word Counts:", dict(word_count))
