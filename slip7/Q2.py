''' Write a Python script to generate and print a dictionary that contains a number (between 1 
to n) in the form (x, x*x). 
Sample Dictionary (n = 5): Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''



def generate_squared_dictionary(n):
    """
    Generate and print a dictionary that contains a number (between 1 to n) in the form (x, x*x).

    Args:
    n (int): The upper limit of the numbers in the dictionary.

    Returns:
    dict: A dictionary containing numbers from 1 to n as keys and their squares as values.
    """
    squared_dict = {}
    for i in range(1, n + 1):
        squared_dict[i] = i * i
    return squared_dict

# Sample Dictionary (n = 5)
n = 5
sample_dict = generate_squared_dictionary(n)
print("Sample Dictionary (n = {}):".format(n), sample_dict)
