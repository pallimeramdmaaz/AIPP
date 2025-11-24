students_marks = [30, 20, 15, 18, 31, 35, 40, 45, 10, 5, 16]

def marks_above_mean(marks):
    """
    Calculate the mean of marks and return values above it.

    Args:
        marks: Iterable of numeric scores.

    Returns:
        Tuple of (mean, list of marks greater than mean).
    """
    if not marks:
        raise ValueError("Marks list must not be empty.")

    mean_value = sum(marks) / len(marks)
    above_mean = [mark for mark in marks if mark > mean_value]
    return mean_value, above_mean

print(marks_above_mean(students_marks))