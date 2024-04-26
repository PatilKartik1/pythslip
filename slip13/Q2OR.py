''' Write a Python program to generate and print a dictionary that contains a number (between 
1 and n) in the form (x, x*x). 
Sample Dictionary (n = 5) 
Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} '''



# Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

def generate_squared_dictionary(n):
    # Initialize an empty dictionary to store the result
    squared_dict = {}

    # Generate the dictionary with numbers from 1 to n and their squares
    for i in range(1, n + 1):
        squared_dict[i] = i * i

    return squared_dict

# Sample Dictionary (n = 5)
n = 5
# Generate the dictionary
result_dict = generate_squared_dictionary(n)
# Print the dictionary
print("Sample Dictionary (n = 5):", result_dict)
