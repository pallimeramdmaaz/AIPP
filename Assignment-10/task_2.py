def find_common(a, b):
    # Cleaner and faster using set intersection
    return list(set(a) & set(b))
# ---- Test Inputs ----
a1 = [1, 2, 3, 4]
b1 = [3, 4, 5, 6]
print("Test 1:", find_common(a1, b1))   # Expected: [3, 4]

a2 = [10, 20, 30]
b2 = [40, 50, 60]
print("Test 2:", find_common(a2, b2))   # Expected: []

a3 = [1, 2, 2, 3]
b3 = [2, 2, 4]
print("Test 3:", find_common(a3, b3))   # Expected: [2]

a4 = ["apple", "banana", "mango"]
b4 = ["banana", "grape", "apple"]
print("Test 4:", find_common(a4, b4))   # Expected: ['apple', 'banana']

a5 = [1, "a", 3.5, "hello"]
b5 = ["hello", 1, 7]
print("Test 5:", find_common(a5, b5))   # Expected: [1, 'hello']
