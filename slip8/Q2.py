''' Write a Python program to match key values in two dictionaries. [20 M] 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2} 
Expected output: key1: 1 is present in both x and y '''

# Define two sample dictionaries
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

# Iterate through the keys in the first dictionary
for key in x:
    # Check if the key exists in the second dictionary and if the values match
    if key in y and x[key] == y[key]:
        # Print the key and its corresponding value if it matches in both dictionaries
        print(f"{key}: {x[key]} is present in both x and y")
