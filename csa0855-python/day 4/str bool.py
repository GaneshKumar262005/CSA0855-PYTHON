def is_valid_string(s: str) -> bool:
    """
    Checks if the string is valid (non-empty) after stripping whitespace.

    Parameters:
        s (str): Input string to validate.

    Returns:
        bool: True if the stripped string is not empty, False otherwise.
    """
    stripped_string = s.strip()  # Remove leading and trailing whitespace
    return bool(stripped_string)  # Returns False if stripped_string is empty

# Test cases
print(is_valid_string("   "))         # Output: False (only spaces)
print(is_valid_string("Hello"))       # Output: True
print(is_valid_string("   Hello   ")) # Output: True
print(is_valid_string(""))            # Output: False (empty string)
