def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string.

    Raises:
        TypeError: if s is not a str
    """
    if not isinstance(s, str):
        raise TypeError("reverse_string expects a str")
    return s[::-1]


if __name__ == "__main__":
    # Example usage
    print(reverse_string("hello"))  # olleh
    print(reverse_string(""))       # (empty string)
    print(reverse_string("Madhu"))  # uhd aM -> uhdaM
