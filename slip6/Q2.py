''' Write a Python program to create and display all combinations of letters, selecting each 
letter from a different key in a dictionary.
Sample data: {'1':['a','b'], 2':['c','d']} 
Expected Output: 
ac 
ad 
bc 
bd'''

from itertools import product

def display_combinations(dictionary):
    """
    Create and display all combinations of letters from a dictionary, selecting each letter from a different key.

    Args:
    dictionary (dict): The dictionary containing keys and corresponding lists of letters.
    """
    # Get the values (lists of letters) from the dictionary
    values = list(dictionary.values())
    
    # Generate all combinations of letters using product function
    combinations = product(*values)
    
    # Print each combination
    for combination in combinations:
        print(''.join(combination))

# Sample data
sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Display combinations
display_combinations(sample_data)
