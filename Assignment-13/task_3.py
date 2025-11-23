class Student:
    """Represents a student with name, age, and marks."""

    def __init__(self, name, age, marks):
        """
        Initialize student details.

        Args:
            name (str): Student's name
            age (int): Student's age
            marks (list): List containing marks in subjects
        """
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        """Display student name and age."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def total_marks(self):
        """Calculate and return total marks."""
        return sum(self.marks)


# ---------- Example usage ----------

# Sample input values
name = "Rohit"
age = 19
marks = [88, 76, 92]   # Three subject marks

# Creating object
student = Student(name, age, marks)

# Output
student.show_details()
print("Total Marks:", student.total_marks())
