'''Write a Python program to print a dictionary where the keys are numbers between 1 and 
15 (both included) and the values are square of keys. 
Sample Dictionary: {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500} '''

# Initialize an empty dictionary
square_dict = {}

# Populate the dictionary with keys from 1 to 15 and their squares as values
for num in range(1, 14):
    square_dict[num] = num ** 2

# Print the resulting dictionary
print("Sample Dictionary:", square_dict)

