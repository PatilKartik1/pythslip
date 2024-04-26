''' Write a Python program to find the length of a string without using built-in function.'''


# Python program to find the length of a string without using built-in function

def find_length(string):
    # Initialize a counter variable
    length = 0
    
    # Iterate through each character in the string
    for char in string:
        # Increment the counter for each character
        length += 1
    
    return length

# Test the function
input_string = input("Enter a string: ")
length = find_length(input_string)
print("Length of the string:", length)
