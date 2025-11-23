def linear_search(lst, target):
    """
    Search for a value in a list using linear search.
    Args:
        lst: List to search in
        target: Value to search for
    
    Returns:
        Index of the target if found, otherwise -1
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
# Example
numbers = [10, 25, 30, 45, 50, 65, 80]
search_value = 45

result = linear_search(numbers, search_value)

if result != -1:
    print(f"Value {search_value} found at index: {result}")
else:
    print(f"Value {search_value} not found in the list")
