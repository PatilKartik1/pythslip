''' Write a Python program to accept and convert string in uppercase or vice versa'''


def convert_case(string):
    """
    Accepts a string and converts it to uppercase if it's in lowercase, or vice versa.
    
    Parameters:
        string (str): The input string to be converted.
    
    Returns:
        str: The converted string.
    """
    return string.swapcase()

# Example usage:
input_string = input("Enter a string: ")
converted_string = convert_case(input_string)
print("Converted string:", converted_string)
