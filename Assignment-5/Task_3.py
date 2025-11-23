#write a recursive function to compute the nth Fibonacci number.
def fibonacci(n):
    # Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
if __name__ == "__main__":
    n = 7
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
