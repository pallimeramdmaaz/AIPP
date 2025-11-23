def divide_numbers(a, b):
    """
    Divides two numbers and handles common errors.

    This function attempts to divide 'a' by 'b'. It uses try-except blocks to
    safely handle:
      - ZeroDivisionError: when the second number is zero.
      - TypeError: when inputs are not valid numbers.

    Returns:
        The division result, or an error message as a string.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."


# ----- Test Inputs -----

print("Test 1:", divide_numbers(10, 2))       # 5
print("Test 2:", divide_numbers(15, 3))       # 5
print("Test 3:", divide_numbers(7, 2))        # 3.5
print("Test 4:", divide_numbers(10, 0))       # Error: Division by zero
print("Test 5:", divide_numbers("a", 5))      # Error: Invalid type
print("Test 6:", divide_numbers(20, "b"))     # Error: Invalid type
print("Test 7:", divide_numbers(None, 3))     # Error: Invalid type
