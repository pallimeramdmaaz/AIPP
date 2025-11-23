def bubble_sort(arr):
    """
    Bubble Sort algorithm - compares adjacent elements and swaps them if needed.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Example
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", numbers)
    
    sorted_array = bubble_sort(numbers)
    print("Sorted array:", sorted_array)

    # Another example: sorting a list of strings
    fruits = ["pear", "apple", "orange", "banana"]
    print("Original fruits:", fruits)
    sorted_fruits = bubble_sort(fruits.copy())
    print("Sorted fruits:", sorted_fruits)

    # Another example: sorting floats
    floats = [3.14, 2.71, -1.0, 0.0]
    print("Original floats:", floats)
    print("Sorted floats:", bubble_sort(floats))
