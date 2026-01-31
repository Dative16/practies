class Person:
    cournt = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old"
    
    def display_info(self):
        print(self.introduce())
              

p1 = Person("Alice", 20)
p1.display_info()

p2 = Person("Bob", 22)
p2.display_info()


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):  # Polymorphism
        print(f"Hi, I am {self.name}, {self.age} years old, and my ID is {self.student_id}")

s1 = Student("Bob", 22, "CS101")
s1.introduce()