def quick_sort(arr):
    """Quick sort using list comprehensions"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# In-place Quick Sort (more efficient)
def quick_sort_inplace(arr, low=0, high=None):
    """In-place quick sort using Hoare partition scheme"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print("Quick Sort:", quick_sort(arr.copy()))
print("Quick Sort (In-place):", quick_sort_inplace(arr.copy()))


def binary_search_iterative(arr, target):
    """Iterative binary search implementation"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example
sorted_arr = [11, 12, 22, 25, 34, 64, 90]
print("Binary Search (Iterative):", binary_search_iterative(sorted_arr, 22))


def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search implementation"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print("Binary Search (Recursive):", binary_search_recursive(sorted_arr, 22))




def fibonacci_recursive(n):
    """Recursive Fibonacci (inefficient for large n)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n, memo={}):
    """Fibonacci with memoization (optimized)"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_iterative(n):
    """Iterative Fibonacci (most efficient)"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example
print("Fibonacci (Recursive, n=10):", fibonacci_recursive(10))
print("Fibonacci (Memoized, n=10):", fibonacci_memoization(10))
print("Fibonacci (Iterative, n=10):", fibonacci_iterative(10))


def tower_of_hanoi(n, source, target, auxiliary):
    """Solve Tower of Hanoi problem recursively"""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example
print("\nTower of Hanoi (3 disks):")
tower_of_hanoi(3, 'A', 'C', 'B')



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Append node to end of list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Prepend node to beginning of list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        """Delete node with given key"""
        if self.head and self.head.data == key:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next
    
    def search(self, key):
        """Search for node with given key"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def display(self):
        """Display the linked list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty"

# Example
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print("\nLinked List:", ll.display())
ll.reverse()
print("Reversed Linked List:", ll.display())
print("Search for 2:", ll.search(2))




# Stack using Python list (built-in)
class StackList:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack[::-1]  # Display from top to bottom

# Stack using Linked List
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = self.top.next
        self._size -= 1
        return popped.data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example
print("\nStack (List Implementation):")
stack_list = StackList()
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)
print("Stack:", stack_list.display())
print("Pop:", stack_list.pop())
print("Peek:", stack_list.peek())

print("\nStack (Linked List Implementation):")
stack_ll = StackLinkedList()
stack_ll.push(10)
stack_ll.push(20)
stack_ll.push(30)
print("Stack:", stack_ll.display())
print("Pop:", stack_ll.pop())
print("Peek:", stack_ll.peek())



# Simple Queue using List
class QueueList:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return self.queue

# Queue using Linked List
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        
        if self.front is None:
            self.rear = None
        
        self._size -= 1
        return temp.data
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            return None
        return self.rear.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
    
    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Circular Queue
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0
    
    def enqueue(self, item):
        if self.is_full():
            return False
        
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        item = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1
        return item
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def display(self):
        if self.is_empty():
            return []
        
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return result

# Priority Queue (Min Heap)
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def display(self):
        return [(priority, item) for priority, _, item in sorted(self.heap)]

# Example
print("\nQueue (List Implementation):")
queue_list = QueueList()
queue_list.enqueue(1)
queue_list.enqueue(2)
queue_list.enqueue(3)
print("Queue:", queue_list.display())
print("Dequeue:", queue_list.dequeue())
print("Front:", queue_list.front())

print("\nQueue (Linked List Implementation):")
queue_ll = QueueLinkedList()
queue_ll.enqueue(10)
queue_ll.enqueue(20)
queue_ll.enqueue(30)
print("Queue:", queue_ll.display())
print("Dequeue:", queue_ll.dequeue())
print("Front:", queue_ll.get_front())
print("Rear:", queue_ll.get_rear())

print("\nCircular Queue (Capacity=5):")
cq = CircularQueue(5)
for i in range(1, 6):
    cq.enqueue(i)
print("Circular Queue:", cq.display())
print("Dequeue:", cq.dequeue())
print("After dequeue:", cq.display())

print("\nPriority Queue:")
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)
print("Priority Queue:", pq.display())
print("Pop (highest priority):", pq.pop())