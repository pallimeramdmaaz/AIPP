class Employee:
    """
    A class to represent an employee with a name and salary.
    Provides methods to increase salary and display employee details.
    """

    def __init__(self, name, salary):
        """
        Initialize an Employee object.

        Parameters:
        name (str): Employee name
        salary (float/int): Employee salary
        """
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        """
        Increase the salary by a given percentage.

        Parameters:
        percent (float): Percentage by which salary should increase
        """
        self.salary += self.salary * percent / 100

    def display_info(self):
        """
        Display the employee's information in a formatted way.
        """
        print(f"Employee Name : {self.name}")
        print(f"Salary        : ₹{self.salary:.2f}")
        print("-" * 30)


# ---- Test Code ----

e1 = Employee("Madhu", 20000)
e1.display_info()

e1.increase_salary(10)
e1.display_info()

e2 = Employee("Rahul", 35000)
e2.display_info()

e2.increase_salary(20)
e2.display_info()
