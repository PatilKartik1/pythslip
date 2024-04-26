''' Write a Python program to accept a string and from a given string where all occurrences of 
its first character have been changed to '$', except the first char itself. '''


# Python program to modify a string where all occurrences of its first character, except the first occurrence, are changed to '$'

def modify_string(input_string):
    # Get the first character of the input string
    first_char = input_string[0]
    
    # Replace all occurrences of the first character, except the first occurrence, with '$'
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    
    return modified_string

# Accept input from the user
input_string = input("Enter a string: ")

# Call the function to modify the string
modified_string = modify_string(input_string)

# Print the modified string
print("Modified string:", modified_string)
