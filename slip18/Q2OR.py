''' Write a Python program to count frequency of each character in a given string using user 
defined function. '''


# Function to count the frequency of each character in a string
def count_frequency(string):
    frequency = {}  # Initialize an empty dictionary to store the frequency of characters

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            frequency[char] = 1
    
    return frequency

# Main function to accept user input and display character frequencies
def main():
    user_input = input("Enter a string: ")  # Accept user input string
    frequencies = count_frequency(user_input)  # Call the function to count character frequencies

    # Display the frequencies
    print("Character frequencies:")
    for char, freq in frequencies.items():
        print(f"'{char}': {freq}")

# Execute the main function
if __name__ == "__main__":
    main()
