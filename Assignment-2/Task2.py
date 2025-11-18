def is_palindrome(string):
    # Convert to lowercase and keep only alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in string if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned_str == cleaned_str[::-1]

# Test cases
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "12321"
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' is{' ' if result else ' not '}a palindrome")
