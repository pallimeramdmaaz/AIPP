def calculate_average(scores):
    """Return the average of the list of scores."""
    total = 0
    for s in scores:
        total += s
    return total / len(scores)


def find_highest(scores):
    """Return the highest score in the list."""
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest


def find_lowest(scores):
    """Return the lowest score in the list."""
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    """Print the average, highest, and lowest score."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Scores:", scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# ---------------------------
# Example test inputs
# ---------------------------

print("Test 1:")
process_scores([45, 67, 89, 90, 56])

print("\nTest 2:")
process_scores([10, 20, 30, 40, 50])

print("\nTest 3:")
process_scores([98, 76, 88, 92, 100])

print("\nTest 4:")
process_scores([5, 15, 25])

print("\nTest 5:")
process_scores([70, 70, 85, 90, 90, 100])
