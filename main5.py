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
