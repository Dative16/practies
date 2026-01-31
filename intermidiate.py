"""
Python Lesson Practice File
Covers:
- Dictionaries & Dictionary Methods
- List Comprehensions & Generators
- Modules & Importing Libraries
- File Handling (Read/Write)
- Error Handling with Try/Except
- Classes & Objects
- Inheritance & Polymorphism
"""

# -----------------------------
# 1. DICTIONARIES
# -----------------------------

student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}

print("Student Name:", student["name"])

# Add new key
student["grade"] = "A"

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Safe access
print("Phone:", student.get("phone", "Not Available"))

# -----------------------------
# 2. LIST COMPREHENSIONS
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6]

# Normal loop
squares = []
for n in numbers:
    squares.append(n ** 2)

print("Squares (loop):", squares)

# List comprehension
squares_comp = [n ** 2 for n in numbers]
print("Squares (comprehension):", squares_comp)

# -----------------------------
# 3. GENERATORS
# -----------------------------

def square_generator(nums):
    for n in nums:
        yield n ** 2

print("Generator output:")
for value in square_generator(numbers):
    print(value)

# -----------------------------
# 4. MODULES & IMPORTS
# -----------------------------

import math
import random

print("Square root of 16:", math.sqrt(16))
print("Random number:", random.randint(1, 10))

# -----------------------------
# 5. FILE HANDLING
# -----------------------------

# Writing to a file
try:
    with open("students.txt", "w") as file:
        file.write("Alice,85\nBob,78\nCharlie,90")
    print("File written successfully")
except Exception as e:
    print("Error writing file:", e)

# Reading from a file
try:
    with open("students.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)
except Exception as e:
    print("Error reading file:", e)

# -----------------------------
# 6. ERROR HANDLING
# -----------------------------

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Execution complete")

# -----------------------------
# 7. CLASSES & OBJECTS
# -----------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")

p1 = Person("Alice", 20)
p1.introduce()

# -----------------------------
# 8. INHERITANCE & POLYMORPHISM
# -----------------------------

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):  # Polymorphism
        print(f"Hi, I am {self.name}, {self.age} years old, and my ID is {self.student_id}")

s1 = Student("Bob", 22, "CS101")
s1.introduce()

# -----------------------------
# END OF LESSON FILE
# -----------------------------
