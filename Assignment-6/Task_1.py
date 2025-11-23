# Student class definition
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 50


# Testing the Student class

# Create student instances
student1 = Student("Alice", 16, 75)
student2 = Student("Bob", 17, 45)

# Print details and passing status
print(student1.get_details())
print("Passing:", student1.is_passing())

print(student2.get_details())
print("Passing:", student2.is_passing())
