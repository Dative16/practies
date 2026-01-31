student = {
    'name': 'Bob',
    'age': 22,
    'courses': ['Math', 'Science', 'Art'],
    'marks': [90, 85, 88]
}

print("Student Name:", student['name'])


for item in student.values():
    print(item)

for key in student.keys():
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")
    
#  Adding data to dictionary
student['grade'] = 'A'
print("Updated Student Dictionary:", student)

for mark in student['marks']:
    print("Mark:", mark)

for course in student['courses']:
    print("Course:", course)


