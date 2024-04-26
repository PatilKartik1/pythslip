''' Write a Python program to count frequency of each character in a given string using user 
defined function'''

# Python program to count frequency of each character in a given string using a user-defined function

def count_character_frequency(input_string):
    # Initialize an empty dictionary to store the frequency of each character
    char_frequency = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is already in the dictionary
        if char in char_frequency:
            # If yes, increment its count
            char_frequency[char] += 1
        else:
            # If not, initialize its count to 1
            char_frequency[char] = 1
    
    return char_frequency

# Function to display the character frequency
def display_character_frequency(char_frequency):
    print("Character Frequency:")
    for char, freq in char_frequency.items():
        print(f"'{char}': {freq}")

# Sample string
sample_string = "Hello all"

# Calculate the character frequency
frequency_dict = count_character_frequency(sample_string)

# Display the character frequency
display_character_frequency(frequency_dict)
