numbers = [1, 2, 3]

try:
    print(numbers[4])
except IndexError:
    print("Error: List index out of range!")
