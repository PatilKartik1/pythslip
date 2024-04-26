''' Write a Python program to print the set difference and a symmetric difference of two sets. '''


def print_set_operations(set1, set2):
    """
    Print the set difference and symmetric difference of two sets.

    Args:
    set1 (set): The first set.
    set2 (set): The second set.
    """
    # Set difference: elements in set1 but not in set2
    difference = set1 - set2
    print("Set Difference (elements in set1 but not in set2):", difference)
    
    # Symmetric difference: elements that are in either set1 or set2, but not in both
    symmetric_difference = set1.symmetric_difference(set2)
    print("Symmetric Difference (elements that are in either set1 or set2, but not in both):", symmetric_difference)

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print the set operations
print_set_operations(set1, set2)
