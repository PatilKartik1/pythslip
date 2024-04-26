''' Write a Python program to create a dictionary from a string. 
Sample String: ’Hello all’ 
Expected output: {'e': 1, 'o': 1, 'a': 1, 'l': 4, 'H': 1} '''


# Python program to create a dictionary from a string
def create_dictionary_from_string(input_string):
    # Initialize an empty dictionary to store the character counts
    char_count = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count of the character in the dictionary
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

# Sample string
sample_string = 'Hello all'

# Create a dictionary from the sample string
result_dict = create_dictionary_from_string(sample_string)

# Print the result
print("Sample String:", sample_string)
print("Expected Output:", result_dict)
