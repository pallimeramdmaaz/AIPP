students_marks = [30, 29, 15, 28, 31, 35, 40, 45, 10, 5, 16]

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

def format_mean_output(mean_value, above_mean):
    """Format the result string to match the requested output."""
    mean_str = (
        str(int(mean_value))
        if isinstance(mean_value, (int, float)) and mean_value.is_integer()
        else f"{mean_value:.2f}"
    )
    above_str = ",".join(str(mark) for mark in above_mean) if above_mean else "None"
    return (
        f"Mean value = {mean_str}, "
        f"Students marks greater than the mean value i.e {mean_str} = {above_str}"
    )

if __name__ == "__main__":
    mean, above = marks_above_mean(students_marks)
    print(format_mean_output(mean, above))
