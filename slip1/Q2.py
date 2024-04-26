''' Write a Python program to find set difference, union, intersection and symmetric 
# difference. '''


# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Set difference
difference = set1 - set2
print("Set Difference:", difference)  # Output: {1, 2, 3}

# Set union
union = set1 | set2
print("Set Union:", union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Set intersection
intersection = set1 & set2
print("Set Intersection:", intersection)  # Output: {4, 5}

# Set symmetric difference
symmetric_difference = set1 ^ set2
print("Set Symmetric Difference:", symmetric_difference)  # Output: {1, 2, 3, 6, 7, 8}
