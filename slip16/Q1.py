'''Write a Python program to create tuple of n numbers, print the first half values of tuple in 
one line and the last half values of tuple on next line. '''


def print_half_tuple(tup):
    """
    Print the first half values of a tuple in one line 
    and the last half values of the tuple on the next line.
    
    Parameters:
        tup (tuple): The tuple containing the numbers.
    
    Returns:
        None
    """
    # Calculate the midpoint of the tuple
    midpoint = len(tup) // 2
    
    # Print the first half values of the tuple in one line
    print("First half:", end=" ")
    for i in range(midpoint):
        print(tup[i], end=" ")
    
    # Print a new line
    print()
    
    # Print the last half values of the tuple on the next line
    print("Last half:", end=" ")
    for i in range(midpoint, len(tup)):
        print(tup[i], end=" ")

# Test the function
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Example tuple
print_half_tuple(numbers)
