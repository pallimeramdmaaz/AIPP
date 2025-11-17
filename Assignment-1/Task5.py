def find_largest_number(numbers):
    if not numbers:  # Check if list is empty
        return None
    
    largest = numbers[0]  # Initialize largest with first element
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

# Example usage
if __name__ == "__main__":
    # Test cases
    numbers = [5, 2, 9, 1, 7, 6, 3]
    result = find_largest_number(numbers)
    print(f"The largest number in {numbers} is: {result}")
