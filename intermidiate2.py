"""
Python Practice File: Algorithms & Data Structures
Covers:
- Sorting Algorithms
- Binary Search
- Recursive Functions
- Linked Lists
- Stacks (Two Implementations)
- Queues (Simple & Circular)
"""

# -----------------------------
# 1. SORTING ALGORITHMS
# -----------------------------

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)
print("Bubble Sort:", bubble_sort(numbers.copy()))
print("Selection Sort:", selection_sort(numbers.copy()))

# -----------------------------
# 2. BINARY SEARCH
# -----------------------------

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_numbers = sorted(numbers)
print("Sorted List:", sorted_numbers)

value = 22
index = binary_search(sorted_numbers, value)
print(f"Value {value} found at index: {index}")

# -----------------------------
# 3. RECURSIVE FUNCTIONS
# -----------------------------

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print("Factorial of 5:", factorial(5))

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci (first 7 numbers):")
for i in range(7):
    print(fibonacci(i), end=" ")
print()

# -----------------------------
# 4. LINKED LIST
# -----------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append("Alice")
ll.append("Bob")
ll.append("Charlie")

print("Linked List:")
ll.display()

# -----------------------------
# 5. STACK (USING LIST)
# -----------------------------

class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print("Stack:", self.stack)

stack1 = StackList()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.display()
print("Popped:", stack1.pop())
stack1.display()

# -----------------------------
# 6. STACK (USING LINKED LIST)
# -----------------------------

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack is empty"
        value = self.top.data
        self.top = self.top.next
        return value

    def display(self):
        current = self.top
        print("Stack (Top to Bottom):", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

stack2 = StackLinkedList()
stack2.push("A")
stack2.push("B")
stack2.push("C")
stack2.display()
print("Popped:", stack2.pop())
stack2.display()

# -----------------------------
# 7. SIMPLE QUEUE
# -----------------------------

class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def display(self):
        print("Queue:", self.queue)

q1 = SimpleQueue()
q1.enqueue("Patient1")
q1.enqueue("Patient2")
q1.enqueue("Patient3")
q1.display()
print("Dequeued:", q1.dequeue())
q1.display()

# -----------------------------
# 8. CIRCULAR QUEUE
# -----------------------------

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            return "Queue is full"
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return "Queue is empty"
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def display(self):
        print("Circular Queue:", self.queue)

cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
print("Dequeued:", cq.dequeue())
cq.enqueue(4)
cq.display()

# -----------------------------
# END OF FILE
# -----------------------------
