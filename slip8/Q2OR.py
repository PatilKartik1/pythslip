''' Write a Python function to multiply all the numbers in a list. [20 M] 
Sample-List: (8, 2, 3, -1, 7) 
Expected Output: -336 '''


def multiply_numbers(lst):
    """
    Function to multiply all the numbers in a list.

    Args:
    lst (list): The input list of numbers.

    Returns:
    int or float: The product of all the numbers in the list.
    """
    result = 1
    for num in lst:
        result *= num
    return result

# Sample list
sample_list = (8, 2, 3, -1, 7)
# Call the function and print the result
print("Expected Output:", multiply_numbers(sample_list))
