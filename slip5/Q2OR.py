''' Write a Python program to create a dictionary from two lists without losing duplicate 
values. 
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3] 
 Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': 
 {3}, 'Class-V': {1}}) '''

from collections import defaultdict

def create_dictionary(keys, values):
    """
    Create a dictionary from two lists without losing duplicate values.

    Args:
    keys (list): The list of keys.
    values (list): The list of values.

    Returns:
    defaultdict: The dictionary created from the two lists.
    """
    # Initialize a defaultdict with set as the default factory
    result = defaultdict(set)
    
    # Iterate through each key-value pair and append the value to the corresponding key
    for key, value in zip(keys, values):
        result[key].add(value)
    
    return result

# Sample lists
keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]

# Create the dictionary
result_dict = create_dictionary(keys, values)

print("Expected Output:", result_dict)
