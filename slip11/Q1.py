''' Write a Python program to accept the strings which contains all vowels.'''


# Python program to accept strings that contain all vowels

def contains_all_vowels(string):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Convert the input string to lowercase to handle case-insensitivity
    string_lower = string.lower()
    # Check if all vowels are present in the input string
    if all(vowel in string_lower for vowel in vowels):
        return True
    else:
        return False

# Test the function
input_string = input("Enter a string: ")
if contains_all_vowels(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
