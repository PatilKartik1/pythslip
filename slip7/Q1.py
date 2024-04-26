''' Write a Python program to find maximum and the minimum value in a set. '''


def find_max_min(s):
    """
    Find the maximum and minimum value in a set.

    Args:
    s (set): The input set.

    Returns:
    tuple: A tuple containing the maximum and minimum values.
    """
    if not s:
        return None, None
    else:
        return max(s), min(s)

# Sample set
sample_set = {3, 1, 4, 1, 5, 9, 2, 6, 5}

# Find maximum and minimum values
max_value, min_value = find_max_min(sample_set)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
