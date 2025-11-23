a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
