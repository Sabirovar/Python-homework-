# 1. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
from datetime import date
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # format: (YYYY, MM, DD)

    def age(self):
        today = date.today()
        return today.year - self.birth_date[0] - ((today.month, today.day) < (self.birth_date[1], self.birth_date[2]))


# 3. Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Error: Division by zero"


# 4. Shape and Subclasses
class Shape:
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError

class CircleShape(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# 5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node: return Node(key)
            if key < node.key: node.left = _insert(node.left, key)
            else: node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(node, key):
            if not node or node.key == key: return node
            return _search(node.left, key) if key < node.key else _search(node.right, key)
        return _search(self.root, key)


# 6. Stack Data Structure
class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None


# 7. Linked List Data Structure
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}  # item_name -> price

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total(self):
        return sum(self.items.values())


# 9. Stack with Display
class StackWithDisplay(Stack):
    def display(self):
        for item in reversed(self.items):
            print(item)


# 10. Queue Data Structure
class Queue:
    def __init__(self): self.queue = []
    def enqueue(self, item): self.queue.append(item)
    def dequeue(self): return self.queue.pop(0) if self.queue else None


# 11. Bank Class
class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self): self.accounts = {}

    def create_account(self, acc_no, name):
        self.accounts[acc_no] = Account(acc_no, name)

    def get_balance(self, acc_no):
        acc = self.accounts.get(acc_no)
        return acc.balance if acc else None

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].withdraw(amount):
                self.accounts[to_acc].deposit(amount)
                return True
        return False
