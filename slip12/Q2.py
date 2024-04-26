''' Write a Python program to accept string and remove the characters which have odd index 
values of a given string using user defined function. '''


# Python program to remove characters at odd indices from a string using a user-defined function

def remove_odd_index_chars(input_str):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through the characters of the input string
    for index, char in enumerate(input_str):
        # Check if the index is even (indices start from 0)
        if index % 2 == 0:
            # Append the character to the result string if the index is even
            result += char
    
    # Return the resulting string without characters at odd indices
    return result

# Test the function
input_string = input("Enter a string: ")
result_string = remove_odd_index_chars(input_string)
print("String after removing characters at odd indices:", result_string)
