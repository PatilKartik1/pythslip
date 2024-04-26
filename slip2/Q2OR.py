'''Write a Python program to perform given operations on set. 
a. check whether 2 sets are equal or not 
b. Symmetric difference 
c. Intersection of sets 
d. Find maximum and the minimum value in a set. '''


# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# a. Check whether 2 sets are equal or not
equal = set1 == set2
print("Are the sets equal?", equal)  # Output: False

# b. Symmetric difference
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)  # Output: {1, 2, 6, 7}

# c. Intersection of sets
intersection = set1.intersection(set2)
print("Intersection:", intersection)  # Output: {3, 4, 5}

# d. Find maximum and minimum value in a set
maximum_value = max(set1)
minimum_value = min(set1)
print("Maximum value:", maximum_value)  # Output: 5
print("Minimum value:", minimum_value)  # Output: 1
