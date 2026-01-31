"""Nested List Comprehensions Example"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
squared_matrix = [[x**2 for x in row] for row in matrix]

print(squared_matrix)
print(matrix[2][2])

print("Original Matrix:")

for row in matrix:
    print(row)
    
print("\nSquared Matrix:")
for row in squared_matrix:
    print(row)

# get individual elements using nested loops
print("\nIndividual Elements:")
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(f"Element at ({row},{col}): {matrix[row][col]}")


"""Tuple"""
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
signle_tuple = (42,)

print("Tuple:", my_tuple)
print("Single Element Tuple:", signle_tuple)
print("Accessing elements in tuple:")
for i in range(len(my_tuple)):
    print(f"Element at index {i}: {my_tuple[i]}")
    


"""Set Operations"""
# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# Set operations
union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b
print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("The Difference_set", difference_set)


